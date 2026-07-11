import streamlit as st

st.title("🔍 Search")
query=st.text_input("Search")
if query:
    st.write(f"Searching for: {query}")
