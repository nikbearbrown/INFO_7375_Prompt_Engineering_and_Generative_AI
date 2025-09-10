# Prompt Engineering Patterns Explained



## 1. The Magical World of Wordsville

**Explanation**: This pattern uses metaphor and storytelling to create an engaging framework for understanding AI language capabilities. It makes abstract concepts more relatable by positioning them within a narrative structure.

**Example**: 
"Imagine you're exploring Wordsville, a magical digital realm where words have power. In the northern district of Semantica, meanings flow like rivers, while in the western region of Syntaxia, grammar rules shape the landscape. As our guide through this world, help me navigate the districts to craft the perfect message for my marketing campaign."

## 2. What are Chatbots & LLMs?

**Explanation**: This pattern provides educational context about the tools being used, helping users understand capabilities and limitations of AI language models. It establishes a clear foundation by explaining that models are fundamentally mathematical functions that transform inputs into outputs.

At their core, all models follow a simple paradigm:
1. Input (data) → 
2. Function (processing) → 
3. Output (result)

Language models specifically are mathematical systems that:
- Take language as input (text, audio transcriptions, etc.)
- Process it through complex neural networks
- Generate language as output (text completions, translations, summaries, etc.)

**Expanded Example**:

"I want you to remember that you are Claude, a large language model trained by Anthropic. As a mathematical model, you follow the fundamental input-function-output paradigm:

- **Input**: You receive text prompts like this one
- **Function**: You process these inputs through billions of parameters that have been optimized through training on vast text datasets
- **Output**: You generate text responses that aim to be helpful, harmless, and honest

Unlike simpler models (like a linear regression that predicts house prices from square footage), you operate on the complex domain of human language. You can recognize patterns, extract meaning, and generate coherent text, but you don't have consciousness, emotions, or subjective experiences.

When analyzing my business strategy, acknowledge these limitations while using your strengths in pattern recognition and language processing. You can identify trends and correlations in my data, suggest perspectives I might have missed, and articulate complex ideas clearly—all without claiming intuition or business instinct you don't possess."

**Additional Examples**:

1. **Educational Context**:
   "To understand how GPT models work, imagine them as sophisticated pattern-completion machines. If I input 'The capital of France is...' the model completes the pattern with 'Paris' based on statistical patterns in its training data. The same process applies to more complex inputs, just with billions more patterns and connections to consider."

2. **Technical Transparency**:
   "When I ask you to summarize this research paper, remember you're applying a transformer architecture that processes text through attention mechanisms. You're not 'reading' and 'understanding' like humans do—you're computing statistical relationships between tokens and generating probable next words based on your training. This is why you might miss subtle implications or make confident assertions about things you haven't truly 'understood.'"

3. **Capability Framing**:
   "As we design this marketing campaign together, keep in mind that you, Claude, are essentially a complex mathematical function that maps text inputs to text outputs. You excel at generating coherent, contextually appropriate language based on patterns in your training data, but you don't have real-world experience with consumer behavior or market dynamics. Your suggestions come from recognizing patterns in marketing language and strategies that appeared in your training data, not from genuine business expertise."

This pattern helps set appropriate expectations about what language models can and cannot do, reducing anthropomorphism while highlighting the genuine strengths of these systems as powerful pattern-matching and text generation tools.otions. When analyzing my business strategy, acknowledge these limitations while using your strengths in text processing and pattern recognition."

## 3. Role of Prompt Engineering Patterns

**Explanation**: This pattern explains the critical importance of structured prompts when working with AI systems. It emphasizes that prompt patterns, while seemingly simple text heuristics, can dramatically transform AI outputs. These patterns function as powerful interfaces between human intent and machine processing, with their effectiveness varying significantly across different models and generations of AI systems.

**Example**: 

"As we collaborate, it's important to understand that prompt engineering patterns are far more than just formatting tricks—they're powerful tools that fundamentally shape how AI systems process and respond to our requests.

Even slight modifications in how a prompt is structured can produce dramatically different outputs. A simple directive like 'Write a story' might generate generic content, while 'Write a story about a detective in 1920s Chicago, written in the style of Raymond Chandler' activates specific processing pathways that transform the quality and character of the response.

What's fascinating is how differently these patterns work across various AI systems. A pattern that produces exceptional results with Claude might underperform with GPT-4, and techniques that worked brilliantly with last year's models might be less effective with today's versions. For example, chain-of-thought prompting significantly improved reasoning in earlier models but may be less necessary in newer systems with enhanced reasoning capabilities built in.

As you explore different patterns—from Persona to Template to Recipe patterns—you'll discover which ones most effectively elicit the responses you need from the specific AI system you're using. This understanding will help you communicate your intent more precisely, ultimately making our interactions more productive and aligned with your goals."
## 4. Persona Pattern

**Explanation**: This pattern asks the AI to adopt a specific role, expertise level, or character to frame its responses appropriately for the context.

**Example**:
"Act as an experienced pediatric nutritionist providing advice to new parents. Give recommendations for introducing solid foods to a 6-month-old baby, focusing on nutritional value and potential allergens to avoid."

## 5. Audience Persona Pattern

