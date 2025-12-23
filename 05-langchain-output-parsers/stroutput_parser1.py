
"""
You want a 2-step pipeline:

Ask the model to write a detailed report about a topic.

Take that report text and ask the model to write a 5-line summary.
"""
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()

model = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.7)

# 1st prompt -> detailed report
template1 = PromptTemplate(
    template='Write a detailed report on {topic}',
    input_variables=['topic']
)

# 2nd prompt -> summary
template2 = PromptTemplate(
    template='Write a 5 line summary on the following text. /n {text}',
    input_variables=['text']
)


# how to use stroutputparser

parser = StrOutputParser()

# forming a chain (chain is bascially a pipeline where output of one step is input to next step)
# this is entire pipeline in one line
# much easier to read and maintain as compared to previous code in stroutput_parser.py

# Pipe Operator (|): This is the modern LangChain way to build pipelines (chains).
"""
The Breakdown of Your Chain

Your chain is defined as: chain = template1 | model | parser | template2 | model | parser

- Here is exactly what happens step-by-step when you run chain.invoke({'topic':'black hole'}):
- template1: Receives {'topic': 'black hole'} and produces a formatted string: "Write a detailed report on black hole".
- model (1st call): Receives that string and generates an AIMessage object containing a long report.
- parser (1st call): Takes the AIMessage and extracts only the text as a clean string.

Crucial Step: Without this parser, the next step would receive a complex object instead of just the text.

- template2: Receives that clean string (the report) and injects it into the {text} variable, creating a new prompt: "Write a 5 line summary on the following text... [Full Report Content]".
- model (2nd call): Receives the summary prompt and generates a new AIMessage with the 5-line summary.
- parser (2nd call): Cleans the final output so result is just a plain Python string.


"""

chain = template1 | model | parser | template2 | model | parser

result = chain.invoke({'topic':'black hole'})
print(result)

