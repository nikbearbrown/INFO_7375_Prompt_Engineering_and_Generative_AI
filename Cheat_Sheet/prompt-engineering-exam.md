# Prompt Engineering and AI Practice Exam (100 Points)

## Instructions
- Each question is worth 5 points
- Select all correct answers for each question
- There may be multiple correct answers per question
- A detailed answer key is provided at the end of the exam

## Section 1: Large Language Models and Fundamentals (35 points)

### Question 1
Which components are essential to modern Large Language Models (LLMs)?
- [ ] A) Recurrent neural connections
- [x] B) Transformer architecture with self-attention
- [x] C) Tokenization of input text
- [x] D) Positional encodings
- [ ] E) Convolutional layers for text processing

### Question 2
What factors affect the randomness in LLM outputs?
- [x] A) Temperature setting in the sampling procedure
- [x] B) Top-p (nucleus) sampling parameters
- [ ] C) The length of the prompt exclusively
- [x] D) Top-k sampling limits
- [ ] E) The programming language used to implement the model

### Question 3
Which of the following are correct statements about LLM capabilities and limitations?
- [x] A) LLMs can translate text between multiple languages
- [ ] B) LLMs inherently understand the factual accuracy of their outputs
- [x] C) LLMs can summarize long documents
- [ ] D) LLMs have perfect recall of their training data
- [x] E) LLMs can adapt to tasks not explicitly seen during training

### Question 4
Which techniques can help improve factual accuracy in LLM outputs?
- [x] A) Retrieval-Augmented Generation (RAG)
- [x] B) Grounding responses in cited knowledge bases
- [ ] C) Increasing temperature to generate more creative responses
- [x] D) Providing more context in the prompt
- [ ] E) Using only greedy decoding (temperature = 0)

### Question 5
What are valid approaches for evaluating LLM performance?
- [x] A) Human evaluation of output quality
- [x] B) Benchmark tasks like MMLU and HellaSwag
- [ ] C) Measuring only the perplexity on the training dataset
- [x] D) Comparing against gold standard responses
- [ ] E) Simply counting the number of parameters in the model

### Question 6
Which statements about model scaling laws are correct?
- [x] A) Performance generally improves with increased model size
- [x] B) Performance can improve with increased training data
- [ ] C) Scaling models always yields proportional improvements
- [x] D) Scaling compute resources can improve model capabilities
- [ ] E) There are no diminishing returns when scaling model parameters

### Question 7
Which approaches help mitigate hallucinations in LLMs?
- [x] A) Grounding the model with external knowledge sources
- [ ] B) Increasing the temperature setting
- [x] C) Using system prompts that emphasize factuality
- [x] D) Fine-tuning on datasets designed to reduce confabulation
- [ ] E) Generating longer outputs to include more details

## Section 2: Prompt Engineering Techniques (35 points)

### Question 8
Which principles are important for crafting effective prompts?
- [x] A) Providing clear and specific instructions
- [ ] B) Always using the shortest possible prompts
- [x] C) Breaking complex tasks into simpler steps
- [x] D) Including relevant context and constraints
- [ ] E) Avoiding examples within the prompt

### Question 9
What are effective prompt patterns for improving LLM responses?
- [x] A) Chain-of-thought prompting to encourage reasoning
- [x] B) Persona-based prompting to establish a specific role
- [x] C) Few-shot prompting with examples
- [ ] D) Adding random information to increase diversity
- [ ] E) Intentionally misspelling words to test model robustness

### Question 10
Which are valid strategies for prompt refinement?
- [x] A) Iteratively testing and improving prompts based on results
- [x] B) Analyzing error patterns in responses
- [ ] C) Always making prompts longer with each iteration
- [x] D) Adjusting the level of specificity based on output quality
- [ ] E) Using only exact technical terminology in all prompts

### Question 11
In the context of few-shot prompting, which statements are correct?
- [x] A) Few-shot prompting includes examples of desired input-output pairs
- [ ] B) Few-shot prompting requires modifying the model's weights
- [x] C) The quality of examples can significantly impact performance
- [x] D) Format consistency between examples improves results
- [ ] E) Few-shot prompting always outperforms zero-shot prompting

