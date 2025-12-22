from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv

load_dotenv()  # expects ANTHROPIC_API_KEY in your .env
model = ChatAnthropic(model="claude-2", temperature=0.7, max_tokens=5)
model = model.invoke("What is the capital of France?")
print(model.content)