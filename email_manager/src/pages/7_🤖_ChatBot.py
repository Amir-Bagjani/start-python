import streamlit as st

st.title("🤖 ChatBot")
msg=st.chat_input("Ask something")
if msg:
    st.chat_message("user").write(msg)
    st.chat_message("assistant").write("Hello! I'm your email assistant.")
