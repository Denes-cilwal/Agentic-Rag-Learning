# # how to interact lanchain with openai

# from langchain_openai import OpenAI
# from dotenv import load_dotenv

# load_dotenv()

# # create openai object 

# llm = OpenAI(model_name="gpt-3.5-turbo-instruct", temperature=0.7)

# # invoke is very important method to interact with in langchain
# # the llm invoke will hit passed model and return the response
# llm_response = llm.invoke("What is the capital of France?")
# print(llm_response)



from dotenv import load_dotenv
from langchain_openai import OpenAI

load_dotenv()

# create openai object
# temporary set max_tokens to 5 for testing purpose
# restrict tokens to avoid large output
llm = OpenAI(model="gpt-3.5-turbo-instruct", temperature=0.7, max_tokens=5)
print(llm.invoke("write 5 lines of poetry about the sea."))