### Question 12
Which techniques are effective for improving factuality in prompted responses?
- [x] A) Instructing the model to cite sources
- [x] B) Asking the model to reason step-by-step
- [ ] C) Using vague instructions to allow flexibility
- [x] D) Requesting the model to evaluate its confidence
- [ ] E) Always prompting for the shortest possible answer

### Question 13
When designing system prompts, which approaches are considered best practices?
- [x] A) Defining clear roles and constraints
- [x] B) Establishing the tone and style of responses
- [ ] C) Making them as lengthy as possible with maximum detail
- [x] D) Including guidance on how to handle edge cases
- [ ] E) Changing system prompts for every user interaction

### Question 14
Which statements about ReAct (Reasoning + Acting) prompting are correct?
- [x] A) ReAct combines reasoning with taking actions
- [x] B) ReAct can improve problem-solving capabilities
- [x] C) ReAct typically involves describing steps before deciding on actions
- [ ] D) ReAct is only useful for mathematical problems
- [ ] E) ReAct requires custom model architectures

## Section 3: AI Agents and Fine-Tuning (30 points)

### Question 15
Which components are typically part of AI agent architectures?
- [x] A) Memory systems for tracking conversation history
- [x] B) Planning capabilities for breaking down complex tasks
- [x] C) Tool use capabilities for interacting with external systems
- [ ] D) Ability to directly modify its own code
- [ ] E) Unlimited context length by default

### Question 16
What are valid approaches for implementing AI agents?
- [x] A) Creating specialized agents with different areas of expertise
- [x] B) Implementing a ReAct pattern for reasoning and action
- [x] C) Using tools like LangChain or AutoGPT frameworks
- [ ] D) Relying exclusively on model size rather than architecture
- [ ] E) Programming all possible responses manually

### Question 17
Which statements about fine-tuning LLMs are correct?
- [x] A) Fine-tuning can adapt models to specific domains or tasks
- [ ] B) Fine-tuning always requires modifying all model parameters
- [x] C) The quality of the fine-tuning dataset significantly impacts results
- [x] D) Parameter-efficient fine-tuning methods can reduce computational requirements
- [ ] E) Fine-tuning permanently improves the model for all tasks

### Question 18
What are appropriate use cases for fine-tuning rather than prompt engineering?
- [x] A) Adapting the model to specialized terminology in a specific field
- [x] B) Teaching the model to follow a consistent output format
- [ ] C) Basic question-answering that's well-covered in pre-training
- [x] D) Aligning the model with specific value systems or guidelines
- [ ] E) All NLP tasks regardless of complexity

### Question 19
Which approaches are effective for multi-agent systems?
- [x] A) Creating specialized agents with different roles
- [x] B) Implementing communication protocols between agents
- [ ] C) Always maximizing the number of agents regardless of task
- [x] D) Including a coordinator agent to manage workflow
- [ ] E) Ensuring all agents have identical capabilities

### Question 20
What are valid considerations when deploying fine-tuned models or agents into production?
- [x] A) Monitoring for performance degradation over time
- [x] B) Implementing safety guardrails and filtering
- [ ] C) Eliminating human oversight once deployed
- [x] D) Managing computational resources and latency requirements
- [ ] E) Using the highest possible temperature settings for creativity

---

# Answer Key with Detailed Explanations

## Section 1: Large Language Models and Fundamentals

### Question 1
**Correct answers: B, C, D**

- **B) Transformer architecture with self-attention** ✓
  - The transformer architecture with self-attention is fundamental to modern LLMs, enabling parallel processing and effective modeling of relationships between tokens.

- **C) Tokenization of input text** ✓
  - Tokenization is essential for converting raw text into tokens that can be processed by the model.

- **D) Positional encodings** ✓
  - Positional encodings are necessary because transformers process all tokens simultaneously and need information about token order.

- **A) Recurrent neural connections** ✗
  - Modern LLMs typically use transformer architectures that explicitly avoid recurrence, which was common in older models like LSTMs.

- **E) Convolutional layers for text processing** ✗
  - While some hybrid architectures exist, standard LLMs rely on self-attention rather than convolutional layers for text processing.

### Question 2
**Correct answers: A, B, D**

- **A) Temperature setting in the sampling procedure** ✓
  - Temperature controls the randomness in token selection; higher values increase randomness and creativity.

- **B) Top-p (nucleus) sampling parameters** ✓
  - Top-p sampling restricts token selection to the smallest set of tokens whose cumulative probability exceeds the threshold p.

