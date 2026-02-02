
# 📗 Low-Rank Adaptation (LoRA & QLoRA):

## Fine-Tuning Large Language Models When You Don’t Have Infinite GPUs

---

## Learning Objectives

By the end of this notebook, you will be able to:

* Explain **where fine-tuning fits** in the LLM training pipeline
* Quantify **why full fine-tuning is impractical** on consumer hardware
* Understand **intrinsic dimensionality** and why LoRA works
* Implement **LoRA from scratch (conceptually)** and with Hugging Face PEFT (practically)
* Reason about **rank, alpha, dropout, and layer targeting**
* Identify **failure modes** of LoRA
* Understand why **QLoRA** is LoRA “2.0” and when to use it
* Make informed decisions when a fine-tune **doesn’t work**

---

## 0. The Problem (Why You Should Care)

> **Scenario:**
> You have **8–16 GB of GPU VRAM**.
> You want to fine-tune a **7B or 8B parameter LLM** on your own dataset.
> Full fine-tuning requires **20–30+ GB** *just to load the model*, not counting gradients or optimizer state.

**Question:**
👉 *What do you do?*

This notebook is about the answer.

---

## 1. Where Fine-Tuning Fits in the LLM Training Pipeline

Large language models are **not trained in one step**.

### The modern pipeline:

1. **Pre-training**

   * Trillions of tokens
   * Next-token prediction
   * Learns general language, facts, structure

2. **Instruction tuning**

   * Makes models conversational (e.g., ChatGPT-style behavior)

3. **Safety tuning / alignment**

   * Prevents harmful or disallowed outputs

4. **Domain fine-tuning**

   * Law, finance, healthcare, code, music, etc.

5. **Task-specific fine-tuning**

   * Classification, extraction, summarization, custom behaviors

**Key insight:**
You are **not training from scratch**.
You are **adapting** a very large, very capable model.

---

## 2. Why Full Fine-Tuning Breaks Down (The GPU Memory Wall)

Let’s quantify the problem.

### Memory needed for model weights

```python
def model_memory_gb(params, bytes_per_param):
    return params * bytes_per_param / (1024**3)

models = {
    "7B": 7e9,
    "13B": 13e9
}

for name, p in models.items():
    print(f"{name} FP16 weights only: {model_memory_gb(p, 2):.2f} GB")
```

### But training needs more than weights

During training, you also store:

* Gradients
* Optimizer states (often 2–4× model size)

Rule of thumb: **~4–6× model size**

👉 A 7B model can easily require **25–40 GB VRAM** for full fine-tuning.

**Conclusion:**
Full fine-tuning is **hardware-limited**, not idea-limited.

---

## 3. Precision & Quantization (How Models Get Smaller)

### Floating-point precision

* FP32: high precision, high memory
* FP16 / BF16: standard for training
* INT8 / INT4: quantized representations

Let’s see precision loss directly.

```python
import torch

x = torch.tensor([7.123456789], dtype=torch.float32)
print("FP32:", x)
print("FP16:", x.half())
```

Small rounding errors are usually fine — but they **accumulate** in deep networks.

---

### Quantization (Conceptual)

Quantization does **not** just “drop bits.”

Instead:

* Values are scaled
* Stored in fewer bits
* De-quantized during computation

**Key result from recent research:**
👉 **4-bit quantization often preserves model quality** when done carefully.

---

## 4. The Core Idea: Intrinsic Dimensionality

A critical observation from Facebook Research (2021):

> Many downstream tasks live in a **much lower-dimensional subspace** than the full parameter space.

### Intuition

* Large models already know *how language works*
* Fine-tuning often nudges behavior, not knowledge
* You don’t need to move in all directions — only a few

**Analogy:**
You’re not rebuilding a piano.
You’re tuning a few strings.

---

## 5. Enter LoRA: Low-Rank Adaptation

### The LoRA idea

Instead of updating the full weight matrix **W**, we write:

[
W = W_0 + \Delta W
]

Where:

* (W_0) is **frozen**
* (\Delta W = B A)
* (B \in \mathbb{R}^{d \times r}), (A \in \mathbb{R}^{r \times k})
* (r \ll d, k)

---

### Why this saves parameters

Example:

* Full matrix: (1000 \times 1000 = 1,000,000) parameters
* Rank-8 LoRA:
  (1000 \times 8 + 8 \times 1000 = 16,000) parameters

That’s **62× fewer trainable parameters**.

---

## 6. Rank Decomposition: Make It Concrete

