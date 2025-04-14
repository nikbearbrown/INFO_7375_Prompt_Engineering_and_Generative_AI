# Prompt Engineering and AI Practice Exam 3 (100 Points)

## Instructions
- Each question is worth 5 points
- Select all correct answers for each question
- There may be multiple correct answers per question
- A detailed answer key is provided at the end of the exam

## Section 1: Real-World Prompt Engineering Applications (35 points)

### Question 1
Which prompt engineering strategies are effective for code generation tasks?
- [x] A) Providing context about the programming language and environment
- [x] B) Breaking down complex coding tasks into simpler components
- [ ] C) Avoiding examples of syntax to promote creativity
- [x] D) Specifying error handling requirements
- [ ] E) Using natural language exclusively without code snippets

### Question 2
In the context of content creation, which prompt strategies yield the most effective results?
- [x] A) Specifying the target audience and tone
- [ ] B) Using the shortest possible prompts
- [x] C) Providing content structure and formatting requirements
- [x] D) Defining the purpose and key messaging
- [ ] E) Avoiding constraints on style or format

### Question 3
For tasks requiring quantitative reasoning, which prompt techniques improve accuracy?
- [x] A) Instructing the model to solve step-by-step
- [x] B) Explicitly asking for verification of intermediate calculations
- [ ] C) Encouraging intuitive reasoning without showing calculations
- [x] D) Requesting multiple solution approaches when appropriate
- [ ] E) Limiting numerical precision requirements

### Question 4
When using prompt templates in production applications, which practices are recommended?
- [x] A) Versioning prompt templates to track changes
- [x] B) Implementing A/B testing to compare template effectiveness
- [x] C) Creating modular templates with variable interpolation
- [ ] D) Hardcoding all prompt elements
- [ ] E) Avoiding iteration once deployed

### Question 5
For domain-specific applications, which prompt engineering approaches are most effective?
- [x] A) Incorporating domain-specific terminology
- [x] B) Including reference standards or guidelines
- [ ] C) Using exclusively general language to ensure flexibility
- [x] D) Specifying the level of expertise expected in responses
- [ ] E) Avoiding examples to prevent biasing the model

### Question 6
Which techniques help ensure ethical output from LLMs?
- [x] A) Including explicit guidelines about harmful content
- [x] B) Using system prompts that emphasize ethical constraints
- [ ] C) Avoiding any discussion of sensitive topics
- [x] D) Requesting consideration of diverse perspectives
- [ ] E) Using maximum temperature settings for creativity

### Question 7
For multilingual applications, which prompt engineering strategies are effective?
- [x] A) Specifying the target language explicitly
- [x] B) Providing examples in the desired language
- [ ] C) Always prompting in English regardless of target language
- [x] D) Including translation quality requirements
- [ ] E) Avoiding language-specific formatting instructions

## Section 2: Advanced AI Agent Design and Implementation (35 points)

### Question 8
Which approaches effectively address the hallucination problem in AI agents?
- [x] A) Implementing verification steps for factual claims
- [x] B) Using retrieval mechanisms to ground responses in reliable sources
- [ ] C) Maximizing response length to include all possible information
- [x] D) Instructing the agent to acknowledge uncertainty
- [ ] E) Increasing temperature settings for more creative responses

### Question 9
For autonomous planning in AI agents, which techniques are most effective?
- [x] A) Breaking complex tasks into subtasks with dependencies
- [x] B) Implementing backtracking when plans fail
- [ ] C) Always pursuing the shortest path to goal completion
- [x] D) Continuous evaluation of plan effectiveness
- [ ] E) Executing all steps simultaneously

### Question 10
Which design patterns improve the long-term memory capabilities of AI agents?
- [x] A) Hierarchical memory organization with summarization
- [x] B) Vector storage of key information for semantic retrieval
- [x] C) Mechanisms for identifying and storing important information
- [ ] D) Storing complete conversation logs without filtering
- [ ] E) Relying solely on the agent's parametric knowledge

### Question 11
What are effective approaches for tool selection and orchestration in AI agents?
- [x] A) Analyzing the task to determine required tools
- [x] B) Using metadata about tool capabilities and limitations
- [ ] C) Always using all available tools for completeness
- [x] D) Implementing feedback loops to evaluate tool effectiveness
- [ ] E) Preferring complex tools over simpler ones regardless of task