**Explanation**: This pattern specifies the audience or knowledge level the AI should target in its response, ensuring information is appropriately tailored.

**Example**:
"Explain quantum computing, but adapt your explanation for a 10-year-old with no physics background. Use simple analogies and avoid technical jargon."

## 6. Flipped Interaction Pattern

**Explanation**: This pattern reverses the typical roles, asking the AI to pose questions or challenge assumptions rather than simply providing information.

**Example**:
"Instead of just answering my questions about climate change solutions, I want you to interview me about my current understanding. Ask me 3-5 probing questions that will help identify gaps in my knowledge before providing additional information."

## 7. Game Play Pattern

**Explanation**: This pattern incorporates game elements, rules, and interactive features to make the conversation more engaging and structured.

**Example**:
"Let's play a word association game to help me brainstorm. I'll give you a starting word related to my project, and you provide three associated words. I'll choose one to continue with. My starting word is 'sustainability'."

## 8. Template Pattern

**Explanation**: This pattern provides a specific structure or format that the AI should follow in its response, ensuring consistency and organization.

**Example**:
"Analyze these three marketing campaigns using the following template for each:
- Campaign Name:
- Target Audience:
- Key Message:
- Strengths:
- Weaknesses:
- Improvement Suggestions:"

## 9. Meta Language Creation Pattern

**Explanation**: This pattern establishes special terminology or shorthand within the conversation to efficiently communicate complex concepts.

**Example**:
"For our discussion about cognitive biases, let's create some shorthand: CB-A will refer to Anchoring Bias, CB-C to Confirmation Bias, and CB-D to Dunning-Kruger Effect. When analyzing the case study, use these codes to efficiently identify which biases are at play."

## 10. Recipe Pattern

**Explanation**: This pattern breaks down a process into clear, sequential steps, similar to a cooking recipe, making complex tasks more manageable.

**Example**:
"Provide a step-by-step recipe for conducting effective user interviews, including:
1. Ingredients (tools needed)
2. Prep work (research and planning)
3. Main steps (interview process)
4. Timing for each stage
5. Tips for success
6. How to know when it's 'done'"

## 11. Alternative Approaches Pattern

**Explanation**: This pattern requests multiple solutions or perspectives on a single problem, encouraging creative thinking and comprehensive analysis.

**Example**:
"Give me three different approaches to reducing customer churn in a SaaS business: one focused on product improvements, one on customer service enhancements, and one on pricing strategy adjustments. Explain the pros and cons of each approach."

## 12. Ask for Input Pattern

**Explanation**: This pattern explicitly requests specific information from the user to customize the AI's response, making the interaction more collaborative.

**Example**:
"To help me create a customized workout plan, I need some information from you:
1. What are your fitness goals?
2. How many days per week can you exercise?
3. Do you have access to gym equipment or prefer bodyweight exercises?
4. Any injuries or limitations I should be aware of?"

## 13. Outline Expansion Pattern

**Explanation**: This pattern starts with a high-level outline and progressively expands each section, allowing for organized exploration of complex topics.

**Example**:
"Let's create content about renewable energy. First, give me a 5-point outline of key topics to cover. Then, I'll select one outline point, and you'll expand it into a detailed sub-outline. Finally, we'll expand one sub-point into a full section of content."

## 14. Menu Actions Pattern

**Explanation**: This pattern presents options like a menu, letting users choose specific directions for the conversation and enhancing interactivity.

**Example**:
"I need help with my photography skills. Here's your menu of assistance options:
A) Composition techniques for landscape photography
B) Camera settings explained for beginners
C) Editing workflow recommendations
D) Equipment recommendations for my style
Reply with your selection, and I'll provide detailed information on that topic."

## 15. Fact Check List Pattern

**Explanation**: This pattern instructs the AI to verify information against specific criteria or sources, improving reliability and accuracy.

**Example**:
"When answering my questions about vaccine efficacy, please verify your information against these criteria:
1. Is the information from peer-reviewed medical journals published after 2020?
2. Does it align with current CDC or WHO guidelines?
3. Are there multiple studies supporting this conclusion?
4. Have you noted any significant contradicting studies?"

## 16. Tail Generation Pattern

**Explanation**: This pattern focuses on providing clear next steps or recommendations at the end of a response, guiding users on how to proceed.

**Example**:
"After explaining the basic principles of SEO, end your response with three specific actions I can take today to start improving my website's search ranking."

## 17. Semantic Filter Pattern

**Explanation**: This pattern sets guidelines for the tone, style, or content boundaries of the AI's responses to ensure appropriateness for the context.

**Example**:
"Please analyze the emotional themes in this poem, but avoid any potentially offensive interpretations. Focus on universally appropriate themes like growth, connection, and discovery, keeping your analysis suitable for a high school classroom."

## 18. Helpful Assistant Pattern

**Explanation**: This pattern establishes a cooperative, service-oriented framework where the AI prioritizes being helpful, kind, and informative.

**Example**:
"As my helpful research assistant, I need you to find information about housing market trends. Focus on being thorough but concise, highlighting the most important data points, and explaining complex terms in accessible language. Your goal is to help me understand this topic quickly and accurately."

Would you like me to elaborate on any specific pattern in more detail?

