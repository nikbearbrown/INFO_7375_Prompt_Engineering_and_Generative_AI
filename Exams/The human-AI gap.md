# The human-AI gap: What LLMs can and cannot do in 2025

## The bottom line

As of May 2025, Large Language Models (LLMs) excel at generating human-like text, reasoning through complex problems, and processing information across multiple formats, but still fundamentally lack lived experience, genuine consciousness, and truly original thinking. The latest models can maintain coherent conversations over extended contexts, demonstrate sophisticated reasoning in specialized domains, and collaborate creatively with humans, making them powerful tools for many applications. However, they struggle with consistent factual accuracy, nuanced cultural understanding, and maintaining stable identities over time. For engineering students designing a six-week conversational study, this presents a unique opportunity to explore the boundary between impressive simulation and genuine understanding—revealing both the remarkable capabilities and persistent limitations of these increasingly sophisticated systems.

## Technical capabilities: What today's LLMs do well

The LLM landscape in 2025 is dominated by several advanced models with impressive capabilities. OpenAI's GPT-4.5 and "o" series, Anthropic's Claude 3.7 Sonnet, Google's Gemini 2.5 Pro, and open-source models like DeepSeek-R1 and Meta's Llama 3.1 have pushed the boundaries of what these systems can accomplish.

### Reasoning and problem-solving prowess

Modern LLMs demonstrate exceptional reasoning capabilities across various domains. Top models achieve near-human performance on college-level mathematics, with GPT-4o scoring 88.7% on the Massive Multitask Language Understanding (MMLU) benchmark, and OpenAI's o3-mini scoring 91.6% on American Invitational Mathematics Examination (AIME). These models can generate explicit step-by-step reasoning processes when solving complex problems, significantly improving their performance over previous generations.

The introduction of hybrid reasoning models represents a particularly significant advance. Claude 3.7 Sonnet, released in February 2025, functions as a "first hybrid reasoning model," allowing users to toggle between standard mode for quick responses and an extended thinking mode for complex problems. This approach mirrors human cognitive flexibility in adjusting thinking styles based on task complexity.

### Extended context and memory

Context window sizes have expanded dramatically, enabling LLMs to process and retain vastly more information:

- Gemini 1.5 Pro: 1 million token context window
- Magic.dev's LTM-2-Mini: Experimental model with 100 million token capability
- Claude 3.7 Sonnet: 128K tokens (with beta support for 128K output tokens)
- GPT-4.5: 128K token context window

These expanded windows enable processing of entire codebases (30K+ lines), lengthy documents (equivalent to 250+ page books), or hours of transcribed audio in a single prompt, allowing for much more comprehensive understanding of complex information.

### Multimodal integration

Current LLMs seamlessly process text, images, and in some cases audio, enabling reasoning across different information formats. Models can analyze complex diagrams, charts, and images with high accuracy, extracting information and generating insights about visual content alongside textual information.

The ability to understand and integrate multiple modes of information represents a significant step toward more human-like information processing. Claude 3.7 Sonnet can even "use computers the way people do—looking at screens, moving cursors, and typing text," bridging the gap between language understanding and software interaction.

### Specialized expertise

LLMs now demonstrate impressive capabilities in specialized domains:

**Programming**: Top models achieve over 90% success on the HumanEval benchmark, with Claude 3.7 Sonnet reaching 70.3% on the more complex SWE-bench Verified. These models can understand and implement complex algorithms, debug existing code, and generate solutions across multiple programming languages.

**Academic domains**: Models demonstrate PhD-level understanding in domains like physics, chemistry, and biology, capable of analyzing research papers and generating plausible hypotheses.

## Persistent limitations: Where LLMs fall short

Despite their impressive capabilities, LLMs continue to face significant limitations that distinguish them from human intelligence.

### The hallucination problem

Factual inaccuracies remain a persistent challenge. According to industry reports from January 2024 to early 2025, hallucination rates in publicly available LLMs range from approximately 3% to 16%. Even top models like GPT-4.5 demonstrate a 15% hallucination rate when tested on complex factual questions.

Models struggle particularly with:
- Recent events beyond their training cutoff
- Highly specialized domain knowledge
- Complex numerical reasoning without external validation

