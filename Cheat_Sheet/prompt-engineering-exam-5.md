# Prompt Engineering and AI Practice Exam 5 (100 Points)

## Instructions
- Each question is worth 5 points
- Select all correct answers for each question
- There may be multiple correct answers per question
- A detailed answer key is provided at the end of the exam

## Section 1: Advanced LLM Architectures and Techniques (35 points)

### Question 1
Which statements accurately describe recent advancements in prompt engineering techniques?
- [x] A) Tree of Thoughts enables exploration of multiple reasoning paths simultaneously
- [x] B) Automatic prompt optimization can use reinforcement learning to improve prompts
- [ ] C) Zero-shot prompting always outperforms few-shot approaches
- [x] D) Multimodal prompting allows combining text with other data types
- [ ] E) The effectiveness of prompt techniques is independent of model architecture

### Question 2
Which approaches effectively leverage retrieval-augmented generation (RAG) in production systems?
- [x] A) Implementing hybrid search combining keyword and semantic retrieval
- [x] B) Chunking documents appropriately based on content structure
- [ ] C) Always retrieving the maximum possible number of documents
- [x] D) Re-ranking retrieved documents based on relevance to the query
- [ ] E) Using only the model's parametric knowledge for factual questions

### Question 3
For agentic systems that require long-term planning, which techniques are most effective?
- [x] A) Hierarchical task decomposition with sub-goal prioritization
- [x] B) Implementing verification steps to check if goals were achieved
- [ ] C) Executing all sub-tasks in parallel regardless of dependencies
- [x] D) Maintaining a state representation that tracks progress and failures
- [ ] E) Avoiding replanning when initial plans encounter obstacles

### Question 4
Which approaches effectively combine the strengths of different LLM architectures in a single system?
- [x] A) Using smaller, specialized models for routine tasks and larger models for complex reasoning
- [x] B) Implementing model routing based on task classification
- [ ] C) Always defaulting to the largest available model
- [x] D) Creating ensembles that aggregate multiple model outputs for critical decisions
- [ ] E) Using identical prompts across all model types

### Question 5
For domain adaptation of LLMs, which techniques are most appropriate?
- [x] A) Domain-specific continued pre-training on relevant corpora
- [x] B) Parameter-efficient fine-tuning focused on domain knowledge
- [ ] C) Avoiding domain-specific terminology in prompts
- [x] D) Creating domain-specific knowledge retrieval systems
- [ ] E) Using only generic models for all specialized domains

### Question 6
Which statements accurately describe the relationship between model size and prompt engineering effectiveness?
- [x] A) Larger models typically require less explicit instruction than smaller models
- [x] B) Chain-of-thought reasoning yields more significant improvements in medium-sized models
- [ ] C) Prompt engineering is unnecessary for the largest models
- [x] D) Few-shot examples remain useful even for the largest models
- [ ] E) Smaller models always require more examples than larger models

### Question 7
Which techniques effectively address hallucination in modern LLMs?
- [x] A) Implementing factuality scoring systems for generated content
- [x] B) Combining multiple models with different knowledge cutoff dates
- [ ] C) Using maximum temperature settings for all generation tasks
- [x] D) Grounding generation in external, verified knowledge sources
- [ ] E) Avoiding all reference to uncertain knowledge areas

## Section 2: Specialized Applications and Evaluation (35 points)

### Question 8
For LLM applications in educational contexts, which prompt engineering approaches are most effective?
- [x] A) Adapting complexity based on educational level
- [x] B) Incorporating evidence-based pedagogical frameworks
- [ ] C) Providing identical explanations for all learner levels
- [x] D) Designing scaffolded prompts that guide learning progression
- [ ] E) Focusing exclusively on factual delivery without engagement

### Question 9
Which techniques are most effective for evaluating and improving LLM reasoning capabilities?
- [x] A) Using benchmark datasets specifically designed to test reasoning
- [x] B) Implementing trace-based evaluation that examines reasoning steps
- [ ] C) Focusing only on final answer accuracy without considering reasoning paths
- [x] D) Comparing model reasoning to expert-annotated reasoning chains
- [ ] E) Avoiding step-by-step reasoning to maximize efficiency