- **D) Top-k sampling limits** ✓
  - Top-k sampling restricts token selection to the k most probable next tokens, affecting output variability.

- **C) The length of the prompt exclusively** ✗
  - While prompt length can affect context, it doesn't directly control randomness in outputs.

- **E) The programming language used to implement the model** ✗
  - The programming language is an implementation detail that doesn't affect the model's stochastic properties.

### Question 3
**Correct answers: A, C, E**

- **A) LLMs can translate text between multiple languages** ✓
  - Large enough LLMs demonstrate strong translation capabilities between multiple languages.

- **C) LLMs can summarize long documents** ✓
  - Summarization is a core capability of modern LLMs, though limited by context window size.

- **E) LLMs can adapt to tasks not explicitly seen during training** ✓
  - This emergent ability is known as in-context learning, allowing models to perform new tasks through prompting.

- **B) LLMs inherently understand the factual accuracy of their outputs** ✗
  - LLMs do not have inherent fact-checking capabilities and can generate plausible-sounding but incorrect information (hallucinations).

- **D) LLMs have perfect recall of their training data** ✗
  - LLMs compress training data into weights and don't have verbatim recall of all training examples.

### Question 4
**Correct answers: A, B, D**

- **A) Retrieval-Augmented Generation (RAG)** ✓
  - RAG enhances factual accuracy by retrieving relevant documents before generating responses.

- **B) Grounding responses in cited knowledge bases** ✓
  - Using knowledge bases for verification improves factual correctness.

- **D) Providing more context in the prompt** ✓
  - Additional relevant context helps the model generate more accurate responses.

- **C) Increasing temperature to generate more creative responses** ✗
  - Higher temperatures increase creativity but can reduce factual accuracy by introducing more randomness.

- **E) Using only greedy decoding (temperature = 0)** ✗
  - While this produces deterministic responses, it doesn't necessarily improve factual accuracy and can produce stilted text.

### Question 5
**Correct answers: A, B, D**

- **A) Human evaluation of output quality** ✓
  - Human evaluation remains the gold standard for assessing LLM performance, especially for subjective qualities.

- **B) Benchmark tasks like MMLU and HellaSwag** ✓
  - Standardized benchmarks provide consistent comparison points across different models.

- **D) Comparing against gold standard responses** ✓
  - Comparing model outputs to expert-created reference answers helps evaluate performance objectively.

- **C) Measuring only the perplexity on the training dataset** ✗
  - This would primarily measure memorization rather than generalization or useful capabilities.

- **E) Simply counting the number of parameters in the model** ✗
  - Parameter count is not a direct measure of performance, though there are correlations with capability.

### Question 6
**Correct answers: A, B, D**

- **A) Performance generally improves with increased model size** ✓
  - Research shows performance tends to improve with model size, following scaling laws.

- **B) Performance can improve with increased training data** ✓
  - More diverse, high-quality training data typically improves model performance.

- **D) Scaling compute resources can improve model capabilities** ✓
  - Increased compute enables larger models, more data, and longer training, all contributing to improved performance.

- **C) Scaling models always yields proportional improvements** ✗
  - Scaling laws show diminishing returns, not proportional improvements.

- **E) There are no diminishing returns when scaling model parameters** ✗
  - Research clearly demonstrates diminishing returns from scaling, though the inflection point varies by task.

### Question 7
**Correct answers: A, C, D**

- **A) Grounding the model with external knowledge sources** ✓
  - External knowledge provides factual anchoring that reduces hallucinations.

- **C) Using system prompts that emphasize factuality** ✓
  - Explicit instructions to prioritize factual accuracy can reduce hallucinations.

- **D) Fine-tuning on datasets designed to reduce confabulation** ✓
  - Specialized fine-tuning can teach models to acknowledge uncertainty rather than hallucinate.

- **B) Increasing the temperature setting** ✗
  - Higher temperatures typically increase, not decrease, the likelihood of hallucinations.

- **E) Generating longer outputs to include more details** ✗
  - Longer outputs often provide more opportunities for hallucinations to occur.

## Section 2: Prompt Engineering Techniques

### Question 8
**Correct answers: A, C, D**

- **A) Providing clear and specific instructions** ✓
  - Clear instructions help the model understand exactly what is expected.

