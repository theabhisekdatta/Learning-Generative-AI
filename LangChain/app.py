from langchain_openai import ChatOpenAI
from constant import openai_key
import os
import streamlit as st
# import warnings
# warnings.filterwarnings("ignore")

os.environ["OPENAI_API_KEY"] = openai_key

# Function to load OpenAI model and get respones


def generate_response(text_ques):
    llm = ChatOpenAI(model="gpt-3.5-turbo", temperature=0.5)
    response = llm.predict(text_ques)
    return response


# Streamlit intregration
st.header("First Langchain Chatbot")

user_input = st.text_input("Give your question")

response = generate_response(user_input)

submit = st.button("Submit your Question")
if submit:
    st.subheader("The Response is ")
    st.write(response)
