# Embeddings – Simple Explanation

This README explains **documents, vectors, and dimensions** in an easy way.

---

## What is a "Document"?

A **document** is just a piece of text.

A document can be:

- one word
- one sentence
- many sentences
- a paragraph
- a chunk from a PDF or website

📌 **Important rule:**

> **1 document → 1 embedding vector**

---

## What is an Embedding?

An **embedding** is a way to convert text into numbers so a computer can understand the **meaning**.

Example:

```
"Delhi is the capital of India."
```

becomes something like:

```
[0.12, -0.44, 0.88, ..., 0.05]
```

These numbers together are called a **vector**.

---

## What is a Vector?

A **vector** is a list of numbers that represents the meaning of a document.

- 1 document → 1 vector
- Vectors are used to compare similarity between texts

---

## What are Dimensions?

**Dimensions** are how many numbers are in one vector.

Example:

```python
OpenAIEmbeddings(dimensions=32)
```

This means:

- Each document becomes **1 vector**
- Each vector has **32 numbers**

Even if the sentence is short or long, the vector **always has 32 numbers**.

---

## Why sentence length doesn’t matter

These all produce **1 vector of the same size**:

- "Delhi"
- "Delhi is the capital of India"
- "Delhi is the capital of India and an important city"

Meaning is compressed into fixed-size numbers.

---

## Why not use 1 dimension?

One number is not enough to describe meaning.

Multiple dimensions help capture:

- topic
- place
- relationships
- facts
- context

More dimensions = more detail.

---

## Real-world usage (RAG)

In practice:

- Large text is split into small chunks
- Each chunk becomes **one document**
- Each document becomes **one vector**
- Vectors are stored in a vector database

This allows fast and accurate search.

---

## Key Takeaways

- Document = any text chunk
- 1 document → 1 vector
- Dimensions are fixed
- Sentence length does NOT change dimensions
- Embeddings store meaning, not words

---
