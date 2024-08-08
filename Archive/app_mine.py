import os
from apikey import apikey
import streamlit as st # type: ignore
from langchain.llms import OpenAI

os.environ['OPENAI_API_KEY'] = apikey

st.title('YouTube GPT Creator')
prompt = st.text_input("Enter your prompt here")

llm = OpenAI(temperature = 0.9, organization = 'org-hSpTI9gy7UK4UDPOjP3o4Igv')

if prompt:
    response = llm(prompt)
    st.write(response)