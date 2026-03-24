# importar as bibliotecas

import streamlit as st
import os
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate



st.set_page_config(
    page_title="UNIVILLE IA",
    layout="centered"
)

# Criar o meu Titulo
st.title("My Chat-IA")


with st.sidebar:

    st.markdown("##  Configurações")
    st.markdown("---")

    groq_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="API_...",
        help="Crie sua chave em console.groq.com/keys"
    )

# Gera a separação entre as interfaces

st.markdown("---")

contexto = st.text_area(
        "Contexto do Assistente",
        value="Você é um assistente acadêmico da Univille especialista em Inteligência Artificial. "
              "Explique conceitos de forma clara, didática e em português.",
        height=150
    )

modelo = st.selectbox(
        "Modelo Groq",
        [
            "llama-3.3-70b-versatile",
            "llama3-8b-8192",
            "mixtral-8x7b-32768"
        ]
    )