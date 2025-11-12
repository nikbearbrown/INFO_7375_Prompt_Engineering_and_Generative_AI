# Fall 2025 Midterm – Friendly Guide to AI: Prompt Engineering

## Table of Contents

* [Introduction to Large Language Models (LLMs)](#introduction-to-large-language-models-llms)
* [Understanding Randomness in AI Responses](#understanding-randomness-in-ai-responses)
* [Creating Your First Prompts](#creating-your-first-prompts)
* [How Prompting AI Differs from Programming](#how-prompting-ai-differs-from-programming)
* [Writing Effective Prompts](#writing-effective-prompts)
* [Prompt Patterns and Strategies](#prompt-patterns-and-strategies)
* [Advanced Prompt Engineering](#advanced-prompt-engineering)
* [How Large Language Models Work](#how-large-language-models-work)

---

## Introduction to Large Language Models (LLMs)

Large Language Models (LLMs) are like super-smart text prediction engines that have read vast amounts of human writing. Think of them as having read millions of books, websites, and articles.

**What makes them special:**

* They can write human-like text based on your requests
* They can answer questions by drawing on their "memory" of texts they've seen
* They can translate languages, summarize information, and even have conversations

**Popular examples you might know:**

* ChatGPT (based on OpenAI's GPT models)
* Claude (by Anthropic)
* Google's Bard/Gemini (based on PaLM and Gemini models)

**Example:**
When you ask an LLM "Write a poem about friendship," it doesn't actually understand what friendship is from personal experience. Instead, it's analyzed millions of examples of poems and writing about friendship, and can create something new based on those patterns.

---

## Understanding Randomness in AI Responses

AI responses aren't completely predictable. Even if you ask the same question twice, you might get different answers!

**Why this happens:**
LLMs decide what word comes next based on probabilities. It's like rolling weighted dice to choose each word. This randomness can be controlled through a setting called "temperature":

* **Low temperature (0.1-0.3):** More predictable responses, good for factual answers
* **High temperature (0.7-1.0):** More creative and varied responses, good for creative writing

**Example:**
Prompt: "Write a tagline for a coffee shop"

With low temperature (0.2):

> "Fresh brew, fresh start. Coffee that energizes your day."

With high temperature (0.8):

> "Where beans dream in liquid form and mornings find their purpose."

The higher temperature allows for more unexpected and creative combinations of words!

---

## Creating Your First Prompts

Prompts are the instructions you give to an AI. Learning to write good prompts is like learning to be a good teacher - clear instructions get better results!

**Key principles:**

1. **Be specific** about what you want
2. **Provide context** to help the AI understand your needs
3. **Try different approaches** if you don't get the result you want

**Example:**
Instead of asking:

> "Tell me about planets"

Try being more specific:

> "Explain the planets in our solar system in order from the sun, including one interesting fact about each planet. Keep your explanation simple enough for a middle school student."

The second prompt gives the AI clear direction about content, order, detail level, and audience.

---

## How Prompting AI Differs from Programming

Talking to AI is very different from traditional programming, where computers follow exact instructions.

**Traditional programming (like C++):**

* Requires precise syntax and rules
* One small error breaks everything
* Computer does exactly what you tell it to do, nothing more

**Prompting AI:**

* Understands natural language (how humans talk)
* Forgiving of typos and unclear instructions
* Can "guess" what you mean and fill in gaps
* May do more or less than exactly what you asked for

**Example:**
In programming, you might write:

```
for (int i = 0; i < 5; i++) {
    printf("Planet %d\n", i+1);
}
```

With AI, you just ask:

> "List the first 5 planets from the sun."

The AI understands what planets are, knows their order, and can create a proper list without you specifying every detail of how to do it.

---

## Writing Effective Prompts

A well-crafted prompt has several key components that help the AI give you exactly what you need.

**Components of great prompts:**

1. **Clear instruction** - What do you want the AI to do?
2. **Relevant context** - Background information the AI needs
3. **Examples** - Show what good output looks like
4. **Constraints** - Any limitations or specific requirements

**Example prompt structure:**

```
[Instruction] Write a short story about a lost dog finding its way home.
[Context] The story is for 8-year-old children and should teach a lesson about perseverance.
[Example] Stories like "Homeward Bound" where animals overcome obstacles.
[Constraints] Keep it under 300 words and avoid anything scary.
```

This gives the AI clear guidance on task, audience, style, and limitations.

---

## Prompt Patterns and Strategies

Certain patterns and strategies can help you get better results from AI models. These are like recipes for success!

### The Persona Pattern

Having the AI adopt a specific role can lead to more appropriate responses.

**Example:**

> "As a high school science teacher, explain how photosynthesis works in a way that would engage teenagers."

This gets better results than just "explain photosynthesis" because it gives the AI a specific perspective and audience.

### The Step-by-Step Pattern

Asking the AI to break down complex problems helps it think more logically.

**Example:**

> "Explain how to solve this math problem step-by-step: If a train travels 120 miles in 2 hours, how fast is it going in miles per hour?"

The AI's response will be more methodical:

1. Identify what we need to find: speed in mph
2. Use the formula: speed = distance ÷ time
3. Plug in values: speed = 120 miles ÷ 2 hours
4. Calculate: speed = 60 mph

This pattern is especially helpful for math, coding, and problem-solving tasks.

---

## Advanced Prompt Engineering

As you get more comfortable with basic prompts, you can use more sophisticated techniques.

### Chain of Thought Prompting

This technique helps AI reason through complex problems by showing its work.

**Example:**
Prompt: "If John has 5 apples and gives 2 to Mary, then buys 3 more and eats 1, how many apples does John have? Think through this step by step."

Response:

> "Let me solve this step by step:
>
> 1. John starts with 5 apples
> 2. John gives 2 apples to Mary, so John now has 5-2 = 3 apples
> 3. John buys 3 more apples, so John now has 3+3 = 6 apples
> 4. John eats 1 apple, so John now has 6-1 = 5 apples
>    Therefore, John has 5 apples."

This technique helps the AI avoid logical errors by breaking down its thinking.

### Few-Shot Learning

Showing examples of what you want helps the AI understand your expectations.

**Example:**

```
Convert these sentences to French:
English: "Hello, how are you?"
French: "Bonjour, comment ça va?"

English: "I like to read books."
French: "J'aime lire des livres."

English: "Where is the train station?"
French:
```

By showing examples first, you help the AI understand exactly what you want. It will likely respond with "Où est la gare?" because it recognizes the pattern.

### ReAct Prompting

ReAct combines reasoning and action to solve problems methodically.

**Example:**

> "You're trying to bake cookies but realized you don't have eggs. What alternatives could you use, and how would they affect the recipe? Think about the purpose of eggs in baking, then suggest alternatives and their effects."

This approach encourages the AI to:

1. Reason about why eggs are used (binding, moisture, leavening)
2. Consider alternatives based on this reasoning (applesauce, bananas, flax seeds)
3. Evaluate how each alternative would affect the final product

---

## How Large Language Models Work

Understanding the basics of how these AI systems work can help you use them more effectively.

### The Evolution of Text Generation

Text generation has come a long way:

* **Early systems** used simple rules and templates
* **Markov chains** predicted text based on what words commonly follow other words
* **Neural networks** learn patterns from vast amounts of text
* **Transformer architecture** (used in modern LLMs) can understand context across long passages

### The Transformer Architecture

Modern LLMs use a design called a "transformer" which has revolutionized AI.

**Key features:**

* **Attention mechanism:** Allows the AI to focus on relevant words when generating each new word
* **Parallel processing:** Can analyze all words in a sentence simultaneously
* **Bidirectional understanding:** Considers words that come both before and after

**Example of how attention works:**
In the sentence "The cat sat on the mat because it was comfortable," what does "it" refer to?

A transformer can "pay attention" to both "cat" and "mat" when processing "it," and figure out that "it" likely refers to "mat" (since cats, not mats, typically seek comfort).


Got it. I’ve added concise explanations and concrete examples for each pattern (items 4–18 from your list), ready to drop into your Midterm doc under a new section.

# How to Speak Bot: Prompt Patterns

## Persona Pattern

**What it is:** Ask the model to assume a role to shape tone, knowledge, and constraints.
**When to use:** You want domain-specific voice or perspective.

**Prompt template:**
“Act as a {role}. {task}. Consider {constraints}.”

**Example:**
“Act as a high-school physics teacher. Explain terminal velocity using an everyday analogy in under 120 words.”

---

## Audience Persona Pattern

**What it is:** Specify who the output is for to tune complexity and framing.
**When to use:** Adjusting reading level, tone, and examples for a target audience.

**Prompt template:**
“Write for {audience}. {task}. Keep reading level around {grade} and include {style cues}.”

**Example:**
“Write for first-year MBA students: compare A/B testing vs. causal inference in ~150 words, 8th-grade reading level, with a simple marketing example.”

---

## Flipped Interaction Pattern

**What it is:** Have the model interview you (or ask clarifying questions) before answering.
**When to use:** Problem is ambiguous; you want better scoping.

**Prompt template:**
“You are a consultant. Ask up to 5 clarifying questions. After I answer, propose a solution.”

**Example:**
“You’re a product strategist. Ask 4 questions about our new study-planner app. Then recommend a 2-week launch plan.”

---

## Game Play Pattern

**What it is:** Turn tasks into game mechanics (levels, rules, scoring) to increase engagement.
**When to use:** Practice, tutoring, onboarding.

**Prompt template:**
“Create a 3-level challenge on {topic}. Each level: 1 scenario + 3 choices. Track score and give hints.”

**Example:**
“Gamify SQL joins practice: 3 levels, each with a short dataset scenario and multiple choice. Explain answers.”

---

## Template Pattern

**What it is:** Provide a structured form the model must fill.
**When to use:** Consistent outputs (reports, emails, briefs).

**Prompt template:**
“Use this template: {fields}. Populate it for {task}.”

**Example:**
“Use this template—Problem, Evidence, Options, Recommendation—to draft a 1-page memo on reducing cart abandonment.”

---

## Meta Language Creation Pattern

**What it is:** Define lightweight command words/DSL to control the model.
**When to use:** Reusable workflows; tool-like behavior.

**Prompt template:**
“Create a mini command set for {domain}. Define 5–8 commands with syntax and examples.”

**Example:**
“Design a micro-language for lesson planning with commands: /obj, /warmup, /demo, /practice, /exit. Show an Algebra I lesson using it.”

---

## Recipe Pattern

**What it is:** Stepwise procedure with ingredients (inputs), tools, and steps.
**When to use:** Repeatable processes (analyses, creative pipelines).

**Prompt template:**
“Create a recipe for {goal} including: Inputs, Tools, Steps (numbered), Quality checks, Variations.”

**Example:**
“Recipe for a 600-word thought-leadership post: inputs (audience, thesis), steps (outline→draft→revise), QC checklist (originality, evidence, CTA).”

---

## Alternative Approaches Pattern

**What it is:** Generate multiple distinct methods with trade-offs.
**When to use:** Exploring solution space before committing.

**Prompt template:**
“Provide 3 approaches to {problem}. For each: steps, pros, cons, effort, risk. End with a comparison table.”

**Example:**
“Three ways to implement search (keyword, semantic, hybrid) with pros/cons and an adoption recommendation for a 3-person team.”

---

## Ask for Input Pattern

**What it is:** The model lists what it needs, then waits for your data.
**When to use:** Data-dependent tasks.

**Prompt template:**
“List the required inputs to do {task}. Wait for me to paste them. Then proceed.”

**Example:**
“List what you need to write a grant abstract (problem, beneficiaries, prior work, metrics). After I reply, draft a 250-word abstract.”

---

## Outline Expansion Pattern

**What it is:** Start from bullet outline → expand iteratively.
**When to use:** Long-form writing, lectures, reports.

**Prompt template:**
“Here’s an outline: {bullets}. Expand to {length}, include {sections}, keep {tone}. Preserve headings.”

**Example:**
“Expand this outline on vector databases to a 1,000-word explainer with sections: Why Vectors, How It Works, Use Cases, Pitfalls.”

---

## Menu Actions Pattern

**What it is:** Offer a short menu of next actions; proceed based on choice.
**When to use:** Interactive workflows with branching.

**Prompt template:**
“Choose an action: (A) Summarize, (B) Critique, (C) Rewrite for {audience}, (D) Create slides. Wait for my letter, then execute.”

**Example:**
“Given this draft blog, offer a menu. If I pick C=Rewrite for clinicians, produce a 300-word version with plain-language definitions.”

---

## Fact Check List Pattern

**What it is:** Require verification steps and citations before final output.
**When to use:** Accuracy-sensitive content.

**Prompt template:**
“Before answering, produce a fact-check checklist for {topic}. Verify each item with a citation placeholder [C1…]. Then give the answer with the checklist appended.”

**Example:**
“Explain ‘RLHF’ with a 5-item fact-check list (method steps, known limits, timeline). Provide sources placeholders to fill later.”

---

## Tail Generation Pattern

**What it is:** Generate many short variations (“the long tail”) from a core.
**When to use:** Headlines, ad copy, prompts, examples.

**Prompt template:**
“Given the core message {text}, generate 25 variants under {constraint} (≤60 chars, no hashtags). Group by tone.”

**Example:**
“Produce 20 email subject lines for a data-viz workshop; categories: playful, expert, urgent.”

---

## Semantic Filter Pattern

**What it is:** Specify inclusion/exclusion rules by meaning, not keywords.
**When to use:** Curating outputs, trimming noise.

**Prompt template:**
“From {items}, keep only entries that meet ALL: {positive semantics}. Exclude ANY that match: {negative semantics}. Return as JSON.”

**Example:**
“Filter research papers to those with real-world RAG evaluations (human or live metrics). Exclude purely theoretical or image-only work.”

---

## Helpful Assistant Pattern

**What it is:** Codify assistant behaviors: clarify, structure, cite, and note limits.
**When to use:** General task help with consistent quality.

**Prompt template:**
“You are a helpful assistant. If ambiguous, ask 2 targeted questions. Otherwise: structure with headings, give numbered steps, and note assumptions/limits.”

**Example:**
“Plan a 90-minute workshop on prompt engineering for non-technical staff. If details are missing, ask 2 questions; else provide agenda, materials, and exercises.”

---

## Prompt Engineering (Bridge Pattern)

**What it is:** Combine goal → constraints → examples → evaluation into one prompt.
**When to use:** Complex tasks requiring consistent quality.

**Prompt template:**
“Goal: {goal}. Constraints: {list}. Examples: {few-shot}. Evaluation: {rubric}. Task: {do X}. Output format: {schema}.”

**Example:**
“Goal: draft a 1-page policy brief. Constraints: ≤400 words, neutral tone, cite 2 sources. Examples: [short samples]. Evaluation: clarity, evidence, actionability. Output: Title, Problem, Evidence, Options, Recommendation.”

---

## Real-World Implementations (Pattern Stitching)

**What it is:** Combine multiple patterns into an end-to-end workflow.
**When to use:** Building repeatable pipelines.

**Example stitch:**

1. **Ask for Input** (collect product specs) →
2. **Template** (PRD structure) →
3. **Fact Check List** (constraints & regs) →
4. **Alternative Approaches** (solution paths) →
5. **Menu Actions** (choose ‘Create slides’) →
6. **Tail Generation** (multiple headlines for the deck).

