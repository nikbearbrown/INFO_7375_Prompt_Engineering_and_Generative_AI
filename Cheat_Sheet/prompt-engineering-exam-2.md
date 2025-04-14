# Prompt Engineering and AI Practice Exam 2 (100 Points)

## Instructions
- Each question is worth 5 points
- Select all correct answers for each question
- There may be multiple correct answers per question
- A detailed answer key is provided at the end of the exam

## Section 1: Advanced Prompt Engineering (35 points)

### Question 1
Which prompt patterns are effective for improving reasoning capabilities in LLMs?
- [x] A) Chain-of-thought prompting
- [ ] B) Always keeping prompts as concise as possible
- [x] C) Tree of thoughts approach for exploring multiple reasoning paths
- [x] D) Self-consistency sampling across multiple reasoning attempts
- [ ] E) Intentionally limiting context to force creative solutions

### Question 2
Which strategies effectively mitigate prompt injection attacks?
- [x] A) Implementing strict role-based instructions in system prompts
- [x] B) Filtering and sanitizing user inputs
- [ ] C) Always using the highest possible temperature settings
- [x] D) Using separate system and user message types
- [ ] E) Allowing unlimited input length from users

### Question 3
What are effective uses of few-shot prompting?
- [x] A) Teaching the model a specific format for responses
- [x] B) Providing examples of reasoning for complex tasks
- [ ] C) Including as many examples as possible regardless of quality
- [x] D) Using diverse examples that cover edge cases
- [ ] E) Always using randomly selected examples from your dataset

### Question 4
Which statements about persona-based prompting are correct?
- [x] A) It helps establish a consistent voice and perspective
- [x] B) It can improve performance on domain-specific tasks
- [ ] C) It completely eliminates the need for other prompt engineering techniques
- [x] D) It works best when the persona has expertise relevant to the task
- [ ] E) The most generic personas yield the best results

### Question 5
What are valid approaches for effective instruction design in prompts?
- [x] A) Breaking complex instructions into sequential steps
- [ ] B) Using ambiguous language to test model capabilities
- [x] C) Clearly indicating any output format requirements
- [x] D) Providing explicit success criteria
- [ ] E) Avoiding examples that might constrain creativity

### Question 6
Which are effective methods for improving the factual accuracy of LLM responses?
- [x] A) Asking the model to cite its sources
- [x] B) Using ReAct prompting to encourage reasoning before responding
- [ ] C) Setting temperature as high as possible
- [x] D) Instructing the model to acknowledge uncertainty
- [ ] E) Encouraging lengthy responses regardless of content

### Question 7
What are valid performance evaluation metrics for prompt engineering?
- [x] A) Success rate on specific tasks
- [x] B) Human evaluation of response quality
- [ ] C) Number of tokens in the response
- [x] D) Factual accuracy compared to ground truth
- [ ] E) Time taken to generate the prompt

## Section 2: LLM Architecture and Fine-Tuning (35 points)

### Question 8
Which statements about parameter-efficient fine-tuning (PEFT) methods are correct?
- [x] A) LoRA adds low-rank matrices to existing weights
- [x] B) Adapter layers add trainable modules while freezing original weights
- [ ] C) PEFT methods always match full fine-tuning performance
- [x] D) PEFT methods significantly reduce memory requirements
- [ ] E) PEFT can only be applied to small language models

### Question 9
What are appropriate scenarios for fine-tuning rather than prompting?
- [x] A) When consistent adherence to specific guidelines is required
- [x] B) When domain-specific terminology needs to be incorporated
- [ ] C) For basic classification tasks well-covered in pre-training
- [x] D) When custom knowledge that isn't in pre-training must be learned
- [ ] E) For any task regardless of data availability

### Question 10
Which statements about instruction fine-tuning are correct?
- [x] A) It teaches models to follow natural language instructions
- [x] B) It typically uses input-output pairs with explicit instructions
- [x] C) It improves zero-shot performance on unseen tasks
- [ ] D) It requires equal amounts of data for all possible instructions
- [ ] E) It eliminates the need for prompt engineering

### Question 11
What are important considerations when creating a fine-tuning dataset?
- [x] A) Data quality matters more than quantity
- [x] B) The dataset should be diverse and representative
- [ ] C) Using exclusively web-scraped data without cleaning
- [x] D) Ensuring consistent formatting across examples
- [ ] E) Maximizing data volume regardless of relevance

