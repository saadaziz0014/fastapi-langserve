from streamlit import streamlit as st
import requests
st.title("Langchain Server")

title=st.text_input("Title")

def callAPI(title):
    response = requests.post("http://localhost:8000/tale/invoke", json={"input": {"title": title}})
    print(response.json())
    return response.json()["output"]


if title:
    output = callAPI(title)
    st.write(output)