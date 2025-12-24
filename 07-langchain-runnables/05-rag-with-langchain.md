# 📚 Retrieval-Augmented Generation (RAG) with LangChain

This repository demonstrates how a manual RAG (Retrieval-Augmented Generation) pipeline works and how LangChain simplifies it using chains.

## 🔍 What is RAG?

Retrieval-Augmented Generation (RAG) is an architecture where:

- Relevant information is retrieved from external knowledge (documents, PDFs, DBs).
- The retrieved content is injected into the LLM prompt.
- The LLM generates an answer grounded in that data.

RAG is commonly used for:

- Question answering over documents
- Chatbots over private data
- Knowledge assistants

## 🧩 Manual RAG Flow (Step-by-Step)

The image/code shows a manual implementation of the RAG retrieval task.

### 1️⃣ Load Documents

```python
loader = TextLoader("docs.txt")
documents = loader.load()
```

Reads raw text data into LangChain Document objects.

### 2️⃣ Split Documents into Chunks

```python
text_splitter = RecursiveCharacterTextSplitter(
    chunk_size=500,
    chunk_overlap=50
)
docs = text_splitter.split_documents(documents)
```

Splitting improves retrieval accuracy and prevents context overflow.

### 3️⃣ Create Embeddings & Store in Vector DB

```python
vectorstore = FAISS.from_documents(docs, OpenAIEmbeddings())
```

Converts text chunks → embeddings

Stores them in FAISS for similarity search

### 4️⃣ Retrieve Relevant Documents

```python
retriever = vectorstore.as_retriever()
retrieved_docs = retriever.get_relevant_documents(query)
```

This is the retrieval task in RAG.

### 5️⃣ Manually Build Prompt

```python
retrieved_text = "\n".join(doc.page_content for doc in retrieved_docs)

prompt = f"""
Based on the following text, answer the question:
{query}

{retrieved_text}
"""
```

All retrieved chunks are manually stuffed into the prompt.

### 6️⃣ Call the LLM

```python
answer = llm.predict(prompt)
```

The LLM generates an answer using retrieved context.

## ⚠️ Problems with Manual RAG

- ❌ Repetitive boilerplate code
- ❌ Hard to maintain and extend
- ❌ No control over prompt strategy
- ❌ Easy to exceed token limits
- ❌ No standard interface

## LangChain Solution: Chains

LangChain provides chains to encapsulate the retrieval + LLM logic into reusable components.

Instead of manually wiring everything, you define what you want, not how.

### RetrievalQA Chain (Classic)

LangChain bundles:

- Retriever
- Prompting logic
- LLM call

into a single chain.

```python
from langchain.chains import RetrievalQA
from langchain_openai import ChatOpenAI

qa_chain = RetrievalQA.from_chain_type(
    llm=ChatOpenAI(model="gpt-4o-mini", temperature=0.2),
    retriever=retriever,
    chain_type="stuff",
    return_source_documents=True
)

result = qa_chain.invoke({"query": "What are the key takeaways?"})
print(result["result"])
```

#### What the chain does internally

- Takes the query
- Calls the retriever
- Formats documents
- Builds the prompt
- Calls the LLM
- Returns the answer (+ sources)