```python
import torch

# Full matrix
W = torch.randn(5, 5)
print("Full rank:", torch.linalg.matrix_rank(W))

# Low-rank construction
B = torch.randn(5, 1)
A = torch.randn(1, 5)
W_low = B @ A
print("Low rank:", torch.linalg.matrix_rank(W_low))
```

**Observation:**
Low-rank matrices still affect *every entry* — but through fewer degrees of freedom.

---

## 7. How LoRA Is Initialized (Critical Detail)

LoRA matrices are initialized so that:

[
\Delta W = BA = 0 \text{ at step 0}
]

* (B = 0)
* (A \sim \mathcal{N}(0, \sigma^2))

👉 Training starts from the **original model behavior**.

---

## 8. Where LoRA Is Applied in Transformers

Transformers are dominated by **linear layers**:

* Attention: Q, K, V, O projections
* Feed-forward networks (MLP layers)

**Rule of thumb:**

| Layer      | Use LoRA?                      |
| ---------- | ------------------------------ |
| Q, V       | Yes (almost always)            |
| K, O       | Often                          |
| MLP        | Yes (especially for reasoning) |
| Embeddings | Usually no                     |

---

## 9. Hyperparameters That Actually Matter

### Rank (r)

* Controls **capacity**
* Typical values: 8–64
* QLoRA paper: rank often **does not matter** in range 8–256 *if all layers are adapted*

---

### Alpha (α)

LoRA output is scaled as:

[
\text{scale} = \frac{\alpha}{r}
]

* Microsoft LoRA: (\alpha = 2r) → 2× effect
* QLoRA: (\alpha = 16, r = 64) → 0.25× effect

**Interpretation:**
Alpha **decouples learning rate from rank**.

---

### Dropout

* Prevents overfitting
* QLoRA defaults:

  * 0.1 for 7B / 13B
  * 0.05 for 33B+

---

## 10. LoRA in Practice with Hugging Face PEFT

```python
from peft import LoraConfig, get_peft_model

config = LoraConfig(
    r=64,
    lora_alpha=16,
    target_modules=["q_proj", "v_proj"],
    lora_dropout=0.1,
    bias="none"
)

model = get_peft_model(base_model, config)
model.print_trainable_parameters()
```

💡 **Eureka moment:**
You’ll often see **<0.5% trainable parameters**.

---

## 11. Critical Insight from the QLoRA Paper

Two findings that change practice:

1. **Training ALL linear layers is essential** to match full fine-tuning
2. **Rank often does not matter** (8–256) if all layers are adapted

👉 Quantization noise is global → adaptation must be global.

---

## 12. QLoRA: LoRA + Quantization

### What QLoRA does

* Quantizes **base model weights** to 4-bit
* Keeps **LoRA adapters in full precision**
* Uses NF4 + double quantization

**Result:**
7B–13B models fine-tuned on **single GPUs**

---

## 13. Failure Modes (What the Videos Don’t Emphasize)

### LoRA struggles when:

| Situation                    | Symptom       | Fix                       |
| ---------------------------- | ------------- | ------------------------- |
| Large domain shift           | Underfitting  | Increase rank or pretrain |
| Safety-aligned contradiction | Model resists | Higher rank + all layers  |
| Tiny dataset                 | Overfitting   | Increase dropout          |
| Attention-only LoRA          | Weak learning | Include MLP layers        |

---

## 14. LoRA vs Other Tools (Decision Guide)

| Goal             | Best Tool                   |
| ---------------- | --------------------------- |
| New facts        | Continued pretraining / RAG |
| Style / behavior | LoRA                        |
| Safety override  | Hard                        |
| Fast iteration   | LoRA                        |
| Zero training    | Prompting                   |

---

## 15. Merging, Swapping, and Deployment

* LoRA adapters can be:

  * **Merged** → zero inference overhead
  * **Swapped** → task-specific adapters
* Enables a **model zoo**:

  * One base model
  * Many behaviors

---

## 16. Final Takeaways

* LoRA learns **directions of change**, not new knowledge
* Intrinsic dimension explains why low rank works
* QLoRA makes LoRA practical on consumer hardware
* Hyperparameters matter less than **which layers you adapt**
* Failure is informative — debug it

---

## What You Should Be Able to Do Now

✅ Explain *why* LoRA works
✅ Implement it correctly
✅ Diagnose failures
✅ Choose between LoRA, QLoRA, RAG, or pretraining
✅ Fine-tune large models **without infinite GPUs**

---

If you want next steps, we can:

* Turn this into a **graded lab**
* Add **guided failure experiments**
* Adapt it for **Humanitarians AI / Musinique**
* Convert it into a **90-minute workshop**

Just tell me how you want to deploy it.
