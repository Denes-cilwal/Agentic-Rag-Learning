from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from typing import TypedDict, Annotated, Optional

load_dotenv()

model = ChatOpenAI(model="gpt-4", temperature=0.5)

# This tells LangChain: “I want an output with exactly these keys and types.”
"""
Without Annotated, the LLM only sees the field names and types.
The LLM only knows the field names and that they're strings. It has to guess what "summary" and "sentiment" mean.



With Annotated, you provide additional context about each field:

Explicit instructions to the LLM: The second argument in Annotated becomes part of the schema sent to OpenAI, 
telling the model exactly what to generate for each field

Clarifies expected values: For sentiment, it explicitly states
valid options: 'positive', 'negative', or 'mixed' - reducing ambiguity

Better output quality: The LLM gets clear guidance rather 
than inferring from just the field name, leading to more consistent and accurate results

Self-documenting code: Developers reading your code understand 
what each field represents without checking separate documentation

"""
class Review(TypedDict):
    key_themes : Annotated[str, "Write down the main themes discussed in the review"]
    summary: Annotated[str, "A brief summary of the review"]
    sentiment: Annotated[str, "The overall sentiment, e.g. 'positive', 'negative', or 'mixed'"]
    pros:   Annotated[Optional[list[str]], "Write down the positive aspects mentioned in the review in list format"]
    cons: Annotated[Optional[list[str]], "Write down the negative aspects mentioned in the review in list format"]

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