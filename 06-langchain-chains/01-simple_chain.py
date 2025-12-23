


from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()  # Load environment variables from .env file


prompt = PromptTemplate(
    template = "Generate 5 interesting facts about {topic}.",
    input_variables=["topic"]
)


model = ChatOpenAI()
parser = StrOutputParser()

# forming chains 
# lanchain expression syntax

chain =  prompt | model | parser

# invoke chain
result = chain.invoke({"topic": "space exploration"})
"""
when you call invoke on the chain, the input is passed to the prompt template, which formats the prompt with the given topic.
The formatted prompt is then sent to the ChatOpenAI(model) which generates a response based on the prompt.(model invoke is called automatically in the chain)
The response from the model is then passed to the StrOutputParser, which processes the output and returns it as a string.

"""

print(result)

print(chain.get_graph().draw_ascii())  # visualize the chain structure in ascii format

"""chain graph structure:
     +-------------+       
     | PromptInput |       
     +-------------+       
            *              
            *              
            *              
    +----------------+     
    | PromptTemplate |     
    +----------------+     
            *              
            *              
            *              
      +------------+       
      | ChatOpenAI |       
      +------------+       
            *              
            *              
            *              
   +-----------------+     
   | StrOutputParser |     
   +-----------------+     
            *              
            *              
            *              
+-----------------------+  
| StrOutputParserOutput |


"""