### Question 12
Which statements about Reinforcement Learning from Human Feedback (RLHF) are correct?
- [x] A) RLHF uses human preferences to optimize model responses
- [x] B) It typically involves training a reward model on human judgments
- [x] C) It can align models with human values and preferences
- [ ] D) It completely eliminates the need for other training methods
- [ ] E) It requires equal amounts of positive and negative examples

### Question 13
What are valid approaches for evaluating a fine-tuned model?
- [x] A) Testing on held-out validation data
- [x] B) Comparing to baseline (pre-fine-tuning) performance
- [ ] C) Evaluating only on the training data
- [x] D) Human evaluation of output quality
- [ ] E) Measuring only the perplexity on the training dataset

### Question 14
Which statements about the tokenization process in LLMs are correct?
- [x] A) Different tokenizers may split the same text differently
- [x] B) Rare words are often split into multiple tokens
- [ ] C) All languages are tokenized with equal efficiency
- [x] D) Tokenization affects the context window utilization
- [ ] E) The choice of tokenizer has no effect on model performance

## Section 3: AI Agents and Applications (30 points)

### Question 15
Which components are essential for building effective AI agents?
- [x] A) Tool-use capabilities for interacting with external systems
- [x] B) Planning modules for breaking tasks into steps
- [ ] C) Ability to modify their own underlying code
- [x] D) Memory systems for tracking context and history
- [ ] E) Complete autonomy without human oversight

### Question 16
What are appropriate applications of AI agents?
- [x] A) Research assistants that can search and synthesize information
- [x] B) Customer support agents handling routine inquiries
- [ ] C) Fully autonomous critical infrastructure management
- [x] D) Collaborative writing and editing assistants
- [ ] E) Replacing human expertise in high-stakes medical decisions

### Question 17
Which design patterns are effective for multi-agent systems?
- [x] A) Specialized agents with different areas of expertise
- [x] B) Coordinator agents that delegate tasks
- [ ] C) Maximum redundancy with all agents having identical capabilities
- [x] D) Defined communication protocols between agents
- [ ] E) Eliminating all constraints on agent operations

### Question 18
What are important considerations for tool-augmented LLMs and agents?
- [x] A) Clearly defined tool interfaces and documentation
- [x] B) Appropriate error handling for tool failures
- [x] C) Verification of tool outputs before taking further actions
- [ ] D) Maximizing the number of tools regardless of usefulness
- [ ] E) Allowing unrestricted tool access without safety considerations

### Question 19
Which statements about Retrieval-Augmented Generation (RAG) are correct?
- [x] A) RAG combines retrieval of relevant documents with generative responses
- [x] B) It improves factual accuracy by grounding responses in source material
- [ ] C) It completely eliminates hallucinations in all cases
- [x] D) Vector databases are commonly used for efficient retrieval
- [ ] E) RAG requires fine-tuning the model on retrieved documents

### Question 20
What are valid deployment considerations for LLM-based applications?
- [x] A) Latency requirements and computational resources
- [x] B) Monitoring systems for detecting performance degradation
- [ ] C) Eliminating human oversight once the system is deployed
- [x] D) Implementing feedback mechanisms for continuous improvement
- [ ] E) Maximizing model size regardless of performance needs

---

# Answer Key with Detailed Explanations

## Section 1: Advanced Prompt Engineering

### Question 1
**Correct answers: A, C, D**

- **A) Chain-of-thought prompting** ✓
  - Chain-of-thought prompting improves reasoning by encouraging step-by-step thinking, showing significant improvements on complex tasks.

- **C) Tree of thoughts approach for exploring multiple reasoning paths** ✓
  - Tree of thoughts extends chain-of-thought by exploring and evaluating multiple reasoning branches, particularly effective for complex problem-solving.

- **D) Self-consistency sampling across multiple reasoning attempts** ✓
  - Self-consistency improves performance by generating multiple reasoning paths and selecting the most consistent answer, reducing errors.

- **B) Always keeping prompts as concise as possible** ✗
  - While conciseness can be valuable, reasoning tasks often benefit from more detailed prompts that guide the thinking process.

- **E) Intentionally limiting context to force creative solutions** ✗
  - Limiting context typically harms reasoning performance by removing potentially relevant information.