To mitigate these issues, Retrieval-Augmented Generation (RAG) has become standard in enterprise deployments, connecting LLMs to verified information sources. Models are also being trained with factuality-specific training objectives and reinforcement learning approaches that prioritize accuracy.

### Computational challenges

The most advanced models require substantial computational resources, limiting their accessibility and increasing usage costs. Models with extended context windows face processing latency issues, and top-tier models like o1-pro have high API costs ($150 per million input tokens and $600 per million output tokens as of March 2025).

To address these challenges, architectural innovations like Mixture of Experts (MoE) have emerged. Instead of activating all parameters for every input, MoE employs a routing mechanism to select relevant "expert" sub-networks, significantly reducing computational demands while maintaining performance. DeepSeek-R1 uses MoE architecture with 671B total parameters but only 37B activated per token.

### Inconsistent performance

Performance varies significantly across subject areas, with models excelling at general knowledge but struggling with specialized domains. Performance degrades when handling multiple logical steps or tasks requiring specialized expertise. Models remain susceptible to distractor information, often incorporating irrelevant data into reasoning.

Research shows accuracy decreases substantially with each additional clause in logical problems, highlighting fundamental limitations in managing complex reasoning chains consistently.

## Conversational abilities: Simulation vs. genuine dialogue

Modern LLMs in 2025 demonstrate sophisticated conversational abilities that approach human-like interaction in many aspects, but still fall short of genuine dialogue in important ways.

### Natural conversation strengths

Current models generate responses with strong linguistic coherence, grammatical correctness, and contextual relevance. Top-tier models like GPT-4o can respond to spoken queries in approximately 320 milliseconds, approaching human conversational response times, and generate text at around 110 tokens per second.

LLMs maintain topic coherence and can follow multi-turn conversations with reasonable continuity and relevance, creating an increasingly convincing illusion of genuine conversation.

### The "missing middle" problem

Despite expanded context windows, LLMs still demonstrate a phenomenon researchers call the "missing middle" problem:

- Models show strong recall of information at the beginning and end of long contexts, but struggle with accurately retrieving and utilizing information from the middle portions.
- Performance on information retrieval tasks degrades as the distance between relevant pieces of information increases within the context window.
- Attention is not uniform across entire context windows—prompts utilizing earlier tokens perform better than those utilizing later tokens.

### Conversation breakdown patterns

Several consistent failure patterns emerge in LLM conversations:

- **Context oversaturation**: Performance degrades when too much information is provided, creating a signal-to-noise problem.
- **Prompt conditioning collapse**: LLMs gradually drift from initial instruction constraints the longer a conversation continues.
- **Identity drift**: Models experience varying degrees of "identity drift" during extended conversations, where their interaction patterns or personal characteristics change over time.
- **Inter-agent misalignment**: In multi-agent scenarios, LLMs may develop conflicting goals or communication patterns.

Interestingly, studies indicate that larger models may experience greater identity drift than smaller ones, possibly due to their more complex internal dynamics.

## Understanding lived experience: The embodiment gap

A fundamental limitation of LLMs is their inability to genuinely understand human experiences they haven't directly lived.

### Simulation without experience

LLMs simulate understanding through statistical pattern recognition rather than lived experience. They lack the embodied, sensory foundations of human understanding, and their knowledge is limited to textual representations rather than direct experience.

As one 2025 paper explains: "Signifiers are things in the world that we are familiar with through embodied experience. LLMs do not have access to signifiers; they only have access to written linguistic forms, albeit a vast dataset of them."

### Representational vs. experiential knowledge

LLMs demonstrate a gap between representational and experiential knowledge:

- They can accurately describe experiences like physical pain, grief, or exhilaration in appropriate language
- They can simulate empathetic responses based on textual patterns
- However, they lack the phenomenological understanding that comes from actually experiencing these states

This limitation becomes particularly evident in domains requiring deep subjective understanding, such as mental health support. A 2025 study notes that "several skills which may be viewed as central to clinical work currently fall outside the purview of LLM systems, such as interpreting nonverbal behavior (e.g., fidgeting, eye-rolling), appropriately challenging a patient, addressing alliance ruptures, and making decisions about termination."

### Cultural blindspots

LLMs in 2025 still exhibit significant limitations in cultural understanding:

