# importar as bibliotecas
import streamlit as st
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate

# Configuração da página
st.set_page_config(
    page_title="UNIVILLE IA",
    layout="centered"
)

# ====== ESTILO CUSTOMIZADO ======
st.markdown("""
    <style>
        .main {
            background-color: #0e1117;
        }
        .stTextInput>div>div>input {
            border-radius: 10px;
        }
        .stTextArea textarea {
            border-radius: 10px;
        }
        .stButton button {
            border-radius: 10px;
            background-color: #4CAF50;
            color: white;
            font-weight: bold;
        }
        .chat-box {
            padding: 12px;
            border-radius: 10px;
            margin-bottom: 10px;
        }
        .user {
            background-color: #1f77b4;
            color: white;
            text-align: right;
        }
        .bot {
            background-color: #2ca02c;
            color: white;
        }
    </style>
""", unsafe_allow_html=True)

# ====== TÍTULO ======
st.title("🤖 UNIVILLE Chat-IA")

# ====== SIDEBAR ======
with st.sidebar:
    st.markdown("## ⚙️ Configurações")
    st.markdown("---")

    groq_key = st.text_input(
        "Groq API Key",
        type="password",
        placeholder="API_...",
        help="Crie sua chave em console.groq.com/keys"
    )

    st.markdown("---")

    if st.button("🗑️ Limpar conversa"):
        st.session_state.messages = []

# ====== CONTEXTO ======
st.markdown("---")

contexto = st.text_area(
    "🧠 Contexto do Assistente",
    value="Você é um assistente acadêmico da Univille especialista em Inteligência Artificial. "
          "Explique conceitos de forma clara, didática e em português.",
    height=120
)

modelo = st.selectbox(
    "🤖 Modelo Groq",
    [
        "llama-3.3-70b-versatile",
        "llama3-8b-8192",
        "mixtral-8x7b-32768"
    ]
)

# ====== MEMÓRIA ======
if "messages" not in st.session_state:
    st.session_state.messages = []

# ====== MENSAGEM INICIAL ======
if not st.session_state.messages:
    st.info("👋 Olá! Sou seu assistente de IA da Univille. Pergunte algo!")

# ====== SUGESTÕES ======
st.markdown("### 💡 Sugestões rápidas")

col1, col2 = st.columns(2)

if col1.button("O que é Machine Learning?"):
    st.session_state.messages.append({
        "role": "user",
        "content": "O que é Machine Learning?"
    })

if col2.button("Explique redes neurais"):
    st.session_state.messages.append({
        "role": "user",
        "content": "Explique redes neurais"
    })

# ====== INPUT DO USUÁRIO ======
user_input = st.chat_input("Digite sua pergunta...")

if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})

# ====== PROCESSAMENTO ======
if st.session_state.messages and groq_key:

    ultima_msg = st.session_state.messages[-1]

    if ultima_msg["role"] == "user":

        llm = ChatGroq(
            api_key=groq_key,
            model=modelo
        )

        prompt = ChatPromptTemplate.from_messages([
            ("system", contexto),
            ("human", "{input}")
        ])

        chain = prompt | llm

        with st.spinner("Pensando... 🤔"):
            resposta = chain.invoke({"input": ultima_msg["content"]})

        st.session_state.messages.append({
            "role": "assistant",
            "content": resposta.content
        })

# ====== EXIBIÇÃO DO CHAT ======
for msg in st.session_state.messages:
    if msg["role"] == "user":
        st.markdown(f"""
            <div class="chat-box user">
                👤 {msg["content"]}
            </div>
        """, unsafe_allow_html=True)
    else:
        st.markdown(f"""
            <div class="chat-box bot">
                🤖 {msg["content"]}
            </div>
        """, unsafe_allow_html=True)