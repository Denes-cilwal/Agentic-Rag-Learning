# RAG Context: README

## Overview

Retrieval-Augmented Generation (RAG) uses a vector database to fetch the most relevant pieces of your original data (text chunks) that are semantically similar to the user’s query. These retrieved chunks are called context and are injected into the LLM prompt to produce accurate, grounded answers.

## One-line Summary

Context is the most relevant text retrieved from your data using semantic similarity, and it is injected into the LLM prompt to produce accurate, non-hallucinated answers.

## Table of Contents

- What is “Context”?
- What does Context contain?
- How Context is created (step-by-step)
- Example
- How the LLM uses Context
- Why Context is critical
- What Context is NOT
- Typical structure of Context (real systems)
- FAQ: Do vector stores only store numbers?
- Further topics

## What is “Context”?

Context = retrieved knowledge that the LLM did not learn during training, but needs at inference time to answer correctly.

## What does Context contain?

- Text chunks (paragraphs, sections, rows)
- Metadata (source, page number, document name, timestamp)
- Similarity scores (sometimes)

## How Context is created (step-by-step)

1. Your data is ingested.
2. Documents are chunked.
3. Each chunk is converted to embeddings.
4. Embeddings are stored in a vector database.
5. User sends a query.
6. Query is converted to an embedding.
7. Vector DB performs similarity search (compares query embedding with stored embeddings).
8. Finds top-k most similar chunks.
9. Vector DB returns these top-k chunks as context.

## Example

### Stored data (in vector DB)

- Chunk 1: "Employees are entitled to 20 paid leaves per year."
- Chunk 2: "Casual leave can be taken for personal reasons."
- Chunk 3: "Sick leave requires medical documentation after 2 days."

### User query

"What is the leave policy?"

### Vector DB returns (context)

1. Employees are entitled to 20 paid leaves per year.
2. Casual leave can be taken for personal reasons.
3. Sick leave requires medical documentation after 2 days.

## How the LLM uses Context

The final prompt conceptually looks like:

```
System:
You are an assistant. Answer only using the given context.

Context:
Employees are entitled to 20 paid leaves per year.
Casual leave can be taken for personal reasons.
Sick leave requires medical documentation after 2 days.

User Question:
What is the leave policy?
```

➡️ The LLM generates an answer only from the provided context.

## Why Context is critical

1. Reduces hallucination — the LLM reads instead of guessing.
2. Enables private/internal knowledge — company policies aren’t part of pretraining.
3. Handles up-to-date data — no retraining needed when data changes.

## What Context is NOT

- Not the embedding vectors
- Not raw database rows
- Not model training data

✅ It is human-readable text retrieved using embeddings.

## Typical structure of Context (real systems)

```json
[
  {
    "text": "Employees are entitled to 20 paid leaves per year.",
    "source": "HR_policy.pdf",
    "page": 3,
    "score": 0.92
  },
  {
    "text": "Casual leave can be taken for personal reasons.",
    "source": "HR_policy.pdf",
    "page": 4,
    "score": 0.89
  }
]
```

## FAQ: Do vector stores only store numbers?

Short answer: A vector DB stores numeric vectors plus a reference to the original text, and it returns the original text as context.

### What a vector DB actually stores

Conceptually, each record includes an embedding, the original chunk text, and metadata:

```json
{
  "embedding": [0.021, -0.87, 0.44],
  "text": "Employees are entitled to 20 paid leaves per year.",
  "metadata": {
    "source": "HR_policy.pdf",
    "page": 3
  }
}
```

### Why numeric data is needed

- Numeric vectors are used for similarity search only.
- Query → embedding (numeric).
- Vector DB compares numbers vs. numbers and finds nearest vectors (e.g., cosine similarity).
- After finding nearest vectors, the DB returns the original text chunks (and optional metadata) as context — not the raw vectors.

## Further topics

