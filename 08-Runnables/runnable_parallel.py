from langchain_openai import ChatOpenAI
from langchain_core.prompts import PromptTemplate
from langchain_core.output_parsers import StrOutputParser
from dotenv import load_dotenv
from langchain_core.runnables import RunnableSequence, RunnableParallel

load_dotenv()

prompt1 = PromptTemplate(
    template='Generate a tweet about {topic}',
    input_variables=['topic']
)

prompt2 = PromptTemplate(
    template='Generate a Linkedin post about {topic}',
    input_variables=['topic']
)

model = ChatOpenAI()

parser = StrOutputParser()

parallel_chain = RunnableParallel({
    'tweet': RunnableSequence(prompt1, model, parser), # first task using runnable sequence
    'linkedin': RunnableSequence(prompt2, model, parser) # second task using runnable sequence
})

result = parallel_chain.invoke({'topic':'AI'})

print(result['tweet'])
print(result['linkedin'])



"""
What “same input to each branch” means

If you do this:

parallel = RunnableParallel({
  "a": branchA, # each branch is sequence or any runnable
  "b": branchB,
})


and then run:

parallel.invoke(INPUT)


LangChain does:

branchA.invoke(INPUT)
branchB.invoke(INPUT)

Same input to each branch” means both branches get the same dictionary, not different ones:

✅ Tweet branch input: {"topic":"AI"}
✅ LinkedIn branch input: {"topic":"AI"}
with the exact same INPUT object/value.


tweet_out = (prompt1 | model | parser).invoke({"topic": "AI"})
linkedin_out = (prompt2 | model | parser).invoke({"topic": "AI"})

result = {
  "tweet": tweet_out,
  "linkedin": linkedin_out,
}
"""

