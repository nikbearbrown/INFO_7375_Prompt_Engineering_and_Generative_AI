# Teach a Prompt Pattern: The Template Pattern

## Abstract

The **Template Pattern** is a structural prompt engineering technique used to enforce a specific output format on a Large Language Model (LLM). Unlike open-ended prompts that allow for "narrative drift," the Template Pattern provides a predefined skeleton (using placeholders or headers) that the AI must populate. This ensures consistency, reduces hallucinations, and makes the output immediately compatible with professional workflows or data processing.

## Use Case: AI Image Generation Architecture

In the world of AI art (Midjourney, DALL-E, etc.), the order and presence of descriptive tags—such as lighting, camera angle, and medium—drastically change the result. A **Template Pattern** is used here to create a "Master Prompt Recipe." This ensures that every generated image has a defined style and technical depth, preventing the AI from defaulting to generic, flat compositions.

---

## Instructions

### Part 1: Comprehensive Exploration of the Chosen Prompt Pattern

#### Definition and Core Concepts

* **Definition:** Clearly define the Template Pattern as a structural "form-filling" approach.
* **Core Concepts:** * **Placeholders:** Using brackets like `[SUBJECT]` or `<SETTING>` to signal where data goes.
* **Structural Anchors:** Using headers or bullet points to force the AI to categorize its thoughts.



#### Purpose of the Pattern

* Explain how it eliminates "AI fluff" and keeps the model focused on specific variables.
* Discuss how it improves user interaction by making the output "scannable."

#### Significance in Real-World Applications

* **Example:** Technical documentation or medical summaries where missing a single field (like "Dosage" or "Safety Warning") is not an option.

---

### Part 2: Demonstrating the Prompt Pattern Through Examples

#### Scenario Description: The "Master Art Director"

* **Scenario:** You are building a tool for a marketing agency that needs 50 consistent product photos of different fruits but in the exact same "Cyberpunk" aesthetic.

#### Prompt Creation and Application

* **Prompt A (The Unstructured Request):** "Give me a cool picture of a neon apple in a futuristic style."
* **Prompt B (The Template Pattern):** "Act as a Prompt Engineer. Use this template for every fruit I name: **Subject:** [Fruit], **Style:** Cyberpunk/Neon, **Lighting:** Volumetric Purple, **Lens:** Macro 100mm."

#### Analysis of Model Responses

* Compare how Prompt A produces random results, while Prompt B allows for a "batch" of images that look like they belong to the same collection.

---

### Part 3: Presentation of the Chosen Prompt Pattern in Two Forms

#### Format 1: The Infographic (Visual)

* Create a visual flow-chart showing a "Blank Template" being filled by the AI to produce a "Structured Result."

#### Format 2: The Live Demo (Interactive)

* A "Screen-share" style video or a series of screenshots showing the "before and after" of using a template for a complex task like coding or lesson planning.

---

### Part 4: Quizzes and Exercises

#### Quiz

1. **Multiple Choice:** Which character is commonly used as a placeholder in a Template Pattern? (A) `[ ]`, (B) `! !`, (C) `? ?`.
2. **True/False:** The Template Pattern increases the AI's creative freedom to change the output format.
3. **Short Answer:** Why would a data scientist prefer a Template Pattern over a Persona Pattern?

#### Exercise: The Travel Itinerary

* **Scenario:** You are a travel agent.
* **Task:** Create a 3-field template (Destination, Daily Activity, Budget) and apply it to a "3-day trip to Tokyo." Analyze if the AI stayed within the lines or started writing long paragraphs.

---

## Grading Criteria

* **Exploration (40%):** Does the student understand that templates are about *structure*?
* **Creativity (30%):** How well did they visualize the "skeleton" of the prompt?
* **Effectiveness (30%):** Is the provided template actually reusable for others?