### Question 12
For collaborative multi-agent systems, which coordination strategies are effective?
- [x] A) Implementing hierarchical supervision with a manager agent
- [x] B) Using shared knowledge repositories accessible to all agents
- [ ] C) Minimizing inter-agent communication
- [x] D) Defining clear roles and responsibilities for each agent
- [ ] E) Assigning all tasks to every agent for redundancy

### Question 13
Which evaluation metrics are appropriate for measuring AI agent performance?
- [x] A) Task completion success rate
- [x] B) Resource efficiency (time, computation, API calls)
- [ ] C) Response length
- [x] D) User satisfaction and perceived helpfulness
- [ ] E) Number of tools used per task

### Question 14
What are effective approaches for handling uncertainty in AI agent systems?
- [x] A) Explicit uncertainty quantification in agent outputs
- [x] B) Gathering additional information when confidence is low
- [ ] C) Always providing a definitive answer regardless of confidence
- [x] D) Human escalation paths for high-uncertainty scenarios
- [ ] E) Favoring the most specific answer regardless of evidence

## Section 3: Advanced Model Customization and Deployment (30 points)

### Question 15
Which considerations are important when deciding between prompt engineering and fine-tuning?
- [x] A) Availability of high-quality training data
- [x] B) Required consistency across similar inputs
- [x] C) Development and maintenance resources
- [ ] D) Always preferring the more complex approach
- [ ] E) Using fine-tuning for all use cases regardless of scale

### Question 16
For enterprise LLM deployment, which security practices are recommended?
- [x] A) Implementing access controls and authentication
- [x] B) Data filtering and sanitization for both inputs and outputs
- [ ] C) Using only public model APIs
- [x] D) Monitoring for potential data exfiltration
- [ ] E) Allowing unlimited API call volumes

### Question 17
Which approaches are effective for continual improvement of deployed LLM applications?
- [x] A) Implementing user feedback collection mechanisms
- [x] B) Monitoring performance metrics for degradation
- [x] C) Regular evaluation against evolving benchmarks
- [ ] D) Freezing model and prompt configurations after initial success
- [ ] E) Focusing exclusively on increasing model size

### Question 18
What are appropriate techniques for optimizing latency in LLM applications?
- [x] A) Response caching for common queries
- [x] B) Model quantization to reduce computation requirements
- [ ] C) Always using the largest available model
- [x] D) Batch processing when real-time responses aren't required
- [ ] E) Maximizing context length for all requests

### Question 19
For customizing models to specific domains using RLHF, which approaches are effective?
- [x] A) Collecting domain-expert preferences for comparison data
- [x] B) Creating a reward model specific to domain performance criteria
- [ ] C) Using only general preference data from non-experts
- [x] D) Iterative refinement based on expert evaluation
- [ ] E) Training exclusively on automated metrics without human input

### Question 20
Which strategies effectively balance model capabilities and resource constraints?
- [x] A) Selecting model size based on task complexity requirements
- [x] B) Using smaller models for simpler tasks within a larger system
- [x] C) Implementing fallback mechanisms for complex edge cases
- [ ] D) Always maximizing parameter count regardless of application
- [ ] E) Avoiding prompt optimization to save development time

---

# Answer Key with Detailed Explanations

## Section 1: Real-World Prompt Engineering Applications

### Question 1
**Correct answers: A, B, D**

- **A) Providing context about the programming language and environment** ✓
  - Language-specific context helps the model generate code appropriate for the target environment.

- **B) Breaking down complex coding tasks into simpler components** ✓
  - Decomposing complex tasks improves accuracy and maintainability of generated code.

- **D) Specifying error handling requirements** ✓
  - Explicit requirements for error handling lead to more robust code generation.

- **C) Avoiding examples of syntax to promote creativity** ✗
  - Syntax examples help ensure correct code generation; creativity in coding is less important than correctness.

- **E) Using natural language exclusively without code snippets** ✗
  - Code snippets provide valuable context and demonstrate desired syntax and patterns.

### Question 2
**Correct answers: A, C, D**