### Question 2
**Correct answers: A, B, D**

- **A) Implementing strict role-based instructions in system prompts** ✓
  - Clear role instructions help the model resist prompts that try to change its behavior or purpose.

- **B) Filtering and sanitizing user inputs** ✓
  - Preprocessing user inputs to detect and neutralize injection attempts is an effective defense.

- **D) Using separate system and user message types** ✓
  - Separating system instructions from user inputs helps maintain boundaries and prevents confusion.

- **C) Always using the highest possible temperature settings** ✗
  - Higher temperature increases randomness, potentially making the model less predictable in following security guidelines.

- **E) Allowing unlimited input length from users** ✗
  - Long inputs provide more opportunities for complex injection attacks and should be reasonably limited.

### Question 3
**Correct answers: A, B, D**

- **A) Teaching the model a specific format for responses** ✓
  - Few-shot examples effectively demonstrate the desired output format.

- **B) Providing examples of reasoning for complex tasks** ✓
  - Examples of reasoning processes help the model understand how to approach complex problems.

- **D) Using diverse examples that cover edge cases** ✓
  - Diverse examples help the model generalize across the problem space.

- **C) Including as many examples as possible regardless of quality** ✗
  - Quality of examples is more important than quantity; poor examples can harm performance.

- **E) Always using randomly selected examples from your dataset** ✗
  - Carefully selected examples typically outperform random selection.

### Question 4
**Correct answers: A, B, D**

- **A) It helps establish a consistent voice and perspective** ✓
  - Personas provide consistent framing for how the model should respond.

- **B) It can improve performance on domain-specific tasks** ✓
  - Domain-specific personas (e.g., "as a physicist") can improve performance on specialized tasks.

- **D) It works best when the persona has expertise relevant to the task** ✓
  - Aligning persona expertise with the task improves response quality.

- **C) It completely eliminates the need for other prompt engineering techniques** ✗
  - Personas complement but don't replace other prompt engineering methods.

- **E) The most generic personas yield the best results** ✗
  - Task-specific personas typically outperform generic ones for specialized tasks.

### Question 5
**Correct answers: A, C, D**

- **A) Breaking complex instructions into sequential steps** ✓
  - Sequential steps make complex instructions easier to follow.

- **C) Clearly indicating any output format requirements** ✓
  - Explicit format requirements lead to more consistently formatted responses.

- **D) Providing explicit success criteria** ✓
  - Clear success criteria help the model understand what constitutes a good response.

- **B) Using ambiguous language to test model capabilities** ✗
  - Ambiguity typically reduces instruction effectiveness and leads to inconsistent results.

- **E) Avoiding examples that might constrain creativity** ✗
  - Examples help set expectations even for creative tasks, and creativity can be explicitly requested while still providing guidance.

### Question 6
**Correct answers: A, B, D**

- **A) Asking the model to cite its sources** ✓
  - Source citation encourages the model to ground responses in recoverable information.

- **B) Using ReAct prompting to encourage reasoning before responding** ✓
  - The reasoning step in ReAct helps the model think through facts more carefully.

- **D) Instructing the model to acknowledge uncertainty** ✓
  - Acknowledging uncertainty helps prevent overconfident assertions about uncertain facts.

- **C) Setting temperature as high as possible** ✗
  - Higher temperature increases randomness, typically reducing factual accuracy.

- **E) Encouraging lengthy responses regardless of content** ✗
  - Length without focus on accuracy often introduces more opportunities for errors.

### Question 7
**Correct answers: A, B, D**

- **A) Success rate on specific tasks** ✓
  - Task completion is a direct measure of prompt effectiveness.

- **B) Human evaluation of response quality** ✓
  - Human judgment remains the gold standard for evaluating many aspects of response quality.

- **D) Factual accuracy compared to ground truth** ✓
  - Comparing responses to verified facts is crucial for assessing factual reliability.

- **C) Number of tokens in the response** ✗
  - Response length is not inherently a measure of quality.

- **E) Time taken to generate the prompt** ✗
  - Prompt creation time doesn't directly measure the effectiveness of the resulting prompt.

## Section 2: LLM Architecture and Fine-Tuning

### Question 8
**Correct answers: A, B, D**

- **A) LoRA adds low-rank matrices to existing weights** ✓
  - LoRA (Low-Rank Adaptation) works by adding trainable low-rank matrices to frozen pre-trained weights.