- **C) Breaking complex tasks into simpler steps** ✓
  - Breaking down complex tasks improves performance through scaffolding.

- **D) Including relevant context and constraints** ✓
  - Context and constraints guide the model toward appropriate responses.

- **B) Always using the shortest possible prompts** ✗
  - While conciseness has value, the shortest prompts often lack necessary detail and context.

- **E) Avoiding examples within the prompt** ✗
  - Examples (few-shot prompting) often improve performance significantly.

### Question 9
**Correct answers: A, B, C**

- **A) Chain-of-thought prompting to encourage reasoning** ✓
  - Chain-of-thought prompting improves performance on reasoning tasks by encouraging step-by-step thinking.

- **B) Persona-based prompting to establish a specific role** ✓
  - Assigning a persona helps frame the model's responses in an appropriate style and knowledge domain.

- **C) Few-shot prompting with examples** ✓
  - Providing examples of desired input-output pairs significantly improves performance.

- **D) Adding random information to increase diversity** ✗
  - Random information can confuse the model and dilute the actual instructions.

- **E) Intentionally misspelling words to test model robustness** ✗
  - While models should handle typos, intentionally including them doesn't improve response quality.

### Question 10
**Correct answers: A, B, D**

- **A) Iteratively testing and improving prompts based on results** ✓
  - Iteration is key to prompt engineering, as feedback from results informs improvements.

- **B) Analyzing error patterns in responses** ✓
  - Identifying systematic errors helps target prompt refinements.

- **D) Adjusting the level of specificity based on output quality** ✓
  - Finding the right balance of specificity is important for optimal results.

- **C) Always making prompts longer with each iteration** ✗
  - Sometimes shorter, more focused prompts yield better results.

- **E) Using only exact technical terminology in all prompts** ✗
  - The appropriate language depends on the task and desired output style.

### Question 11
**Correct answers: A, C, D**

- **A) Few-shot prompting includes examples of desired input-output pairs** ✓
  - This is the defining characteristic of few-shot prompting.

- **C) The quality of examples can significantly impact performance** ✓
  - The choice of examples matters greatly for few-shot performance.

- **D) Format consistency between examples improves results** ✓
  - Consistent formatting helps the model recognize patterns in the examples.

- **B) Few-shot prompting requires modifying the model's weights** ✗
  - Few-shot prompting works without changing model weights, unlike fine-tuning.

- **E) Few-shot prompting always outperforms zero-shot prompting** ✗
  - While often true, this depends on the task and the quality of examples.

### Question 12
**Correct answers: A, B, D**

- **A) Instructing the model to cite sources** ✓
  - Requesting citations encourages the model to ground statements in verifiable information.

- **B) Asking the model to reason step-by-step** ✓
  - Step-by-step reasoning often improves factual accuracy by encouraging careful thinking.

- **D) Requesting the model to evaluate its confidence** ✓
  - Prompting for confidence assessment can help the model express uncertainty rather than hallucinate.

- **C) Using vague instructions to allow flexibility** ✗
  - Vague instructions typically reduce, not improve, factual accuracy.

- **E) Always prompting for the shortest possible answer** ✗
  - Brevity constraints can force the model to omit important nuances and qualifications.

### Question 13
**Correct answers: A, B, D**

- **A) Defining clear roles and constraints** ✓
  - Roles and constraints help guide the model's behavior appropriately.

- **B) Establishing the tone and style of responses** ✓
  - Setting expectations for tone and style helps ensure consistent, appropriate responses.

- **D) Including guidance on how to handle edge cases** ✓
  - Anticipating edge cases in system prompts improves robustness.

- **C) Making them as lengthy as possible with maximum detail** ✗
  - Excessively long system prompts can be counterproductive, diluting the most important instructions.

- **E) Changing system prompts for every user interaction** ✗
  - System prompts are designed to be persistent settings, with user prompts changing instead.

### Question 14
**Correct answers: A, B, C**

- **A) ReAct combines reasoning with taking actions** ✓
  - The name ReAct itself stands for "reasoning" and "acting" combined.

- **B) ReAct can improve problem-solving capabilities** ✓
  - The structured approach of ReAct enhances complex problem-solving.

- **C) ReAct typically involves describing steps before deciding on actions** ✓
  - The reasoning step typically precedes and informs the action step.

- **D) ReAct is only useful for mathematical problems** ✗
  - ReAct is valuable across many domains, including planning, research, and tool use.

