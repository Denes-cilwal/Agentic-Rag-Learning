from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict

load_dotenv()

model = ChatOpenAI()

# This tells LangChain: “I want an output with exactly these keys and types.”
class Review(TypedDict):
    summary: str
    sentiment: str  # e.g. "positive" | "negative" | "mixed"

# structured_output is not the raw model anymore. It is like: Model + “output must match Review” + “parse into Python”
"""
Wraps the base model to guarantee the output matches the Review schema
Instead of getting raw text, you get a Python dictionary with the exact keys specified
The model automatically extracts/generates the summary and determines sentiment from the input

"""
structured_output = model.with_structured_output(Review)

print(structured_output)


"""structured_output.invoke(...) does the following:
The model receives this text along with instructions to output data matching the Review schema
OpenAI's API generates:
A summary string that condenses the review
A sentiment string (likely "mixed" given the positive and negative feedback)
LangChain automatically parses the response into a Python dictionary

"""

result = structured_output.invoke(
    "The hardware specifications of the new iPhone are impressive. "
    "There are too many installed apps that I cannot remove. "
    "Also the UI looks cluttered. Hoping for a better experience next time."
)

print(result)              # {'summary': '...', 'sentiment': 'mixed'}
print(result["summary"])
print(result["sentiment"])


"""
 This approach ensures type-safe, predictable outputs 
 that can be directly used in your application without 
 manual parsing or validation. The LLM is instructed to 
 structure its response according to your schema automatically.

"""