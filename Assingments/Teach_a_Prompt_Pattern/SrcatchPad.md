
# Prompt Architecture Notebook

**Instructor Example: Assignment Submission**

## Abstract

The **Template Pattern** is a structural prompt engineering technique that replaces open-ended "chatting" with a standardized "skeleton." By using placeholders—like `[Subject]` or `[Style]`—the user ensures the AI focuses on specific variables without losing consistency. This is the primary method used by professional Art Directors to maintain a unified "look" across hundreds of AI-generated assets.

---

## Part 1: Comprehensive Exploration

### Definition and Core Concepts

The Template Pattern is a "Fill-in-the-Blanks" approach to prompting.

* **Variable Placeholders:** Symbols like `[ ]` or `< >` that indicate where new data should be swapped in.
* **Structural Anchors:** Fixed words (e.g., "Cinematic photography," "Kodak Portra 400") that never change, ensuring every image in a set shares the same DNA.

### Purpose and Significance

In NLP, the Template Pattern prevents "narrative drift." Without a template, an AI might describe Dorothy as a 3D cartoon in one prompt and a realistic human in the next. With a template, the **Style** is anchored, and only the **Subject** changes.

---

## Part 2: Demonstration (The Oz Character Study)

We will start with a basic structure and "build up" to a professional-grade prompt.

### Level 1: The Foundational Template

**Template:** `[Subject], [Style], [Camera Angle]`

* **Dorothy:** `Young girl in blue gingham, 1930s technicolor film style, eye-level portrait.`
* **Tin Man:** `Metallic man made of tin, 1930s technicolor film style, eye-level portrait.`

### Level 2: The Modular Framework (Adding Environment & Light)

**Template:** `[Subject] in [Environment], [Style], [Lighting], [Camera Angle]`

* **Scarecrow:** `Burlap scarecrow in a Kansas wheat field, vintage oil painting, golden hour sun, wide-angle shot.`
* **Cowardly Lion:** `Cowering lion in a dark spooky forest, vintage oil painting, dappled moonlight, wide-angle shot.`

### Level 3: The Master "Production" Template

This combines the narrative template with **Midjourney Parameters** for technical control.

**The Master Template:**

> `[Subject] in [Environment], [Style], [Lighting] --ar [Ratio] --stylize [Value] --v 7`

**The Final "Production" Result:**

> **Wicked Witch** in a stone castle turret, gothic digital art, eerie green glow **--ar 16:9 --stylize 500 --v 7**

---

## Part 3: Presentation Formats

### Format 1: The "Blueprint" Infographic

A visual side-by-side showing a "Messy Prompt" (Standard Chat) vs. a "Structured Prompt" (Template Pattern). It highlights how the template creates a predictable, professional result.

### Format 2: The Interactive Gallery

A series of four images (Dorothy, Scarecrow, Tin Man, Lion) all generated using the **exact same template**. This demonstrates to the class how the "Look and Feel" stays consistent while the character changes.

---

## Part 4: Quizzes and Exercises

### Quiz: Testing the Pattern

1. **Multiple Choice:** What happens to the "Structural Anchors" when you change subjects in a template?
* A) They are deleted.
* B) They stay exactly the same to ensure consistency.
* C) The AI ignores them.


2. **Scenario:** If you want all your Oz images to be widescreen, which **Parameter** should you anchor at the end of your template?
3. **True/False:** The Template Pattern is most useful when you need to generate a *series* of related items.

### Exercise: The "New Resident of Oz"

**The Scenario:** A new character, "The Flying Monkey General," has arrived in Oz.
**The Task:** Using the **Master Template** from Part 2, fill in the variables to ensure he looks like he belongs in the same movie as our previous characters.

> `[Flying Monkey General] in [Location], [Style], [Lighting] --ar 16:9`

---

# Glossary
---

## Glossary_01: {Subject} (The Heroes of Oz)

*These represent the core focus of your image. They fill the first slot of your template.*

| Variable | Description |
| --- | --- |
| **Dorothy Gale** | Young farm girl, blue gingham dress, braided hair, holding Toto. |
| **The Scarecrow** | Tall, lanky, stuffed with straw, burlap face, patched clothing. |
| **The Tin Man** | Riveted silver metal body, funnel hat, holding an oil can or axe. |
| **The Cowardly Lion** | Large bipedal lion, thick mane, wearing a "Courage" medal. |
| **The Wicked Witch** | Green skin, pointed black hat, long flowing black robes, broomstick. |

---

## Glossary_02: [Style] (The Artistic DNA)

*These define the "look" of the entire series. When you swap these, the whole world changes.*

| Variable | Visual Aesthetic |
| --- | --- |
| **1939 Technicolor** | High saturation, vibrant reds/yellows, cinematic grain, soft glow. |
| **Whimsical Watercolor** | Soft edges, paper texture, pastel bleeding, hand-drawn ink lines. |
| **Cyberpunk Neon** | Dark shadows, glowing pink/green lights, futuristic mechanical parts. |
| **Gothic Horror** | High contrast, desaturated colors, sharp shadows, eerie atmosphere. |
| **Studio Ghibli** | Clean lines, lush painted backgrounds, soft facial features, hand-painted feel. |

---

## Glossary_03: [Views] (Perspective & Framing)

*Formerly "Camera Angles," these define how the viewer sees the character.*

| Variable | Emotional Impact |
| --- | --- |
| **Heroic Low-View** | Looking up at the subject; makes them appear powerful and tall. |
| **Vulnerable High-View** | Looking down at the subject; makes them appear small or in danger. |
| **Close-Up Portrait** | Focuses on the face; emphasizes emotional expression and texture. |
| **Wide-Angle Landscape** | Shows the character and their environment; great for the Yellow Brick Road. |
| **Bird's-Eye View** | Looking straight down; useful for seeing the pattern of the Poppy Fields. |

[Image diagram showing camera view types: low angle, high angle, and close up]

---

## Class Live Demo: "The Slot Machine"

Show the students how the **Template Pattern** acts like a slot machine. You pull a lever and swap one glossary term for another:

**Prompt Structure:**
`{Subject} in the Emerald City, [Style], [Views]`

* **Combo A:** `{Dorothy} in the Emerald City, [1939 Technicolor], [Heroic Low-View]`
* **Combo B:** `{The Wicked Witch} in the Emerald City, [Cyberpunk Neon], [Vulnerable High-View]`