- **A) Specifying the target audience and tone** ✓
  - Audience and tone guidance helps tailor content appropriately.

- **C) Providing content structure and formatting requirements** ✓
  - Structure guidance ensures content organization meets expectations.

- **D) Defining the purpose and key messaging** ✓
  - Clear purpose and messaging guidance helps focus content on objectives.

- **B) Using the shortest possible prompts** ✗
  - For content creation, comprehensive prompts typically yield better results than minimal ones.

- **E) Avoiding constraints on style or format** ✗
  - Appropriate constraints help ensure content meets specific needs.

### Question 3
**Correct answers: A, B, D**

- **A) Instructing the model to solve step-by-step** ✓
  - Step-by-step solving reduces calculation errors and improves reasoning.

- **B) Explicitly asking for verification of intermediate calculations** ✓
  - Verification steps catch computational errors before they affect final results.

- **D) Requesting multiple solution approaches when appropriate** ✓
  - Multiple approaches can provide verification through convergent results.

- **C) Encouraging intuitive reasoning without showing calculations** ✗
  - For quantitative tasks, showing calculations is important for verification.

- **E) Limiting numerical precision requirements** ✗
  - Appropriate precision is important for accurate quantitative results.

### Question 4
**Correct answers: A, B, C**

- **A) Versioning prompt templates to track changes** ✓
  - Versioning enables rollback and analysis of prompt performance over time.

- **B) Implementing A/B testing to compare template effectiveness** ✓
  - Empirical testing helps identify the most effective prompts.

- **C) Creating modular templates with variable interpolation** ✓
  - Modularity and variable interpolation enable flexible reuse and adaptation.

- **D) Hardcoding all prompt elements** ✗
  - Hardcoding reduces flexibility and maintainability.

- **E) Avoiding iteration once deployed** ✗
  - Continuous improvement of prompts is important for maintaining performance.

### Question 5
**Correct answers: A, B, D**

- **A) Incorporating domain-specific terminology** ✓
  - Domain terminology signals to the model which knowledge area to draw from.

- **B) Including reference standards or guidelines** ✓
  - Reference to standards ensures compliance with domain-specific requirements.

- **D) Specifying the level of expertise expected in responses** ✓
  - Expertise level guidance helps calibrate the technical depth of responses.

- **C) Using exclusively general language to ensure flexibility** ✗
  - Domain-specific language improves accuracy and relevance for specialized tasks.

- **E) Avoiding examples to prevent biasing the model** ✗
  - Domain-specific examples help guide the model toward appropriate responses.

### Question 6
**Correct answers: A, B, D**

- **A) Including explicit guidelines about harmful content** ✓
  - Clear ethical guidelines help prevent generation of harmful content.

- **B) Using system prompts that emphasize ethical constraints** ✓
  - System-level ethical guidance provides consistent constraints.

- **D) Requesting consideration of diverse perspectives** ✓
  - Considering diverse perspectives helps avoid biased or narrow viewpoints.

- **C) Avoiding any discussion of sensitive topics** ✗
  - Many sensitive topics can be discussed ethically with appropriate framing.

- **E) Using maximum temperature settings for creativity** ✗
  - High temperature settings may increase the risk of inappropriate outputs.

### Question 7
**Correct answers: A, B, D**

- **A) Specifying the target language explicitly** ✓
  - Explicit language specification ensures the model generates content in the desired language.

- **B) Providing examples in the desired language** ✓
  - Examples in the target language help guide style and vocabulary.

- **D) Including translation quality requirements** ✓
  - Quality requirements help ensure translation preserves meaning and nuance.

- **C) Always prompting in English regardless of target language** ✗
  - Prompting in the target language often improves quality, especially for non-English outputs.

- **E) Avoiding language-specific formatting instructions** ✗
  - Language-specific formatting (like date formats, quotation styles) is important for natural outputs.

## Section 2: Advanced AI Agent Design and Implementation

### Question 8
**Correct answers: A, B, D**

- **A) Implementing verification steps for factual claims** ✓
  - Verification processes help catch and correct hallucinations.

- **B) Using retrieval mechanisms to ground responses in reliable sources** ✓
  - Grounding in reliable sources reduces hallucinations by providing factual context.

