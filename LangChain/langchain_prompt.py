# Integrate the code to openai API

import os
from constant import openai_key
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptTemplate

import streamlit as st


os.environ["OPENAI_API_KEY"] = openai_key

# Streamlit framework

st.title("Celebrity Search Results")
input_text = st.text_input("Search the topic you want")

# Peompt Template

prompt = ChatPromptTemplate.from_messages([
    ("system", "Tell me something about the Celebrity."),
    ("user", "{input}")
])

llm = ChatOpenAI(temperature=0.8)
chain = prompt | llm

if input_text:
    st.write(chain.invoke({"input": input_text}))