- **E) ReAct requires custom model architectures** ✗
  - ReAct is a prompting technique that works with standard LLMs.

## Section 3: AI Agents and Fine-Tuning

### Question 15
**Correct answers: A, B, C**

- **A) Memory systems for tracking conversation history** ✓
  - Memory is essential for maintaining context and coherence in agent interactions.

- **B) Planning capabilities for breaking down complex tasks** ✓
  - Planning helps agents handle multi-step problems effectively.

- **C) Tool use capabilities for interacting with external systems** ✓
  - Tool use extends agent capabilities beyond pure language generation.

- **D) Ability to directly modify its own code** ✗
  - While agents can suggest code modifications, they typically don't self-modify.

- **E) Unlimited context length by default** ✗
  - Agents are still limited by the context windows of their underlying models.

### Question 16
**Correct answers: A, B, C**

- **A) Creating specialized agents with different areas of expertise** ✓
  - Specialization allows for more effective division of complex tasks.

- **B) Implementing a ReAct pattern for reasoning and action** ✓
  - ReAct provides an effective framework for agent decision-making.

- **C) Using tools like LangChain or AutoGPT frameworks** ✓
  - These frameworks provide infrastructure for building and deploying agents.

- **D) Relying exclusively on model size rather than architecture** ✗
  - Architecture and design patterns are as important as the underlying model size.

- **E) Programming all possible responses manually** ✗
  - This defeats the purpose of using generative AI agents and isn't scalable.

### Question 17
**Correct answers: A, C, D**

- **A) Fine-tuning can adapt models to specific domains or tasks** ✓
  - This is the primary purpose of fine-tuning.

- **C) The quality of the fine-tuning dataset significantly impacts results** ✓
  - Dataset quality is often more important than quantity for fine-tuning.

- **D) Parameter-efficient fine-tuning methods can reduce computational requirements** ✓
  - Methods like LoRA and adapter tuning significantly reduce resource needs.

- **B) Fine-tuning always requires modifying all model parameters** ✗
  - Parameter-efficient methods modify only a small subset of parameters.

- **E) Fine-tuning permanently improves the model for all tasks** ✗
  - Fine-tuning often involves tradeoffs, improving performance on the target task while potentially degrading performance on others.

### Question 18
**Correct answers: A, B, D**

- **A) Adapting the model to specialized terminology in a specific field** ✓
  - Fine-tuning excels at teaching models domain-specific vocabulary and concepts.

- **B) Teaching the model to follow a consistent output format** ✓
  - Fine-tuning can effectively encode output format requirements.

- **D) Aligning the model with specific value systems or guidelines** ✓
  - Value alignment is effectively taught through fine-tuning on examples that demonstrate the desired values.

- **C) Basic question-answering that's well-covered in pre-training** ✗
  - Prompt engineering is typically sufficient for tasks already well-represented in pre-training.

- **E) All NLP tasks regardless of complexity** ✗
  - Many simple NLP tasks can be handled effectively with prompt engineering alone.

### Question 19
**Correct answers: A, B, D**

- **A) Creating specialized agents with different roles** ✓
  - Division of labor between specialized agents improves overall system performance.

- **B) Implementing communication protocols between agents** ✓
  - Explicit communication protocols help coordinate multi-agent systems.

- **D) Including a coordinator agent to manage workflow** ✓
  - Coordinator agents help organize the activities of specialized agents.

- **C) Always maximizing the number of agents regardless of task** ✗
  - More agents increase complexity and overhead, which isn't always beneficial.

- **E) Ensuring all agents have identical capabilities** ✗
  - Differentiated capabilities are often the point of multi-agent systems.

### Question 20
**Correct answers: A, B, D**

- **A) Monitoring for performance degradation over time** ✓
  - Monitoring helps detect concept drift and ensures continued performance.

- **B) Implementing safety guardrails and filtering** ✓
  - Safety measures are essential for responsible AI deployment.

- **D) Managing computational resources and latency requirements** ✓
  - Resource management is crucial for cost-effective and responsive deployment.

- **C) Eliminating human oversight once deployed** ✗
  - Ongoing human oversight remains important for most AI systems.

- **E) Using the highest possible temperature settings for creativity** ✗
  - Temperature should be calibrated to the specific use case, not maximized by default.