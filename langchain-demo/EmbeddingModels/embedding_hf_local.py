from langchain_huggingface import HuggingFaceEmbeddings

embeddings = HuggingFaceEmbeddings(model_name="sentence-transformers/all-MiniLM-L6-v2")
documents = [
    "Delhi is the capital of India.",
    "Mumbai is the financial capital of India.",
    "Bangalore is the IT hub of India.",
    "Paris is the capital of France."
]

vector_embeddings = embeddings.embed_documents(documents)
print(vector_embeddings)
print(str(len(vector_embeddings)))  # should print 4