import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv
from langchain_core.prompts import PromptTemplate

load_dotenv()

model = ChatOpenAI(model="gpt-4o-mini", temperature=0.7, max_tokens=500)

st.header("Research Tools Prompt Interface")

paper_input = st.selectbox(
    "Select Research Paper Name",
    [
        "Attention Is All You Need",
        "BERT: Pre-training of Deep Bidirectional Transformers",
        "GPT-3: Language Models are Few-Shot Learners",
        "Diffusion Models Beat GANs on Image Synthesis",
    ],
)

style_input = st.selectbox(
    "Select Explanation Style",
    ["Beginner-Friendly", "Technical", "Code-Oriented", "Mathematical"],
)

length_input = st.selectbox(
    "Select Explanation Length",
    ["Short", "Medium", "Long"],
)

# map UI length -> clearer instruction
length_map = {
    "Short": "1–2 short paragraphs",
    "Medium": "3–5 paragraphs",
    "Long": "a detailed explanation with sections and examples",
}

prompt_template = PromptTemplate(
    input_variables=["paper", "style", "length"],
    template=(
        "You are a helpful research assistant.\n"
        "Task: Summarize the research paper titled: {paper}\n\n"
        "Writing style: {style}\n"
        "Length: {length}\n\n"
        "Include:\n"
        "1) One-sentence takeaway\n"
        "2) Problem the paper solves\n"
        "3) Key idea / method\n"
        "4) Why it matters / impact\n"
        "5) 2 limitations or open questions\n"
        "Avoid fluff. Be accurate.\n"
    ),
)

if st.button("Summarize"):
    formatted_prompt = prompt_template.format(
        paper=paper_input,
        style=style_input,
        length=length_map[length_input],
    )

    response = model.invoke(formatted_prompt)

    st.subheader("Summary:")
    st.write(response.content)
