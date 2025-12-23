from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate
from dotenv import load_dotenv

load_dotenv()
model = ChatOpenAI()

prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful assistant."),
    ("human", "Explain {topic} in {style} style.")
])

messages = prompt.invoke({"topic": "transformers", "style": "beginner-friendly"})
response = model.invoke(messages)

print(response.content)
