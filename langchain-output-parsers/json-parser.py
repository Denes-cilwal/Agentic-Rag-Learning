"""
Docstring for langchain-output-parsers.json-parser

While the StrOutputParser is great for simple text, 
the JsonOutputParser is what you use when you want t
he AI to return data that your code can immediately treat as a Python dictionary.

This is extremely powerful for "Automated Data Extraction" tasks.

The Pydantic Approach (Recommended)
The easiest way to use the JsonOutputParser is to define a "blueprint" (a Pydantic class) 
so the parser knows exactly what keys to look for.
"""

from typing import List
from langchain_core.output_parsers import JsonOutputParser
from langchain_core.prompts import PromptTemplate
from pydantic import BaseModel, Field
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# 1. Define the structure you want
class Movie(BaseModel):
    title: str = Field(description="The name of the movie")
    year: int = Field(description="The year it was released")
    actors: List[str] = Field(description="A list of main actors")

# 2. Setup Parser and Inject Instructions
"""
When you initialize JsonOutputParser(pydantic_object=Person), 
the parser generates a long string of instructions. 
It says to the LLM: "You must return JSON. 
It must have a key called 'name' as a string and 'age' as an integer."
"""
parser = JsonOutputParser(pydantic_object=Movie)

# 3. Create a prompt that includes the parser's instructions
# format_instructions tells the LLM exactly how the JSON should look
prompt = PromptTemplate(
    template="Answer the user query.\n{format_instructions}\n{query}",
    input_variables=["query"],
    partial_variables={"format_instructions": parser.get_format_instructions()},
)

# 4. Chain it together
model = ChatOpenAI(model="gpt-4o-mini")

"""
Step,Component,Action
1,Prompt,Combines your user question + the Pydantic-based JSON instructions.
2,Model,"Receives the instructions. Instead of ""chatting,"" it attempts to write code-like JSON."
3,Output,"The Model sends back a raw string: '{""name"": ""Alice"", ""age"": 30}'."
4,Parser,This is the critical part. The parser takes that string and runs Person.model_validate_json().
5,Result,"If it passes validation, you get a clean Python Dictionary (or Pydantic object)."


"""

chain = prompt | model | parser

"""
Definition vs. Execution
The Chain (|): This is the Blueprint. It tells LangChain: "When I give you data, first put it in this prompt,
 then send it to this model, then clean it with this parser."

The .invoke(): This is the Action. It actually passes
 your specific data (like "Stranger Things") into that blueprint and starts the calculation.

"""


# 5. Run it
result = chain.invoke({"query": "Tell me about the series Stranger Things season 1."})

print(type(result)) # Output: <class 'dict'>
print(result["year"]) # Output: 2016