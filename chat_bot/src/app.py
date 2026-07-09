import streamlit as st
from src.utils.utils import chat

st.title("Wellcome to KHANDANG chat bot")
st.subheader("What's in your mind today, retard")

if "messages" not in st.session_state:
    st.session_state["messages"] = [{"role": "user", "content": "How can i help you?"}]


for msg in st.session_state.messages:
    st.chat_message(msg["role"]).write(msg["content"])


if prompt := st.chat_input():

    st.session_state.messages.append({"role": "user", "content": prompt})
    st.chat_message("user").write(prompt)

    with st.spinner("Generating response..."):
        msg = chat(prompt)

    st.session_state.messages.append({"role": "assistant", "content": msg})
    st.chat_message("assistant").write(msg)
