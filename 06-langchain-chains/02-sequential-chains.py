from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser

load_dotenv()  # Load environment variables from .env file


prompt1 = PromptTemplate(
    template = "Generate detailed report on {topic}.",
    input_variables=["topic"]
)

prompt2 = PromptTemplate(
    template = "Generate 5 points summary on following text \n {text}",
    input_variables=["text"]
)

model = ChatOpenAI()
parser = StrOutputParser()

# forming chains - sequential chain
chain =  prompt1 | model | parser | prompt2 | model | parser
"""
the chain works as follows:
1. The input topic is passed to prompt1, which generates a detailed report on the topic.
2. The detailed report is then sent to the ChatOpenAI model, which generates a response based on the report.
3. The response from the model is processed by the StrOutputParser to return it as a string.
4. This string (detailed report) is then passed to prompt2, which generates a 5-point summary of the report.
5. The summary is sent again to the ChatOpenAI model for final processing.
6. The final response from the model is processed by the StrOutputParser to return the summary as a string.
"""

# invoke chain
result = chain.invoke({"topic": "artificial intelligence"})
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
+-----------------------+  
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
+-----------------------+               
"""