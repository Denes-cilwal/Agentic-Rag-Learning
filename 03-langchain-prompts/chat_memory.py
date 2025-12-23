from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate, MessagesPlaceholder
from langchain_core.messages import HumanMessage, AIMessage

from dotenv import load_dotenv
load_dotenv()
model = ChatOpenAI()

# mports ChatPromptTemplate, which lets you build prompts as chat messages (system / human / ai), not just plain text.
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    MessagesPlaceholder("history"),
    ("human", "{input}")
])

"""
What it does in your example
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Summarize {paper} in {style} style.")
])


This creates a template object that, when you later run:

prompt.invoke({"paper": "Attention Is All You Need", "style": "technical"})


…it fills the placeholders and produces a list of message objects like:

System: “You are a helpful assistant.”

Human: “Summarize Attention Is All You Need in technical style.”
That message list is what you pass to ChatOpenAI.
"""

history = []

while True:
    user_input = input("You: ")
    if user_input.lower() in ["exit", "quit"]:
        break

    # build messages with history + new input
    msgs = prompt.invoke({"history": history, "input": user_input})

    ai_msg = model.invoke(msgs)
    print("AI:", ai_msg.content)

    # store history
    history.append(HumanMessage(content=user_input))
    history.append(AIMessage(content=ai_msg.content))