- **B) Adapter layers add trainable modules while freezing original weights** ✓
  - Adapters insert small trainable modules between frozen layers of the original model.

- **D) PEFT methods significantly reduce memory requirements** ✓
  - By training only a small subset of parameters, PEFT drastically reduces memory usage.

- **C) PEFT methods always match full fine-tuning performance** ✗
  - While PEFT often approaches full fine-tuning performance, there can be a small gap in some tasks.

- **E) PEFT can only be applied to small language models** ✗
  - PEFT methods are especially valuable for large models where full fine-tuning is prohibitively expensive.

### Question 9
**Correct answers: A, B, D**

- **A) When consistent adherence to specific guidelines is required** ✓
  - Fine-tuning is effective for encoding consistent behavior patterns across diverse inputs.

- **B) When domain-specific terminology needs to be incorporated** ✓
  - Fine-tuning helps models learn specialized vocabulary and domain-specific knowledge.

- **D) When custom knowledge that isn't in pre-training must be learned** ✓
  - New knowledge not covered in pre-training data can be incorporated through fine-tuning.

- **C) For basic classification tasks well-covered in pre-training** ✗
  - Simple tasks that leverage common knowledge are often handled well with prompting alone.

- **E) For any task regardless of data availability** ✗
  - Fine-tuning requires sufficient high-quality data; with limited data, prompting may be more appropriate.

### Question 10
**Correct answers: A, B, C**

- **A) It teaches models to follow natural language instructions** ✓
  - Instruction fine-tuning specifically improves models' ability to follow diverse instructions.

- **B) It typically uses input-output pairs with explicit instructions** ✓
  - Training data consists of instructions paired with desired responses.

- **C) It improves zero-shot performance on unseen tasks** ✓
  - A key benefit is better generalization to instructions not seen during training.

- **D) It requires equal amounts of data for all possible instructions** ✗
  - Effective instruction tuning can be done with uneven distribution of instruction types.

- **E) It eliminates the need for prompt engineering** ✗
  - While it improves baseline instruction-following, prompt engineering still enhances performance.

### Question 11
**Correct answers: A, B, D**

- **A) Data quality matters more than quantity** ✓
  - High-quality examples typically yield better results than larger quantities of lower-quality data.

- **B) The dataset should be diverse and representative** ✓
  - Diverse data helps the model generalize to varied inputs in production.

- **D) Ensuring consistent formatting across examples** ✓
  - Consistent formatting helps the model learn patterns more effectively.

- **C) Using exclusively web-scraped data without cleaning** ✗
  - Raw web-scraped data often contains noise, inconsistencies, and problematic content.

- **E) Maximizing data volume regardless of relevance** ✗
  - Irrelevant data can dilute the training signal and reduce effectiveness.

### Question 12
**Correct answers: A, B, C**

- **A) RLHF uses human preferences to optimize model responses** ✓
  - Human preferences provide the reward signal that guides optimization.

- **B) It typically involves training a reward model on human judgments** ✓
  - The reward model translates human preferences into a signal that can guide RL.

- **C) It can align models with human values and preferences** ✓
  - RLHF effectively aligns model outputs with human values across various dimensions.

- **D) It completely eliminates the need for other training methods** ✗
  - RLHF complements rather than replaces supervised pre-training and fine-tuning.

- **E) It requires equal amounts of positive and negative examples** ✗
  - Effective reward modeling can be done with unbalanced preference data.

### Question 13
**Correct answers: A, B, D**

- **A) Testing on held-out validation data** ✓
  - Validation on unseen data helps measure generalization.

- **B) Comparing to baseline (pre-fine-tuning) performance** ✓
  - Measuring improvement over the base model quantifies the value of fine-tuning.

- **D) Human evaluation of output quality** ✓
  - Human judgment remains crucial for assessing subjective aspects of model outputs.

- **C) Evaluating only on the training data** ✗
  - This measures memorization rather than generalization.

- **E) Measuring only the perplexity on the training dataset** ✗
  - Training perplexity alone doesn't reflect real-world performance.

### Question 14
**Correct answers: A, B, D**

- **A) Different tokenizers may split the same text differently** ✓
  - Tokenization varies significantly between models and implementation choices.

- **B) Rare words are often split into multiple tokens** ✓
  - Uncommon words are typically broken into smaller subword units.