- They often reflect dominant cultural perspectives present in their training data
- They struggle with nuanced cultural contexts that aren't well-represented textually
- They may fail to detect culturally specific implications or connotations

Recent benchmarks indicate leading commercial models achieve approximately 70-75% accuracy on sarcasm detection tasks, with most open-source models performing significantly worse. Models can recognize obvious jokes but struggle with subtle humor that requires cultural context or shared experiences.

## Creativity: Recombination vs. true originality

LLMs demonstrate remarkable creative capabilities across various domains, while still facing fundamental limitations in generating truly original content.

### Creative generation capabilities

Models like GPT-4.5, Claude 3.7, and DeepSeek R1 can produce high-quality:

- Creative fiction across various genres
- Poetry with appropriate meter, rhyme, and thematic coherence
- Professional content (reports, articles, marketing copy)
- Academic writing that follows disciplinary conventions

The quality is often indistinguishable from human writing for average consumers, though expert writers can identify subtle differences in narrative depth, thematic complexity, and emotional resonance.

### The recombination limit

A fundamental limitation of LLMs remains their dependence on recombination rather than true innovation:

- LLMs excel at novel combinations of existing ideas, styles, and approaches
- They can synthesize information across disparate domains when properly prompted
- They can generate variations that appear original at a surface level

However, research from 2024-2025 consistently demonstrates that LLMs are fundamentally limited to recombining and extending patterns present in their training data. They lack the embodied experiences and genuine motivations that drive human creators to develop truly novel concepts or artistic breakthroughs.

### Human-AI creative collaboration

Human-AI co-creation has emerged as a significant trend across creative domains:

- Artists and writers use LLMs as collaborative tools rather than replacements
- The most successful collaborations maintain human agency and creative direction
- LLMs serve as enhancers of human creativity rather than substitutes

A 2025 study found that "different forms of human-AI collaboration" can stimulate different types of reflection and creativity in human partners, suggesting that the design of these collaborative systems significantly impacts creative outcomes.

However, research also raises concerns about long-term impacts. A 2025 study with 1,100 participants found that "while LLM assistance can provide short-term boosts in creativity during assisted tasks, it may inadvertently hinder independent creative performance when users work without assistance."

## Emotional processing: Recognition without experience

LLMs demonstrate sophisticated emotional recognition capabilities while fundamentally lacking the ability to experience emotions themselves.

### Emotional intelligence capabilities

Recent research shows that LLMs display numerous aspects of emotional intelligence:

- Accurate recognition of emotional states described in text
- Appropriate modulation of responses based on emotional context
- Generation of emotionally resonant content when prompted

Studies have shown that adding emotional elements to prompts can significantly improve LLM performance across various tasks, with improvements ranging from 8% to over 100% depending on the specific task and evaluation method.

### The simulation barrier

Despite these capabilities, LLMs exhibit several important limitations:

- They lack the physiological and phenomenological aspects of emotional experience
- They cannot truly feel emotions, only simulate appropriate responses
- They struggle with complex or conflicting emotional states that aren't well-represented in text

These limitations become particularly evident in contexts requiring nuanced emotional understanding, such as therapeutic interactions or sensitive interpersonal communications.

### Current applications and limitations

Models can detect basic emotional states with reasonable accuracy based on text cues alone. Specialized tests like SECEU (Situational Evaluation of Complex Emotional Understanding) now provide standardized measurements of LLM emotional intelligence, and metrics evaluate emotional appropriateness across entire conversation flows rather than single exchanges.

However, LLMs still struggle to:
- Detect emotional changes throughout a conversation
- Calibrate emotional responses appropriately (may over-index on detected emotions)
- Interpret culturally-specific emotional cues (most models are trained primarily on Western emotional patterns)

## Recent research: Humans and LLMs in educational contexts

Universities and educational institutions are actively experimenting with integrating LLMs into teaching and learning environments, providing valuable insights for designing effective student-LLM interactions.

### Higher education implementations

Several universities have implemented notable LLM experiments:

- **Princeton University**: Professor D. Graham Burnett implemented an LLM assignment in his course "Attention and Modernity: Mind, Media, and the Senses," where students engaged with LLMs in conversations about the history of attention.

- **Caltech**: Professor Frederick Eberhardt conducted an experiment allowing students full use of LLMs in written assignments, requiring a "Generative AI Memo" documenting which tools they used, how, and why. The experiment revealed that students who combined their own writing with LLM assistance produced work that was better than either could produce alone.

