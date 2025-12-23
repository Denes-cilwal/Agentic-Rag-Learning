"""
Docstring for 06-langchain-chains.03-parallel-chains
How the Parallel Flow Works
In your diagram, the flow follows these specific stages:

User Input: A single piece of data  enters the system.


The Parallel Split: Instead of waiting for one task to finish,
 the input is sent to two separate models (or chains) at the exact same time.

Branch 1: One model processes the input to generate Notes.
Branch 2: A second model (or the same model with a different prompt) processes the input to generate a Quiz.

The Merge: The outputs from both branches are collected into a 
single dictionary (e.g., {"notes": "...", "quiz": "..."}).


Final Output: This merged data is then passed to a 
final model or output stage to be presented to the user.


"""



from langchain_openai import ChatOpenAI
from langchain_anthropic import ChatAnthropic
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableParallel

load_dotenv()

model1 = ChatOpenAI()

# model2 = ChatAnthropic(model_name='claude-3-7-sonnet-20250219')

prompt1 = PromptTemplate(
    template='Generate short and simple notes from the following text \n {text}',
    input_variables=['text']
)

prompt2 = PromptTemplate(
    template='Generate 5 short question answers from the following text \n {text}',
    input_variables=['text']
)

prompt3 = PromptTemplate(
    template='Merge the provided notes and quiz into a single document \n notes -> {notes} and quiz -> {quiz}',
    input_variables=['notes', 'quiz']
)

parser = StrOutputParser()

# this is independent task
parallel_chain = RunnableParallel({
    'notes': prompt1 | model1 | parser, # first branch
    'quiz': prompt2 | model1 | parser # second branch
})

"""
. The Automatic Dictionary Creation
RunnableParallel is designed to 
return a dictionary. Once both branches finish, the output of this stage is:

Python

{
    "notes": "...(OpenAI's output)...",
    "quiz": "...(Claude's output)..."
}

The Merge Stage (merge_chain)
You then pipe (|) that dictionary into prompt3.

Because your prompt3 has variables {notes} and {quiz}, it automatically matches the keys in the dictionary to the variables in the prompt.
model1 then takes this combined prompt and writes a single, final document
"""


# this is 2nd stage after parallel
merge_chain = prompt3 | model1 | parser

chain = parallel_chain | merge_chain

text = """
Support vector machines (SVMs) are a set of supervised learning methods used for classification, regression and outliers detection.

The advantages of support vector machines are:

Effective in high dimensional spaces.

Still effective in cases where number of dimensions is greater than the number of samples.

Uses a subset of training points in the decision function (called support vectors), so it is also memory efficient.

Versatile: different Kernel functions can be specified for the decision function. Common kernels are provided, but it is also possible to specify custom kernels.

The disadvantages of support vector machines include:

If the number of features is much greater than the number of samples, avoid over-fitting in choosing Kernel functions and regularization term is crucial.

SVMs do not directly provide probability estimates, these are calculated using an expensive five-fold cross-validation (see Scores and probabilities, below).

The support vector machines in scikit-learn support both dense (numpy.ndarray and convertible to that by numpy.asarray) and sparse (any scipy.sparse) sample vectors as input. However, to use an SVM to make predictions for sparse data, it must have been fit on such data. For optimal performance, use C-ordered numpy.ndarray (dense) or scipy.sparse.csr_matrix (sparse) with dtype=float64.
"""

result = chain.invoke({'text':text})

print(result)

chain.get_graph().print_ascii()


"""Output

          +---------------------------+            
            | Parallel<notes,quiz>Input |            
            +---------------------------+            
                 **               **                 
              ***                   ***              
            **                         **            
+----------------+                +----------------+ 
| PromptTemplate |                | PromptTemplate | 
+----------------+                +----------------+ 
          *                               *          
          *                               *          
          *                               *          
  +------------+                    +------------+   
  | ChatOpenAI |                    | ChatOpenAI |   
  +------------+                    +------------+   
          *                               *          
          *                               *          
          *                               *          
+-----------------+              +-----------------+ 
| StrOutputParser |              | StrOutputParser | 
+-----------------+              +-----------------+ 
                 **               **                 
                   ***         ***                   
                      **     **                      
           +----------------------------+            
           | Parallel<notes,quiz>Output |            
           +----------------------------+            
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