from langchain_community.document_loaders import TextLoader
from langchain_openai import ChatOpenAI
from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import PromptTemplate
from dotenv import load_dotenv

load_dotenv()

model = ChatOpenAI()

prompt = PromptTemplate(
    input_variables=["text"],
    template="Summarize the following text:\n\n{text}\n\nSummary:",
    
)



parser = StrOutputParser()


loader = TextLoader("cricket.txt", encoding="utf8")
load_as_documents = loader.load()
print(load_as_documents)
print(type(load_as_documents))
print(len(load_as_documents))

print("----- Loaded as list by document loader -----")
print(load_as_documents[0])
print((load_as_documents[0].metadata))


chain = prompt | model | parser
result = chain.invoke({"text": load_as_documents[0].page_content})
print("----- Summary of the loaded document -----")
print(result)


# Output: A list of Document objects containing the text from cricket.txt -  loaded as list by document loader

# [Document(metadata={'source': 'cricket.txt'}, 
# page_content="Beneath the sun or floodlight's gleam,\n\nCricket lives like a waking dream.\n\nA field of green, a willowed sound,\n\n")]