### Question 10
For developing LLM applications in legally sensitive contexts, which approaches are most appropriate?
- [x] A) Implementing clear disclaimers about the non-advisory nature of responses
- [x] B) Designing prompts that avoid making definitive legal judgments
- [ ] C) Allowing the model to provide specific legal advice without verification
- [x] D) Focusing on information provision rather than recommendation
- [ ] E) Encouraging definitive interpretations of complex legal matters

### Question 11
Which approaches efficiently balance computational costs and model performance?
- [x] A) Implementing intelligent caching for common queries
- [x] B) Using model distillation to create more efficient specialized models
- [ ] C) Always selecting the largest model for all tasks
- [x] D) Dynamically adjusting context length based on task requirements
- [ ] E) Maximizing prompt length regardless of task needs

### Question 12
For applications requiring source attribution and verification, which techniques are most effective?
- [x] A) Implementing automatic fact extraction and verification against trusted sources
- [x] B) Designing prompts that explicitly request citations and evidence
- [ ] C) Prioritizing confident answers over uncertain but cited responses
- [x] D) Using retrieval systems that maintain links to original documents
- [ ] E) Avoiding references to external sources to test model knowledge

### Question 13
Which human evaluation approaches most effectively assess LLM output quality?
- [x] A) Blind comparison between human and LLM outputs
- [x] B) Expert evaluation using domain-specific rubrics
- [ ] C) Focusing exclusively on grammatical correctness
- [x] D) Multi-dimensional evaluation across relevance, accuracy, and helpfulness
- [ ] E) Using only automated metrics without human judgment

### Question 14
For developing AI writing assistants, which prompt engineering strategies are most effective?
- [x] A) Adapting style and tone based on document type and audience
- [x] B) Incorporating user preferences and feedback over time
- [ ] C) Providing identical suggestions for all writing contexts
- [x] D) Maintaining document-level coherence through context awareness
- [ ] E) Prioritizing grammatical correctness over user intent

## Section 3: Emerging Trends and Enterprise Integration (30 points)

### Question 15
Which approaches effectively integrate LLMs with traditional enterprise systems?
- [x] A) Implementing middleware that handles data transformation between systems
- [x] B) Designing clear APIs with appropriate input validation
- [ ] C) Replacing all existing systems with LLM-based alternatives
- [x] D) Ensuring appropriate authentication and authorization mechanisms
- [ ] E) Allowing unrestricted data flow between systems

### Question 16
For maintaining LLM systems in production, which practices are most effective?
- [x] A) Implementing monitoring for performance drift over time
- [x] B) Collecting user feedback to identify improvement opportunities
- [ ] C) Avoiding updates to deployed systems
- [x] D) Maintaining comprehensive documentation of system design decisions
- [ ] E) Removing human oversight once systems are stabilized

### Question 17
Which strategies effectively balance innovation and responsible AI deployment?
- [x] A) Implementing staged deployment with increasing autonomy levels
- [x] B) Creating clear escalation paths for edge cases
- [ ] C) Prioritizing rapid deployment over thorough testing
- [x] D) Designing systems with appropriate capability limitations
- [ ] E) Granting systems maximum capabilities regardless of use case

### Question 18
For agentic systems in enterprise environments, which security considerations are most important?
- [x] A) Implementing least-privilege access to enterprise systems
- [x] B) Designing comprehensive audit trails for agent actions
- [ ] C) Allowing unrestricted tool access to maximize capabilities
- [x] D) Creating sandboxed environments for testing before deployment
- [ ] E) Minimizing monitoring to improve operational efficiency

### Question 19
Which approaches most effectively combine human expertise with LLM capabilities?
- [x] A) Creating human-in-the-loop systems for critical decisions
- [x] B) Designing clear handoff protocols between automated and human processes
- [ ] C) Minimizing human involvement to maximize automation
- [x] D) Implementing feedback mechanisms that improve system performance over time
- [ ] E) Replacing human experts entirely with autonomous systems

