from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=32)

result = embedding.embed_query("Delhi is the capital of India.")
print(result)
print(str(len(result)))  # should print 32

"""
this is query of single sentence/document | query
larger the dimension, better the quality of embeddings
larger the dimension, higher the cost of embeddings
"""