- **D) Instructing the agent to acknowledge uncertainty** ✓
  - Acknowledging uncertainty prevents overconfident assertions when information is limited.

- **C) Maximizing response length to include all possible information** ✗
  - Longer responses often increase opportunities for hallucination.

- **E) Increasing temperature settings for more creative responses** ✗
  - Higher temperature typically increases hallucination risk.

### Question 9
**Correct answers: A, B, D**

- **A) Breaking complex tasks into subtasks with dependencies** ✓
  - Task decomposition enables more manageable planning and execution.

- **B) Implementing backtracking when plans fail** ✓
  - Backtracking and replanning are essential for handling unexpected situations.

- **D) Continuous evaluation of plan effectiveness** ✓
  - Ongoing evaluation allows adaptation to changing conditions.

- **C) Always pursuing the shortest path to goal completion** ✗
  - The shortest path may not be optimal for reliability, safety, or other important criteria.

- **E) Executing all steps simultaneously** ✗
  - Dependencies between steps often require sequential execution.

### Question 10
**Correct answers: A, B, C**

- **A) Hierarchical memory organization with summarization** ✓
  - Hierarchical organization helps manage and retrieve information at appropriate levels of detail.

- **B) Vector storage of key information for semantic retrieval** ✓
  - Vector-based storage enables retrieval based on semantic similarity rather than exact matching.

- **C) Mechanisms for identifying and storing important information** ✓
  - Importance filtering helps manage memory capacity by prioritizing key information.

- **D) Storing complete conversation logs without filtering** ✗
  - Unfiltered storage is inefficient and can lead to context dilution.

- **E) Relying solely on the agent's parametric knowledge** ✗
  - External memory augmentation is crucial for long-term knowledge retention.

### Question 11
**Correct answers: A, B, D**

- **A) Analyzing the task to determine required tools** ✓
  - Task analysis ensures appropriate tool selection.

- **B) Using metadata about tool capabilities and limitations** ✓
  - Tool metadata helps the agent make informed decisions about tool applicability.

- **D) Implementing feedback loops to evaluate tool effectiveness** ✓
  - Feedback on tool performance enables learning and adaptation.

- **C) Always using all available tools for completeness** ✗
  - Using unnecessary tools increases complexity and potential for errors.

- **E) Preferring complex tools over simpler ones regardless of task** ✗
  - Tool selection should match task requirements; simpler tools are often preferable when sufficient.

### Question 12
**Correct answers: A, B, D**

- **A) Implementing hierarchical supervision with a manager agent** ✓
  - Hierarchical coordination helps manage complex multi-agent systems.

- **B) Using shared knowledge repositories accessible to all agents** ✓
  - Shared knowledge reduces duplication and enables collaboration.

- **D) Defining clear roles and responsibilities for each agent** ✓
  - Clear roles prevent confusion and overlap in multi-agent systems.

- **C) Minimizing inter-agent communication** ✗
  - Effective coordination typically requires substantial communication.

- **E) Assigning all tasks to every agent for redundancy** ✗
  - Full redundancy is inefficient; specialization with targeted redundancy is generally more effective.

### Question 13
**Correct answers: A, B, D**

- **A) Task completion success rate** ✓
  - Success rate directly measures agent effectiveness at achieving its goals.

- **B) Resource efficiency (time, computation, API calls)** ✓
  - Efficiency measures are important for practical deployment considerations.

- **D) User satisfaction and perceived helpfulness** ✓
  - User-centric metrics capture the practical value of the agent.

- **C) Response length** ✗
  - Length alone is not a reliable indicator of quality or effectiveness.

- **E) Number of tools used per task** ✗
  - Tool count doesn't reliably indicate performance; optimal tool use depends on the specific task.

### Question 14
**Correct answers: A, B, D**

- **A) Explicit uncertainty quantification in agent outputs** ✓
  - Communicating uncertainty levels helps users interpret agent outputs appropriately.

- **B) Gathering additional information when confidence is low** ✓
  - Active information gathering helps resolve uncertainty when possible.

- **D) Human escalation paths for high-uncertainty scenarios** ✓
  - Human intervention for high-stakes uncertain situations improves reliability.