### Question 20
For implementing LLM-based innovation in traditional industries, which approaches are most effective?
- [x] A) Starting with focused applications that demonstrate clear ROI
- [x] B) Designing systems that augment rather than replace human expertise
- [ ] C) Deploying comprehensive solutions that transform entire business processes at once
- [x] D) Implementing robust evaluation frameworks to measure business impact
- [ ] E) Prioritizing technological sophistication over business alignment

---

# Answer Key with Detailed Explanations

## Section 1: Advanced LLM Architectures and Techniques

### Question 1
**Correct answers: A, B, D**

- **A) Tree of Thoughts enables exploration of multiple reasoning paths simultaneously** ✓
  - Tree of Thoughts extends chain-of-thought prompting by systematically exploring and evaluating multiple reasoning branches, particularly effective for complex problem-solving.

- **B) Automatic prompt optimization can use reinforcement learning to improve prompts** ✓
  - RL-based prompt optimization systems can iteratively refine prompts based on outcome quality, similar to RLHF for model outputs.

- **D) Multimodal prompting allows combining text with other data types** ✓
  - Multimodal LLMs can process inputs combining text with images, audio, or other data types, expanding prompt engineering possibilities.

- **C) Zero-shot prompting always outperforms few-shot approaches** ✗
  - Few-shot prompting typically outperforms zero-shot for most tasks, especially complex ones, though the gap narrows with larger models.

- **E) The effectiveness of prompt techniques is independent of model architecture** ✗
  - Different model architectures respond differently to various prompt techniques; effectiveness is highly model-dependent.

### Question 2
**Correct answers: A, B, D**

- **A) Implementing hybrid search combining keyword and semantic retrieval** ✓
  - Hybrid search leverages both exact matching and semantic similarity for optimal retrieval, particularly for specialized terminology.

- **B) Chunking documents appropriately based on content structure** ✓
  - Strategic chunking that respects content boundaries (sections, paragraphs) improves retrieval relevance and context coherence.

- **D) Re-ranking retrieved documents based on relevance to the query** ✓
  - Re-ranking using cross-encoders or other techniques improves retrieval precision by considering query-document interactions more deeply.

- **C) Always retrieving the maximum possible number of documents** ✗
  - Quality and relevance of retrieved documents typically matter more than quantity; excess retrieval can dilute relevant information.

- **E) Using only the model's parametric knowledge for factual questions** ✗
  - Retrieval specifically addresses the limitations of parametric knowledge, especially for recent or specialized information.

### Question 3
**Correct answers: A, B, D**

- **A) Hierarchical task decomposition with sub-goal prioritization** ✓
  - Breaking complex goals into prioritized sub-goals enables effective long-term planning and resource allocation.

- **B) Implementing verification steps to check if goals were achieved** ✓
  - Verification ensures progress tracking and prevents the agent from moving forward with flawed assumptions.

- **D) Maintaining a state representation that tracks progress and failures** ✓
  - Persistent state tracking enables learning from failures and maintaining progress across multiple steps.

- **C) Executing all sub-tasks in parallel regardless of dependencies** ✗
  - Task dependencies often require sequential execution for correctness.

- **E) Avoiding replanning when initial plans encounter obstacles** ✗
  - Effective planning requires adapting to obstacles and unexpected outcomes.

### Question 4
**Correct answers: A, B, D**

- **A) Using smaller, specialized models for routine tasks and larger models for complex reasoning** ✓
  - This tiered approach optimizes resource usage while maintaining performance on critical tasks.

- **B) Implementing model routing based on task classification** ✓
  - Task classification enables directing queries to the most appropriate model architecture.

- **D) Creating ensembles that aggregate multiple model outputs for critical decisions** ✓
  - Ensembling can improve reliability and reduce biases by combining strengths of different models.

- **C) Always defaulting to the largest available model** ✗
  - Using the largest model for all tasks is inefficient and unnecessary.

