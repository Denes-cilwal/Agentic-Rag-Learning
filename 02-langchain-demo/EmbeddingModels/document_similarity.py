from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from sklearn.metrics.pairwise import cosine_similarity
import numpy as np

load_dotenv()

embedding = OpenAIEmbeddings(model="text-embedding-3-large", dimensions=300)

documents = [
    "Virat Kohli is a famous Indian cricketer.",
    "Ms Dhoni is a former captain of the Indian cricket team.",
    "Rohit Sharma is known for his elegant batting style and is a key player in the Indian cricket team.",
    "Sachin Tendulkar is regarded as one of the greatest batsmen in the history of cricket.",
    "Jasprit Bumrah is a leading fast bowler for India."
]


query = 'tell me about virat kohli'

# generate embeddings for documents
# each vector will be in 300-dimensional space
doc_embeddings = embedding.embed_documents(documents)

# now we need to store these embeddings in some vector database for efficient similarity search
# but for simplicity, we will compute cosine similarity directly here

# generate embedding for query - single vector
query_embedding = embedding.embed_query(query)

# compute cosine similarities between query and document embeddings
similarities_scores = cosine_similarity([query_embedding], doc_embeddings)[0]
print("Cosine Similarities:", similarities_scores)

# [[0.66308802 0.29264069 0.3978261  0.39597744]] # example output
# [0.66, 0.29, 0.39, 0.39] # here 0.66 is comparision with first document and so on

# print(sorted(list(enumerate(similarities_scores)), key=lambda x: x[1]))

index, score = sorted(list(enumerate(similarities_scores)), key=lambda x: x[1], reverse=True)[0]

print(f"Most similar document to the query: '{documents[index]}' with a similarity score of {score}")
