# README — RAG + Data Ingestion Pipeline Notes (as in notebook)

## Data ingestion pipeline

**(Data ingestion pipeline)**  
`data -> Parsing -> Embedding -> (vector DB / vector store)`

**Supported data examples:**

- PDF
- HTML
- Excel

> Data parsing is very important step (How do you read unstructure and chunk the data)

> Once you start complete chunking you pass to embedding model where you converts Text -> vectors)

> (vector) is a just a numerical representation of text.

> So that you will be able to apply Similarity search, cosine similarity techniques that are already available, wherein similar kind of results based on a specific query can be retrieved from particular database.

### Flow diagram — Data ingestion pipeline

```
data-ingestion.png
```

---

## RAG? (simple GenAI application)

**Diagram idea:**
```
user -> (Query + prompt) -> LLM -> o/p
```

Let consider I have user, user is giving a query and before sending to LLM it is added to prompt (i.e. a instruction to LLM (how LLM should work). based on this, we get output.

This is simple GenAI application -

---
### (1) Hallucination

Every llm that is trained, will be trained for every specific data.

Right now it is 17Dec, &  
Let this is LLM model GPT5, Now lets say this LLM model is trained with data only till 31st August.

So there is a big gap between 31 - 12

When you query on data after 31 it will starts hallucination which is biggest disadvantage of LLM.

---

## Retrieval Pipeline (Traditional RAG)ill starts hallucination which is biggest disadvantage of LLM.

## Retrieval Pipeline (Traditional RAG)

Now, this query instead of directly goes to LLM.

Our query is also send to vectordb where embedder is applied (numeric representation) where similarity search is applied and this vector db return a context

**Example query written:**

> What's leave policy

**Flow:**
```
Context + prompt -> LLM -> output
```

This pipeline is called Retrieval Pipeline (Traditional RAG)

Here will you remove some amount of hallucination why

## Vector DB / Vector Store + Embedding models

vector db is my vector DB or vector store here we are storing embedding (is applied)

**Embedding model sources mentioned:**

- google gemini embedding models
- huggin face
- openai embedding models

so each embedding model comes with cost & also there are open source embedding models.

---

## Hollucinations different from data:

This knowledge base does not exist with LLM.

---

## Company/private data + Fine tuning (why not always)
This knowledge base does not exist with LLM.

Company/private data + Fine tuning (why not always)

even though it doesnot have knowledge, it try to pretend answer and it will make sure the ans LLM returns.

lets say i am running startup and I have data like policies of company.

This data will not be publicly available.

one solution is, we can take the data and finetune the model.

but finetune model is very tedious process, because this LLM has billions of parameters.
so, everytime we cannot finetune it. So How can we prevent it?

---

## Instead of finetuning, implement RAG

Instead of finetuning, we can implement rag.

(Along with LLM I will be having external database (vector database) and we are going to create data ingestion pipeline here)

There will be two important piplines that will be created Here, we are trying to optimize the pipeline that we are creating

---

## RAG + external vector database + ingestiondatabase (vector database) and we are going to create data ingestion pipeline here)

There will be two important piplines that will be created Here, we are trying to optimize the pipeline that we are creating


RAG + external vector database + ingestion