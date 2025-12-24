"""
Docstring for 07-langchain-runnables.11-langchain-runnable

Runnable approach solves this by standardizing composition

Instead of creating new chain classes for every workflow, you:

- wrap each step as a Runnable
- connect steps using |
- reuse and rearrange steps easily
"""

import random
from typing import Any, Dict

from langchain_core.runnables import RunnableLambda, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

class NakliLLM:
    def __init__(self):
        print("Initialized NakliLLM")

    def predict(self, prompt:str) -> dict[str, str]:
        response_list = [
            "Roses are red, violets are blue.",
            "The sun sets in the west, painting the sky with hues.",
            "In the quiet of the night, dreams take flight.",
            "Mountains stand tall, touching the sky's call."
        ]
        response = random.choice(response_list)
        """
        predict(prompt) simulates an LLM call.
        It returns a dict: {"response": "...random..."}
        Why dict?
        Many LLM wrappers return structured data (text + metadata).
        Your earlier chain returned only the "response" field
        """
        return {"response": response}


# Fake Prompt Template (NakliPromptTemplate)


class NakliPromptTemplate:
    def __init__(self, template: str, input_variables: list[str]):
        self.template = template
        self.input_variables = input_variables

    """
    Meaning
Holds a template: "Write a {length} poem about {topic}"
Expects length and topic in inputs
Validates missing keys and then formats the string

input - {"length": "short", "topic": "india"}
Returns - "Write a short poem about india" -> output

    """
    def format(self, input_dict: Dict[str, Any]) -> str:
        missing = [k for k in self.input_variables if k not in input_dict]
        if missing:
            raise ValueError(f"Missing input variables: {missing}")
        return self.template.format(**input_dict)


# Creating Runnable steps

# Prompt runnable: dict -> string

# ----------------------------
# 3) Build Runnables
# ----------------------------
template = NakliPromptTemplate(
    template="Write a {length} poem about {topic}",
    input_variables=["length", "topic"],
)

llm = NakliLLM()

# Runnable: dict -> formatted prompt string -> dict -> string
prompt_runnable = RunnableLambda(lambda x: template.format(x))

"""
Input: {"length":"short","topic":"india"}
Output: "Write a short poem about india"
So this is your “prompt formatting step” as a Runnable.
"""


# Runnable: prompt string -> LLM raw dict output - LLM runnable: string -> dict
"""
Input: "Write a short poem about india"
Output: {"response": "IPL is a cricket league"} (random)
This is your “LLM call step” as a Runnable.
"""
llm_runnable = RunnableLambda(lambda prompt: llm.predict(prompt))

# Runnable: LLM raw dict -> final string
# (Using a parser-like step)
# Extract runnable: dict -> string
"""
Input: {"response": "Delhi is the capital of India"}
Output: "Delhi is the capital of India"

This replaces your old return result["response"].
"""
extract_response = RunnableLambda(lambda d: d["response"])

# ----------------------------
# 4) Compose the "chain" using Runnable connectors (|)

"""
This is the core of Runnables.

It means:

run prompt_runnable
feed its output into llm_runnable
feed its output into extract_response

"""
# ----------------------------
chain = prompt_runnable | llm_runnable | extract_response

# ----------------------------
# 5) Run / Invoke
# ----------------------------
result = chain.invoke({"length": "short", "topic": "india"})
print(result)