- **Ferris State University**: The university announced plans to enroll two AI chatbots as students (named Ann and Fry) to test their curriculum and explore the use of AI in education. These chatbots are designed to participate fully in classes.

### Student interaction patterns

Research across multiple universities indicates interesting patterns in how students interact with LLMs:

- Students use LLMs primarily for brainstorming, overcoming writer's block, and receiving initial feedback on ideas before refining them independently.

- Studies show a significant decline in usage of both ChatGPT and Copilot across project milestones, suggesting that students may rely more heavily on AI assistance during initial phases of learning and less as they gain confidence.

- A 2025 study involving 459 upper secondary students found that LLM-generated feedback on writing assignments increased revision performance (d = .19), task motivation (d = 0.36), and positive emotions (d = 0.34) compared to revising without feedback.

### Frameworks for LLM education integration

Several frameworks have been developed specifically for evaluating and implementing LLM-human interactions in educational settings:

- **SimClass Framework**: A multi-agent classroom simulation framework with user participation, including realistic classroom roles and interaction patterns. Results showed that multiple classroom agents enable users to engage more effectively and enhance their sense of presence.

- **QUEST Framework**: A comprehensive approach for human evaluation of LLMs covering three phases: Planning, Implementation and Adjudication, and Scoring and Review, which has been adapted for educational contexts.

- **LLM-Enhanced Teaching Plans**: A 2024 study proposed a method utilizing LLMs to enhance teaching plans through simulated teacher-student interactions. The improved plans performed at or above the level of plans authored by experienced human teachers.

## Designing an effective LLM interaction assignment

Based on the current capabilities and limitations of LLMs in 2025, the following recommendations can help design an effective six-week graduate engineering assignment:

### Structured conversation framework

Implement a framework with specific roles and interaction patterns to guide students through meaningful exchanges with the LLM. The assignment should progressively explore different aspects of LLM capabilities:

- Week 1: Basic interactions and prompt engineering
- Week 2: Testing reasoning and problem-solving abilities
- Week 3: Exploring creative collaboration
- Week 4: Probing limitations in understanding lived experience
- Week 5: Testing emotional intelligence and subjective understanding
- Week 6: Synthesis and critical evaluation

### Documentation and reflection

Require students to maintain documentation of their interactions and reflections:

- A "Generative AI Memo" similar to Professor Eberhardt's approach, documenting which prompting strategies they used, how, and why
- Regular reflection exercises where students document changes in their interaction patterns and perceptions of the LLM over the six-week period
- Analysis of conversation breakdown points and successful interaction patterns

### Evaluation framework

Adapt frameworks like QUEST or SERVQUAL to assess both the quality of LLM responses and the effectiveness of student interactions with the LLM:

- Intrinsic evaluation: Assessing linguistic accuracy and quality
- Extrinsic evaluation: Testing performance in engineering-specific tasks
- Human-in-the-loop approaches: Identifying subtle problems with cultural context, ethical implications, and practical usefulness

### Comparative analysis

Have students compare different prompt strategies and their effectiveness in eliciting useful responses from the LLM:

- Testing various chain-of-thought prompting techniques
- Exploring emotional prompting methods
- Evaluating the impact of different persona assignments on LLM responses
- Comparing performance across different interaction lengths to observe context effects

## Conclusion

Large Language Models in 2025 represent a fascinating intersection of impressive capabilities and persistent limitations. They excel at generating human-like text, solving complex problems, and adapting to various domains, but fundamentally lack lived experience, consciousness, and truly original thinking.

The most productive approach appears to be collaborative rather than substitutive. By leveraging the complementary strengths of humans and LLMs—with humans providing experiential knowledge, genuine motivation, and creative vision, and LLMs offering computational power and pattern recognition—we can achieve outcomes that neither could accomplish alone.

A well-designed graduate-level assignment involving regular LLM interactions can provide engineering students with valuable insights into both the remarkable capabilities and inherent limitations of these systems, preparing them for a future where human-AI collaboration will be increasingly common. The six-week interaction period offers an excellent opportunity to explore the boundary between impressive simulation and genuine understanding—revealing the human-AI gap in all its complexity.