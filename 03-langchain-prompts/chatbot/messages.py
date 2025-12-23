from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)

from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# If you don’t pass model="...", it uses LangChain/OpenAI defaults (depends on your installed versions / config).
model = ChatOpenAI()

"""
HumanMessage: Represents a message sent by a human user to LLM.
AIMessage: Represents a message sent by the AI model in response to user input.
SystemMessage: Represents system-level instructions or context provided to the LLM to guide its behavior.
(for example, setting the tone of the conversation, providing background information, or defining specific rules for interaction).
for example. You are a helpful assistant.
"""

message = [
    SystemMessage(content="You are a helpful assistant."),
    HumanMessage(content="Tell me a joke about computers."),

]

model_response = model.invoke(message)
messages = AIMessage(content=model_response.content)
print(messages.content)