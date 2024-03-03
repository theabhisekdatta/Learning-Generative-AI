# Integrate the code to openai API

import os
from constant import openai_key
from langchain_openai import ChatOpenAI


import streamlit as st


os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework

st.title("LangChain First connection  with OpenAI")
input_text = st.text_input("Search the topic you want")

# OpenAI LLMs

llm = ChatOpenAI(temperature=0.8)

if input_text:
    st.write(llm.invoke(input_text))
