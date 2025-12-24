from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.runnables import RunnableBranch, RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv

load_dotenv()

# 1. Initialize the LLM
model = ChatOpenAI(model="gpt-4o")

# 2. Define specialized chains
tech_chain = PromptTemplate.from_template(
    "You are a Senior Engineer. Fix this: {input}"
) | model

billing_chain = PromptTemplate.from_template(
    "You are a Billing Specialist. Address this payment issue: {input}"
) | model

general_chain = PromptTemplate.from_template(
    "You are a friendly assistant. Answer this: {input}"
) | model

# 3. Create a Classification Chain
# This step determines where the input should go
classification_template = PromptTemplate.from_template(
    "Classify the following user input as 'technical', 'billing', or 'general'. "
    "Respond with only one word.\n\nInput: {input}"
)
classifier = classification_template | model | StrOutputParser()

# 4. Define the RunnableBranch
# Syntax: RunnableBranch((condition, action), (condition, action), ..., default_action)
branch = RunnableBranch(
    (lambda x: "technical" in x["topic"].lower(), tech_chain),
    (lambda x: "billing" in x["topic"].lower(), billing_chain),
    general_chain # The default
)

# 5. Connect it all together using RunnableSequence using LCEL expression
full_chain = (
    {"topic": classifier, "input": RunnablePassthrough()} 
    | branch 
    | StrOutputParser()
)

# --- Execution ---
print(full_chain.invoke({"input": "My credit card was charged twice!"}))
print(full_chain.get_graph().print_ascii())