- **D) Tokenization affects the context window utilization** ✓
  - Different tokenization approaches use varying numbers of tokens for the same text.

- **C) All languages are tokenized with equal efficiency** ✗
  - Languages not well-represented in training data often tokenize less efficiently.

- **E) The choice of tokenizer has no effect on model performance** ✗
  - Tokenization significantly impacts how models process and understand text.

## Section 3: AI Agents and Applications

### Question 15
**Correct answers: A, B, D**

- **A) Tool-use capabilities for interacting with external systems** ✓
  - Tools extend agent capabilities beyond pure language generation.

- **B) Planning modules for breaking tasks into steps** ✓
  - Planning is essential for handling complex, multi-step tasks.

- **D) Memory systems for tracking context and history** ✓
  - Memory enables coherent interactions over time.

- **C) Ability to modify their own underlying code** ✗
  - Self-modification is not a standard capability of current AI agents.

- **E) Complete autonomy without human oversight** ✗
  - Human oversight remains important for most AI agent applications.

### Question 16
**Correct answers: A, B, D**

- **A) Research assistants that can search and synthesize information** ✓
  - Information gathering and synthesis are well-suited to current agent capabilities.

- **B) Customer support agents handling routine inquiries** ✓
  - Structured customer support with clear escalation paths is appropriate.

- **D) Collaborative writing and editing assistants** ✓
  - Writing assistance with human collaboration is a suitable application.

- **C) Fully autonomous critical infrastructure management** ✗
  - Critical infrastructure requires human oversight and established safeguards.

- **E) Replacing human expertise in high-stakes medical decisions** ✗
  - High-stakes medical decisions require human judgment, with AI as a support tool.

### Question 17
**Correct answers: A, B, D**

- **A) Specialized agents with different areas of expertise** ✓
  - Specialization allows each agent to excel in a specific domain.

- **B) Coordinator agents that delegate tasks** ✓
  - Coordination improves efficiency in multi-agent systems.

- **D) Defined communication protocols between agents** ✓
  - Clear protocols enable effective collaboration.

- **C) Maximum redundancy with all agents having identical capabilities** ✗
  - Redundancy without specialization is inefficient.

- **E) Eliminating all constraints on agent operations** ✗
  - Constraints provide necessary guardrails for appropriate operation.

### Question 18
**Correct answers: A, B, C**

- **A) Clearly defined tool interfaces and documentation** ✓
  - Well-documented interfaces help agents use tools effectively.

- **B) Appropriate error handling for tool failures** ✓
  - Robust error handling prevents cascading failures when tools don't work as expected.

- **C) Verification of tool outputs before taking further actions** ✓
  - Verifying outputs helps prevent propagation of errors.

- **D) Maximizing the number of tools regardless of usefulness** ✗
  - Tool quality and relevance matter more than quantity.

- **E) Allowing unrestricted tool access without safety considerations** ✗
  - Safety constraints on tool use are essential, especially for powerful tools.

### Question 19
**Correct answers: A, B, D**

- **A) RAG combines retrieval of relevant documents with generative responses** ✓
  - This describes the fundamental architecture of RAG systems.

- **B) It improves factual accuracy by grounding responses in source material** ✓
  - Grounding in retrieved content significantly enhances factual reliability.

- **D) Vector databases are commonly used for efficient retrieval** ✓
  - Vector databases enable semantic search crucial for effective retrieval.

- **C) It completely eliminates hallucinations in all cases** ✗
  - While RAG reduces hallucinations, it doesn't completely eliminate them.

- **E) RAG requires fine-tuning the model on retrieved documents** ✗
  - RAG operates through in-context learning without requiring model fine-tuning.

### Question 20
**Correct answers: A, B, D**

- **A) Latency requirements and computational resources** ✓
  - Understanding performance needs is essential for deployment planning.

- **B) Monitoring systems for detecting performance degradation** ✓
  - Continuous monitoring helps maintain quality over time.

- **D) Implementing feedback mechanisms for continuous improvement** ✓
  - User feedback loops enable ongoing enhancement.

- **C) Eliminating human oversight once the system is deployed** ✗
  - Human oversight remains important, especially for consequential applications.

- **E) Maximizing model size regardless of performance needs** ✗
  - Model size should be matched to requirements, with smaller models often sufficient for specific tasks.