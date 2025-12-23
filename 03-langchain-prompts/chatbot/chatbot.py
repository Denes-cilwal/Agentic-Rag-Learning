from langchain_openai import ChatOpenAI
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
chat_history = []

while True:
    user_input = input("You: ")
    chat_history.append(user_input)
    if user_input.lower() in ['exit', 'quit']:
        print("Exiting chat. Goodbye!")
        break

    response = model.invoke(user_input)
    chat_history.append(f"AI Bot: {response.content}")
    print("AI Bot:", response.content)

# print the entire chat history after exiting the loop

print("\nChat History:", chat_history)    

# but the problem here is the model has no context about who sent what message.
# To solve this we can use ChatMessage objects from langchain_core.schema
# systemmessage, humanmessage, aimessage etc.