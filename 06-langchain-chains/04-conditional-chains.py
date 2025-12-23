"""
Docstring for 06-langchain-chains.04-conditional-chains
In LangChain, handling Conditional Logic is done using the RunnableBranch 
or the more modern RunnableLambda (using a Python function to decide the path).

A classic developer use case is a Support Router: Depending on the "sentiment" or "intent" 
of a user's message, the chain should route the request to different 
models or prompts.

1. The Use Case: Intelligent Support RouterStep 
1: Analyze the incoming message.
Step 2 (The Condition):If it's a Technical Issue $\rightarrow$ Route to a "Tech Expert" prompt.
If it's a Billing Issue $\rightarrow$ Route to a "Billing Specialist" prompt.
Otherwise $\rightarrow$ Route to a "General FAQ" prompt.

"""


from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_core.runnables import RunnableLambda
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini")

# --- Define our specialized prompts ---
tech_prompt = PromptTemplate.from_template("You are a Senior Engineer. Fix this: {input}")
billing_prompt = PromptTemplate.from_template("You are a Billing Specialist. Resolve this: {input}")
general_prompt = PromptTemplate.from_template("You are a helpful assistant. Answer this: {input}")

# --- Logic to decide which path to take ---
def route_request(info):
    # 'info' will be the output from the previous step in the chain
    query = info["input"].lower()
    if "error" in query or "bug" in query or "code" in query:
        return tech_prompt | model | StrOutputParser()
    elif "payment" in query or "refund" in query or "price" in query:
        return billing_prompt | model | StrOutputParser()
    else:
        return general_prompt | model | StrOutputParser()

# --- Build the Chain ---
# We use RunnableLambda to inject the 'route_request' function into the pipeline
full_chain = RunnableLambda(route_request)

# --- Test it ---
print("--- Tech Routing ---")
print(full_chain.invoke({"input": "I have a syntax error in my Python script."}))

print("\n--- Billing Routing ---")
print(full_chain.invoke({"input": "Where can I request a refund for my last invoice?"}))

"""
hy this is powerful for Developers
Cost Efficiency: You can route simple questions to cheaper models 
(like GPT-4o-mini) and complex technical bugs to expensive models (like Claude 3.7 or GPT-4o).

Specialization: A "one-size-fits-all" prompt often fails. 
By branching, you can give the AI very specific personas (e.g., "You are a database admin") only when needed.

Clean Code: Instead of a giant if/else block inside 
your main application code, the routing logic is built directly into the Chain Graph

"""