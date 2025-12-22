import streamlit as st
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()



model = ChatOpenAI(model="gpt-4", temperature=0.7, max_tokens=300)
st.header("Research Tools Prompt Interface")
prompt = st.text_input("Enter your prompt:")

# this is static prompt for testing

if st.button("Submit"):
    result = model.invoke(prompt)
    st.write("Response from the model:")
    st.write(result.content)
