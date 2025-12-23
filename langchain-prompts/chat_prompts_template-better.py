from langchain_core.prompts import ChatPromptTemplate
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage


chat_template = ChatPromptTemplate(
   ('system', 'You are a helpful {domain} expert.'),
    ('human', 'Explain in simple terms, what is {topic}?')
)



prompt = chat_template.invoke({"domain": "science", "topic": "quantum physics"})
print(prompt)

"""
messages=[SystemMessage(content='You are a helpful {domain} expert.', additional_kwargs={}, response_metadata={}), 
HumanMessage(content='Explain in simple terms, what is {topic}?', additional_kwargs={}, response_metadata={})]

"""

"""
what is message placeholders?
- message placeholders are variables within message templates that can be dynamically replaced with 
specific values when the template is invoked. In the provided code snippet, placeholders like {
domain} and {topic} are used in the system and human messages. 
When the prompt is invoked with specific values for these placeholders (e.g., "science" for {domain} and "quantum physics" for {topic}), 
'they are replaced accordingly to generate a complete message.
"""
