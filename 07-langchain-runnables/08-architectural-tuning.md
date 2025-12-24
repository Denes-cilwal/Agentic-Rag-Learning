
# LangChain Architectural Tuning: From Chains to Runnables

---

## 1️⃣ The problem LangChain created for itself

Early LangChain tried to standardize everything by creating many components:

LLMChain

RetrievalQA

ConversationalRetrievalChain

RouterChain

TransformChain

SequentialChain

MultiPromptChain

…and many more

What went wrong?

Too many classes

Too many abstractions

# LangChain Architectural Tuning: From Chains to Runnables

---

## 1️⃣ The Problem LangChain Created for Itself

Early LangChain tried to standardize everything by creating many components:

* `LLMChain`
* `RetrievalQA`
* `ConversationalRetrievalChain`
* `RouterChain`
* `TransformChain`
* `SequentialChain`
* `MultiPromptChain`
* ...and many more

**What went wrong?**

- Too many classes
- Too many abstractions
- Hard to customize
- Hard to compose
- Hard to debug
- Users had to learn LangChain, not just build AI apps

So LangChain recreated the same problem it was trying to solve:

> "Too many chains"

---

## 2️⃣ The Insight: Everything is the Same Shape

LangChain authors realized something very important:

Every AI step is just: `input → output`

**Examples:**

- `PromptTemplate`: `dict → string`
- `Retriever`: `string → documents`
- `LLM`: `string → string`
- `OutputParser`: `string → structured data`
- `Tool`: `input → output`

So instead of many types of chains, they needed one universal abstraction.

---

## 3️⃣ Enter: Runnables 🧠

**What is a Runnable?**

A Runnable is:

> Anything that takes an input and produces an output

That’s it. No special meaning.

**Formally:**

`Runnable[I, O]`

**Examples:**

- `Runnable[str, list[Document]]` → retriever
- `Runnable[dict, str]` → prompt
- `Runnable[str, str]` → LLM
- `Runnable[str, Any]` → parser

---

## 4️⃣ Why Runnables Solve “Too Many Components”

Instead of this 👎:

* `LLMChain`
* `RetrievalQA`
* `StuffDocumentsChain`
* `MapReduceChain`
* `SequentialChain`

They now have this 👍:

* Runnable + composition

Everything becomes:

- simple
- composable
- debuggable
- reusable
- No special classes per use case

---

## 5️⃣ How Composition Works (This is the Key)

Runnables can be chained using operators:

**Pipe (`|`) operator**

```python
prompt | llm | parser
```

Means:

```python
output = parser(llm(prompt(input)))
```

This replaces `LLMChain` entirely.

---

## 6️⃣ RAG Expressed with Runnables (Matches Your Diagram)

Your manual RAG flow:

```
query
 → retriever
 → format docs
 → prompt
 → LLM
 → answer
```

Runnable version:

```python
chain = (
    {
        "context": retriever | format_docs,
        "question": RunnablePassthrough()
    }
    | prompt
    | llm
    | parser
)
```

No special “RAG chain” class. Just composition.

---

## 7️⃣ Why This is Better Than Old Chains

**Old way (rigid):**

- Behavior hidden inside classes
- Hard to inject logic
- Hard to debug intermediate outputs

**Runnable way (transparent):**

- Every step visible
- Every step testable
- Swap any part easily
- Works for all AI workflows

---

## 8️⃣ Intent Detection Example (from Your Diagram)

**Old approach:**

- Custom intent chain
- Custom router chain
- Custom glue

**Runnable approach:**

```python
intent_chain = intent_prompt | llm | parser

router = RunnableBranch(
    (is_search, search_chain),
    (is_chat, chat_chain),
    default_chain
)
```

Intent routing is now just another runnable.

---

## 9️⃣ Mental Model Shift (Very Important)

**Before:**

> “Which LangChain class should I use?”

**Now:**

> “How do I compose Runnables?”

LangChain stopped being a framework and became a composition layer.