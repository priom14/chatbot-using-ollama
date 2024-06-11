from langchain_core.output_parsers import StrOutputParser
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.llms import Ollama

import streamlit as st
import os
from dotenv import load_dotenv

os.environ["LANGCHAIN_TRACING_V2"] = "true"
os.environ["LANGCHAIN_ENDPOINT"]="https://api.smith.langchain.com"
os.environ["LANGCHAIN_API_KEY"] = os.getenv("LANGCHAIN_API_KEY")
os.environ["LANGCHAIN_PROJECT"] = os.getenv("LANGCHAIN_PROJECT")

##PROMPT TEMPLATE

system_template = "Hi I'm your personal assisnant. How can I help You"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', 'Question: {question}')
])
## Streamlit Framework


st.title("Langchain testing with OLLAMA")
input_text = st.text_input("Search the topic you want")

## Ollama LLM

model = Ollama(model = 'llama3')
output_parser = StrOutputParser()
chain = prompt_template|model|output_parser

if input_text:
    st.write(chain.invoke({'question': input_text}))

