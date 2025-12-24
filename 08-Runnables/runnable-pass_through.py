# from langchain_core.runnables import RunnableParallel, RunnablePassthrough, RunnableLambda

# summarize = RunnableLambda(lambda x: x[:5] + "...")  # pretend this is an LLM

# chain = RunnableParallel({
#     "original": RunnablePassthrough(),  # keep input as-is
#     "summary": summarize,               # also create something from it
# })

# print(chain.invoke("This is a long message"))


"""
Why Passthrough matters here

Without it, you’d only get the summary (processed output).
Passthrough lets you return both:

the input (original)

and the new computed thing (summary)
"""


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel, RunnablePassthrough

load_dotenv()

prompt1 = PromptTemplate(
    template='Write a joke about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

prompt2 = PromptTemplate(
    template='Explain the following joke - {text}',
    input_variables=['text']
)

joke_gen_chain = RunnableSequence(prompt1, model, parser) 

parallel_chain = RunnableParallel({
    'joke': RunnablePassthrough(), # keep the joke as-is but for that we need to generate it first from joke_gen_chain
    'explanation': RunnableSequence(prompt2, model, parser)
})

# combine both chains
final_chain = RunnableSequence(joke_gen_chain, parallel_chain)

print(final_chain.invoke({'topic': 'computers'}))




print(final_chain.get_graph().print_ascii())


"""
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
        +---------------------------------+        
        | Parallel<joke,explanation>Input |        
        +---------------------------------+        
                 **              ***               
              ***                   **             
            **                        ***          
+----------------+                       **        
| PromptTemplate |                        *        
+----------------+                        *        
          *                               *        
          *                               *        
          *                               *        
  +------------+                          *        
  | ChatOpenAI |                          *        
  +------------+                          *        
          *                               *        
          *                               *        
          *                               *        
+-----------------+               +-------------+  
| StrOutputParser |               | Passthrough |  
+-----------------+               +-------------+  
                 **              **                
                   ***        ***                  
                      **    **                     
        +----------------------------------+       
        | Parallel<joke,explanation>Output |       
        +----------------------------------+    

"""