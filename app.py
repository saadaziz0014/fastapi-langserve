from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langchain_community.llms import Ollama
import streamlit as st
import os
from dotenv import load_dotenv
from fastapi import FastAPI
from langserve import add_routes

load_dotenv()

os.environ["LANGCHAIN_TRACING_V2"]="true"
os.environ["LANGCHAIN_API_KEY"]=os.getenv("LANGCHAIN_API_KEY")

model = Ollama(model="llama3.1")

prompt = ChatPromptTemplate.from_messages(
    [
        ("system", "you are heplful assistant in telling short tales. response to the following title"),
        ("human","Title:{title}")
    ]
)

app = FastAPI(
    title="Langserve",
    version="0.0.1",
    description="Langchain Server",
)

add_routes(
    app,
    prompt | model,
    path="/tale"
)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app:app", host="localhost", port=8000, reload=True)