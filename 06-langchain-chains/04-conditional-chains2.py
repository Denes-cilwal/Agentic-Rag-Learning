"""
Docstring for 06-langchain-chains.01-simple_chain
1. The Flow: Step-by-Step
The pipeline is a sequence of two main stages: Classification and Branching.

Stage 1: The Classifier (classifier_chain)
Input: Receives a raw string like "This is a beautiful phone".

Structured Reasoning: Instead of a simple chat response, 
it uses a PydanticOutputParser to force the LLM to return a structured object.

Output: This stage results in a Pydantic object: Feedback(sentiment='positive').


Stage 2: The Router (branch_chain)
Evaluation: The RunnableBranch receives that Pydantic 
object and checks its properties.

Conditional Execution:

If sentiment == 'positive', it executes the Positive 
Response Chain (prompt2 | model | parser).

If sentiment == 'negative', it executes the Negative 
Response Chain (prompt3 | model | parser).

Final Output: The user receives a human-friendly 
response tailored to their specific mood.

"""



from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel, RunnableBranch, RunnableLambda
from langchain_core.output_parsers import PydanticOutputParser
from pydantic import BaseModel, Field
from typing import Literal

load_dotenv()

model = ChatOpenAI()

parser = StrOutputParser()

class Feedback(BaseModel):

    sentiment: Literal['positive', 'negative'] = Field(description='Give the sentiment of the feedback')

parser2 = PydanticOutputParser(pydantic_object=Feedback)

prompt1 = PromptTemplate(
    template='Classify the sentiment of the following feedback text into postive or negative \n {feedback} \n {format_instruction}',
    input_variables=['feedback'],
    partial_variables={'format_instruction':parser2.get_format_instructions()}
)

classifier_chain = prompt1 | model | parser2

prompt2 = PromptTemplate(
    template='Write an appropriate response to this positive feedback \n {feedback}',
    input_variables=['feedback']
)

prompt3 = PromptTemplate(
    template='Write an appropriate response to this negative feedback \n {feedback}',
    input_variables=['feedback']
)

branch_chain = RunnableBranch(
    (lambda x:x.sentiment == 'positive', prompt2 | model | parser),
    (lambda x:x.sentiment == 'negative', prompt3 | model | parser),
    RunnableLambda(lambda x: "could not find sentiment")
)

# final chain 
chain = classifier_chain | branch_chain

print(chain.invoke({'feedback': 'This is a beautiful phone'}))

chain.get_graph().print_ascii()