# This code is a toy (nakli = fake) version of how LangChain used to work with PromptTemplate + LLM + LLMChain.
from random import random
class NakliLLM:
  def __init__(self):
    print('LLM created')

  def predict(self, prompt):
    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]
    return {'response': random.choice(response_list)}

"""A nakli (fake) LLM that randomly returns one of a few canned responses.

class NakliLLM:
  def __init__(self):
    print('LLM created')

  def predict(self, prompt):
    response_list = [
        'Delhi is the capital of India',
        'IPL is a cricket league',
        'AI stands for Artificial Intelligence'
    ]
    return {'response': random.choice(response_list)}


What it does
When you create it: prints “LLM created”
When you call predict(prompt):
it ignores the prompt
randomly picks one sentence from response_list
returns it as a dict: {"response": "..."}
So it behaves like a very dumb LLM.
 
 """

class NakliPromptTemplate:
  def __init__(self, template, input_variables):
    self.template = template
    self.input_variables = input_variables

  def format(self, input_dict):
    return self.template.format(**input_dict)

"""
# NakliPromptTemplate (fake prompt template)
class NakliPromptTemplate:
  def __init__(self, template, input_variables):
    self.template = template
    self.input_variables = input_variables

  def format(self, input_dict):
    return self.template.format(**input_dict)


What it does

Stores:

template: a string with placeholders like {length} {topic}
input_variables: list of allowed placeholder names
format(input_dict) fills the placeholders using Python string formatting:


template = "Write a {length} poem about {topic}"
template.format(**{"length":"short","topic":"india"})

"""

class NakliLLMChain:
  def __init__(self, llm, prompt):
    self.llm = llm
    self.prompt = prompt

  def run(self, input_dict):
    final_prompt = self.prompt.format(input_dict)
    result = self.llm.predict(final_prompt)
    return result['response']

template = NakliPromptTemplate(
    template='Write a {length} poem about {topic}',
    input_variables=['length', 'topic']
)

llm = NakliLLM()
chain = NakliLLMChain(llm=llm, prompt=template)


# this is not flexible, just for demo