- **E) Using identical prompts across all model types** ✗
  - Different model architectures often respond better to tailored prompt strategies.

### Question 5
**Correct answers: A, B, D**

- **A) Domain-specific continued pre-training on relevant corpora** ✓
  - Continued pre-training on domain text helps the model learn domain concepts and terminology.

- **B) Parameter-efficient fine-tuning focused on domain knowledge** ✓
  - PEFT methods like LoRA or adapters enable efficient domain adaptation while preserving general capabilities.

- **D) Creating domain-specific knowledge retrieval systems** ✓
  - Retrieval systems with domain knowledge complement model capabilities, especially for specialized information.

- **C) Avoiding domain-specific terminology in prompts** ✗
  - Domain terminology in prompts often improves performance by signaling relevant domain knowledge.

- **E) Using only generic models for all specialized domains** ✗
  - Domain adaptation significantly improves performance for specialized applications.

### Question 6
**Correct answers: A, B, D**

- **A) Larger models typically require less explicit instruction than smaller models** ✓
  - Larger models generally demonstrate better instruction-following with less detailed guidance.

- **B) Chain-of-thought reasoning yields more significant improvements in medium-sized models** ✓
  - The relative benefit of chain-of-thought is often greater for medium-sized models that need more reasoning support.

- **D) Few-shot examples remain useful even for the largest models** ✓
  - Even the largest models benefit from well-crafted examples for complex or unusual tasks.

- **C) Prompt engineering is unnecessary for the largest models** ✗
  - Prompt engineering remains valuable for all model sizes, though techniques may differ.

- **E) Smaller models always require more examples than larger models** ✗
  - While generally true, the relationship isn't universal; the type of task and model architecture also matter.

### Question 7
**Correct answers: A, B, D**

- **A) Implementing factuality scoring systems for generated content** ✓
  - Factuality scoring helps identify and flag potential hallucinations.

- **B) Combining multiple models with different knowledge cutoff dates** ✓
  - Model ensembles with different training cutoffs can help identify temporally inconsistent information.

- **D) Grounding generation in external, verified knowledge sources** ✓
  - External knowledge grounding (like RAG) provides factual anchoring for generation.

- **C) Using maximum temperature settings for all generation tasks** ✗
  - Higher temperatures typically increase creativity but also hallucination risk.

- **E) Avoiding all reference to uncertain knowledge areas** ✗
  - Acknowledging uncertainty is preferable to avoiding topics entirely.

## Section 2: Specialized Applications and Evaluation

### Question 8
**Correct answers: A, B, D**

- **A) Adapting complexity based on educational level** ✓
  - Level-appropriate content ensures material is neither too advanced nor too basic for learners.

- **B) Incorporating evidence-based pedagogical frameworks** ✓
  - Pedagogical best practices improve learning outcomes in AI-supported education.

- **D) Designing scaffolded prompts that guide learning progression** ✓
  - Scaffolding provides appropriate support that can gradually decrease as learners progress.

- **C) Providing identical explanations for all learner levels** ✗
  - Different learner levels require different approaches, examples, and language.

- **E) Focusing exclusively on factual delivery without engagement** ✗
  - Engagement is crucial for effective learning, not just factual correctness.

### Question 9
**Correct answers: A, B, D**

- **A) Using benchmark datasets specifically designed to test reasoning** ✓
  - Specialized reasoning benchmarks provide standardized evaluation of reasoning capabilities.

- **B) Implementing trace-based evaluation that examines reasoning steps** ✓
  - Analyzing intermediate steps reveals reasoning quality beyond just the final answer.

- **D) Comparing model reasoning to expert-annotated reasoning chains** ✓
  - Expert comparison provides a gold standard for reasoning quality assessment.

- **C) Focusing only on final answer accuracy without considering reasoning paths** ✗
  - The quality of reasoning matters, not just arriving at the correct answer.

