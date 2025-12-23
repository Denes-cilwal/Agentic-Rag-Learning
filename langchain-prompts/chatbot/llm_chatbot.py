from langchain_openai import ChatOpenAI
from langchain_core.messages import (
    SystemMessage,
    HumanMessage,
    AIMessage,
)
from dotenv import load_dotenv
import streamlit as st

load_dotenv()
# If you don’t pass model="...", it uses LangChain/OpenAI defaults (depends on your installed versions / config).
model = ChatOpenAI()

"""
while True: starts the loop (no condition to stop on its own).
It asks you for input: You:
If you type exit or quit, it runs break
break stops the loop, so the program ends.
Otherwise, it continues and repeats again (asks you again).
"""
chat_history = [
    SystemMessage(content="You are a helpful assistant."),
]

while True:
    user_input = input("You: ")
    chat_history.append(HumanMessage(content=user_input))
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting chat. Goodbye!")
        break

    response = model.invoke(chat_history)
    chat_history.append(AIMessage(content=response.content))
    print("AI Bot:", response.content)

# print the entire chat history after exiting the loop
# conversation history now has context about who sent what message

print("\nChat History:", chat_history)    