- **C) Always providing a definitive answer regardless of confidence** ✗
  - Forced definitive answers in uncertain situations lead to misinformation.

- **E) Favoring the most specific answer regardless of evidence** ✗
  - Specificity without sufficient evidence increases error risk.

## Section 3: Advanced Model Customization and Deployment

### Question 15
**Correct answers: A, B, C**

- **A) Availability of high-quality training data** ✓
  - Fine-tuning requires sufficient high-quality data; prompt engineering may be preferable with limited data.

- **B) Required consistency across similar inputs** ✓
  - Fine-tuning typically provides more consistent responses than prompting.

- **C) Development and maintenance resources** ✓
  - Resource constraints affect the feasibility of different customization approaches.

- **D) Always preferring the more complex approach** ✗
  - Complexity should be justified by performance improvements, not pursued for its own sake.

- **E) Using fine-tuning for all use cases regardless of scale** ✗
  - For many use cases, prompt engineering is more efficient and practical.

### Question 16
**Correct answers: A, B, D**

- **A) Implementing access controls and authentication** ✓
  - Access controls prevent unauthorized usage of enterprise LLM systems.

- **B) Data filtering and sanitization for both inputs and outputs** ✓
  - Filtering helps prevent data leakage and inappropriate content.

- **D) Monitoring for potential data exfiltration** ✓
  - Monitoring helps detect potential misuse or security breaches.

- **C) Using only public model APIs** ✗
  - For many enterprise applications, private deployments offer better security and data controls.

- **E) Allowing unlimited API call volumes** ✗
  - Rate limiting helps prevent abuse and resource exhaustion.

### Question 17
**Correct answers: A, B, C**

- **A) Implementing user feedback collection mechanisms** ✓
  - User feedback provides valuable signals for improvement opportunities.

- **B) Monitoring performance metrics for degradation** ✓
  - Monitoring helps detect issues such as concept drift or changing user needs.

- **C) Regular evaluation against evolving benchmarks** ✓
  - Benchmark evaluation ensures the application keeps pace with state-of-the-art capabilities.

- **D) Freezing model and prompt configurations after initial success** ✗
  - Continuous improvement is essential for maintaining performance over time.

- **E) Focusing exclusively on increasing model size** ✗
  - Model size is just one factor among many for improvement.

### Question 18
**Correct answers: A, B, D**

- **A) Response caching for common queries** ✓
  - Caching eliminates generation time for repeated queries.

- **B) Model quantization to reduce computation requirements** ✓
  - Quantization reduces computational load with minimal quality impact.

- **D) Batch processing when real-time responses aren't required** ✓
  - Batch processing improves throughput efficiency for appropriate use cases.

- **C) Always using the largest available model** ✗
  - Smaller models often provide sufficient quality with much lower latency.

- **E) Maximizing context length for all requests** ✗
  - Using only necessary context reduces computation time.

### Question 19
**Correct answers: A, B, D**

- **A) Collecting domain-expert preferences for comparison data** ✓
  - Expert preferences ensure the reward model reflects domain-specific quality criteria.

- **B) Creating a reward model specific to domain performance criteria** ✓
  - Domain-specific reward models capture the unique requirements of the field.

- **D) Iterative refinement based on expert evaluation** ✓
  - Iterative improvement with expert feedback is essential for optimizing domain alignment.

- **C) Using only general preference data from non-experts** ✗
  - Non-expert preferences may not capture important domain-specific considerations.

- **E) Training exclusively on automated metrics without human input** ✗
  - Human input is crucial for capturing subjective aspects of quality.

### Question 20
**Correct answers: A, B, C**

- **A) Selecting model size based on task complexity requirements** ✓
  - Matching model capabilities to task requirements optimizes resource usage.

- **B) Using smaller models for simpler tasks within a larger system** ✓
  - Tiered model deployment efficiently allocates resources according to needs.

- **C) Implementing fallback mechanisms for complex edge cases** ✓
  - Fallbacks provide graceful handling of cases beyond primary model capabilities.

- **D) Always maximizing parameter count regardless of application** ✗
  - Larger models aren't always better, especially considering deployment costs.

- **E) Avoiding prompt optimization to save development time** ✗
  - Prompt optimization often provides substantial performance improvements for minimal cost.