- How many chunks to return (top-k)
- Bad vs. good context examples
- Context window limits and truncation
- Production prompt templates for RAG

In RAG (Retrieval-Augmented Generation), the context returned by a vector database is:

The most relevant pieces of your original data (text chunks) that are semantically similar to the user’s query.

What exactly is “context”?

Context = retrieved knowledge that the LLM did not learn during training, but needs at inference time to answer correctly.

It usually contains:

Text chunks (paragraphs, sections, rows)

Metadata (source, page number, document name, timestamp)

Similarity scores (sometimes)

How the context is created (step-by-step)

Your data was ingested earlier

Documents → chunked

Each chunk → converted to embeddings

Stored in a vector DB

User sends a query

Query → converted to an embedding

Vector DB performs similarity search

Compares query embedding with stored embeddings

Finds top-k most similar chunks

Vector DB returns context

These top-k chunks are returned as context

Example (very important)
Stored data (in vector DB)
Chunk 1: "Employees are entitled to 20 paid leaves per year."
Chunk 2: "Casual leave can be taken for personal reasons."
Chunk 3: "Sick leave requires medical documentation after 2 days."

User query
"What is the leave policy?"

Vector DB returns (context)
Context:

1. Employees are entitled to 20 paid leaves per year.
2. Casual leave can be taken for personal reasons.
3. Sick leave requires medical documentation after 2 days.

This context is then sent to the LLM.

How context is used by the LLM

The final prompt looks like this (conceptually):

System:
You are an assistant. Answer only using the given context.

Context:
Employees are entitled to 20 paid leaves per year.
Casual leave can be taken for personal reasons.
Sick leave requires medical documentation after 2 days.

User Question:
What is the leave policy?

➡️ LLM generates an answer only from the context, not from imagination.

Why context is critical

1. Reduces hallucination

LLM no longer “guesses” — it reads.

2. Enables private / internal knowledge

LLM never saw your company policies during training.

3. Handles up-to-date data

No retraining needed when data changes.

What context is NOT

❌ Not the embedding vectors
❌ Not raw database rows
❌ Not model training data

✅ It is human-readable text retrieved using embeddings.

Typical structure of context (real systems)
[
{
"text": "Employees are entitled to 20 paid leaves per year.",
"source": "HR_policy.pdf",
"page": 3,
"score": 0.92
},
{
"text": "Casual leave can be taken for personal reasons.",
"source": "HR_policy.pdf",
"page": 4,
"score": 0.89
}
]

One-line summary

Context is the most relevant text retrieved from your data using semantic similarity, and it is injected into the LLM prompt to produce accurate, non-hallucinated answers.

If you want, I can also:

Explain how many chunks to return (top-k)

Show bad vs good context examples

Explain context window limits & truncation

Show production prompt template for RAG

Just tell me 👍

but vector stores numeric data right

Yes — you’re absolutely right 👍
A vector store stores numeric data, but that is only half of the story.

Let’s make this very clear and precise, because this is the most common confusion in RAG.

Short answer (one line)

Vector DB stores numeric vectors plus a reference to the original text, and it returns the original text as context.

What a vector DB actually stores

A vector database does NOT store only numbers in isolation.

Each record looks conceptually like this:

{
embedding: [0.021, -0.87, 0.44, ...], // numeric vector
text: "Employees are entitled to 20 paid leaves per year",
metadata: {
source: "HR_policy.pdf",
page: 3
}
}

So internally it stores:

✅ Embedding vector (numeric)

✅ Original chunk text

✅ Metadata

Why numeric data is needed

Numeric vectors are needed only for similarity search.

When a query comes in:

Query → embedding (numeric)

Vector DB compares numbers vs numbers

Finds nearest vectors (cosine similarity, etc.)

👉 This part is pure math, no text involved.

What happens after similarity search

Once the closest vectors are found:

Vector DB does NOT return vectors to the LLM

Vector DB returns:

the original text chunks

optional metadata

That returned text is called context.