- **E) Avoiding step-by-step reasoning to maximize efficiency** ✗
  - Step-by-step reasoning is essential for complex problem-solving and transparent decision-making.

### Question 10
**Correct answers: A, B, D**

- **A) Implementing clear disclaimers about the non-advisory nature of responses** ✓
  - Disclaimers set appropriate expectations and mitigate legal risks.

- **B) Designing prompts that avoid making definitive legal judgments** ✓
  - Avoiding definitive judgments helps maintain appropriate boundaries for AI in legal contexts.

- **D) Focusing on information provision rather than recommendation** ✓
  - Information provision is generally safer than specific recommendations in legal contexts.

- **C) Allowing the model to provide specific legal advice without verification** ✗
  - Specific legal advice from LLMs without expert verification poses significant risks.

- **E) Encouraging definitive interpretations of complex legal matters** ✗
  - Definitive interpretations of complex legal matters exceed appropriate AI boundaries.

### Question 11
**Correct answers: A, B, D**

- **A) Implementing intelligent caching for common queries** ✓
  - Caching eliminates redundant computation for frequently asked questions.

- **B) Using model distillation to create more efficient specialized models** ✓
  - Distillation can create smaller, faster models for specific tasks with minimal performance loss.

- **D) Dynamically adjusting context length based on task requirements** ✓
  - Using only necessary context reduces token usage and computational costs.

- **C) Always selecting the largest model for all tasks** ✗
  - Largest models are often unnecessary for simpler tasks and use more resources.

- **E) Maximizing prompt length regardless of task needs** ✗
  - Longer prompts increase token usage and costs without necessarily improving performance.

### Question 12
**Correct answers: A, B, D**

- **A) Implementing automatic fact extraction and verification against trusted sources** ✓
  - Automated verification provides systematic fact-checking at scale.

- **B) Designing prompts that explicitly request citations and evidence** ✓
  - Explicit requests for citations encourage attribution and verifiability.

- **D) Using retrieval systems that maintain links to original documents** ✓
  - Source links enable verification and provide additional context when needed.

- **C) Prioritizing confident answers over uncertain but cited responses** ✗
  - Uncertainty with citation is often preferable to unjustified confidence.

- **E) Avoiding references to external sources to test model knowledge** ✗
  - External references improve verifiability and accuracy, especially for specialized knowledge.

### Question 13
**Correct answers: A, B, D**

- **A) Blind comparison between human and LLM outputs** ✓
  - Blind comparison reduces bias in quality assessment.

- **B) Expert evaluation using domain-specific rubrics** ✓
  - Domain experts can assess nuanced aspects of quality that automated metrics might miss.

- **D) Multi-dimensional evaluation across relevance, accuracy, and helpfulness** ✓
  - Comprehensive evaluation captures the multiple aspects of quality that matter to users.

- **C) Focusing exclusively on grammatical correctness** ✗
  - Grammar is just one aspect of quality; content accuracy and relevance are equally important.

- **E) Using only automated metrics without human judgment** ✗
  - Automated metrics alone cannot capture all aspects of quality, especially subjective ones.

### Question 14
**Correct answers: A, B, D**

- **A) Adapting style and tone based on document type and audience** ✓
  - Context-appropriate style improves writing assistance effectiveness.

- **B) Incorporating user preferences and feedback over time** ✓
  - Personalization based on feedback creates more helpful writing assistance.

- **D) Maintaining document-level coherence through context awareness** ✓
  - Document-level awareness ensures suggestions fit the broader context.

- **C) Providing identical suggestions for all writing contexts** ✗
  - Different writing contexts require different approaches (academic, creative, business, etc.).

- **E) Prioritizing grammatical correctness over user intent** ✗
  - While grammar matters, preserving the user's intended meaning and voice is typically more important.

## Section 3: Emerging Trends and Enterprise Integration

### Question 15
**Correct answers: A, B, D**

- **A) Implementing middleware that handles data transformation between systems** ✓
  - Middleware facilitates communication between LLMs and legacy systems with different data formats.

