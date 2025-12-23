# LangChain Chains: From Manual Coding to Chaining

In early LLM development, building applications required a lot of manual "glue code." Developers had to:

- Manually pass outputs from one function to the next
- Strip away metadata from model responses
- Format prompts before sending them to the model
- Rewrite logic to insert new steps (like output parsers) into the pipeline

This manual approach quickly becomes unmanageable for complex applications.

## The Problem with Manual Flows

- **Handling Metadata:** Each call to `llm.invoke()` returns an object (like `AIMessage`) with metadata. You must manually extract the content.
- **Prompt Formatting:** You have to call `.format()` on your prompt templates before passing them to the model.
- **Brittleness:** Adding new steps (e.g., output parsers) requires rewriting your code, making it hard to maintain.

## How LangChain Solves This

LangChain introduces the **LangChain Expression Language (LCEL)** and the **pipe operator (`|`)** to build chains. This allows you to:

- Connect components (prompts, models, parsers) in a pipeline
- Automatically handle formatting and metadata
- Easily insert or remove steps without rewriting your logic

**Result:** Cleaner, more maintainable, and scalable LLM applications.

---

Manual way:

```python
# Step 1: Format
formatted_prompt = template.format(topic="Space")
# Step 2: Invoke Model
response = model.invoke(formatted_prompt)
# Step 3: Extract
final_text = response.content

```
