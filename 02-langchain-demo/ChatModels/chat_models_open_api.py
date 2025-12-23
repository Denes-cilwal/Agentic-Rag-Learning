from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()  # expects OPENAI_API_KEY in your .env

model = ChatOpenAI(model="gpt-4", temperature=0.7, max_tokens=5)
model = model.invoke("What is the capital of France?")
print(model.content)



# there is minimal difference between ChatOpenAI and Anthropic chat model implementation
# that's why langchain provides similar interface for both models