- **B) Designing clear APIs with appropriate input validation** ✓
  - Well-designed APIs with validation improve reliability and security of integrated systems.

- **D) Ensuring appropriate authentication and authorization mechanisms** ✓
  - Security controls prevent unauthorized access and enforce appropriate use policies.

- **C) Replacing all existing systems with LLM-based alternatives** ✗
  - Complete replacement is typically impractical and unnecessary; integration is usually preferable.

- **E) Allowing unrestricted data flow between systems** ✗
  - Data flow restrictions are essential for security, privacy, and compliance.

### Question 16
**Correct answers: A, B, D**

- **A) Implementing monitoring for performance drift over time** ✓
  - Drift monitoring helps detect degradation before it impacts users significantly.

- **B) Collecting user feedback to identify improvement opportunities** ✓
  - User feedback reveals real-world performance issues and improvement opportunities.

- **D) Maintaining comprehensive documentation of system design decisions** ✓
  - Documentation supports maintenance, troubleshooting, and knowledge transfer.

- **C) Avoiding updates to deployed systems** ✗
  - Regular updates are essential for performance improvement and addressing issues.

- **E) Removing human oversight once systems are stabilized** ✗
  - Ongoing human oversight remains important even for mature systems.

### Question 17
**Correct answers: A, B, D**

- **A) Implementing staged deployment with increasing autonomy levels** ✓
  - Gradual autonomy increase allows monitoring system behavior before granting fuller autonomy.

- **B) Creating clear escalation paths for edge cases** ✓
  - Escalation paths ensure appropriate handling of situations beyond system capabilities.

- **D) Designing systems with appropriate capability limitations** ✓
  - Capability boundaries help ensure systems operate within safe parameters.

- **C) Prioritizing rapid deployment over thorough testing** ✗
  - Thorough testing is essential for responsible AI deployment.

- **E) Granting systems maximum capabilities regardless of use case** ✗
  - Capabilities should match use case requirements and safety considerations.

### Question 18
**Correct answers: A, B, D**

- **A) Implementing least-privilege access to enterprise systems** ✓
  - Least-privilege principles minimize security risks by granting only necessary access.

- **B) Designing comprehensive audit trails for agent actions** ✓
  - Audit trails enable accountability and help identify potential security issues.

- **D) Creating sandboxed environments for testing before deployment** ✓
  - Sandboxing prevents unintended consequences during development and testing.

- **C) Allowing unrestricted tool access to maximize capabilities** ✗
  - Unrestricted access creates significant security risks.

- **E) Minimizing monitoring to improve operational efficiency** ✗
  - Robust monitoring is essential for security, not an efficiency impediment.

### Question 19
**Correct answers: A, B, D**

- **A) Creating human-in-the-loop systems for critical decisions** ✓
  - Human oversight for critical decisions improves reliability and accountability.

- **B) Designing clear handoff protocols between automated and human processes** ✓
  - Clear handoffs ensure smooth transitions between automated and human components.

- **D) Implementing feedback mechanisms that improve system performance over time** ✓
  - Human feedback enables continual system improvement.

- **C) Minimizing human involvement to maximize automation** ✗
  - Human involvement remains valuable for judgment, oversight, and exceptional cases.

- **E) Replacing human experts entirely with autonomous systems** ✗
  - Augmentation rather than replacement typically yields better outcomes for complex domains.

### Question 20
**Correct answers: A, B, D**

- **A) Starting with focused applications that demonstrate clear ROI** ✓
  - Targeted applications with measurable benefits build organizational confidence.

- **B) Designing systems that augment rather than replace human expertise** ✓
  - Augmentation leverages complementary strengths of humans and AI.

- **D) Implementing robust evaluation frameworks to measure business impact** ✓
  - Impact measurement demonstrates value and guides future development.

- **C) Deploying comprehensive solutions that transform entire business processes at once** ✗
  - Incremental approaches typically reduce risk and improve adoption.

- **E) Prioritizing technological sophistication over business alignment** ✗
  - Business alignment should drive technological choices, not vice versa.