
# LangChain Runnables: LLMChain Example

This document explains the difference between manual prompt assembly and automated chaining using LangChain's `LLMChain` helper.

---

## Before: Manual Assembly

Before LangChain introduced standard wrappers, you had to act as the "middleman" for every single step in your workflow.

### Example: Simple Translator App
A translator that takes a word and translates it to French.

**Manual Steps:**
1. **Create the Prompt:** Write the string template.
2. **Format the Prompt:** Manually inject the user's word into that string.
3. **Call the LLM:** Pass that specific string to the model.
4. **Handle the Output:** Manually clean up the text the LLM returns.

**Problem:**
If you have 10 steps (like a PDF load → Split → Embed flow), you have to write 10 different manual hand-offs. It's easy to make a mistake in the middle.

---

## After: Automated Chaining with LLMChain

LangChain introduced the `LLMChain` helper, which acts like a pre-built pipeline to automate these steps.

**Benefits:**
- Reduces manual hand-offs
- Minimizes errors
- Simplifies complex workflows

---

## Summary

Manual prompt assembly is error-prone and tedious. LangChain's `LLMChain` automates the process, making it easier to build robust LLM-powered applications.