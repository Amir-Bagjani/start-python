import streamlit as st
from constants import RESUME_SCHEME_PROMPT
from llm_interface import ask_ai
from PyPDF2 import PdfReader


def extract_pdf_text(pdf_file) -> str:
    reader = PdfReader(pdf_file)

    resume_text = ""
    for page in reader.pages:
        resume_text += page.extract_text() or ""

    return resume_text


st.set_page_config(page_title="Resume Parser", page_icon="📄")

st.title("📄 Resume Parser")

uploaded_file = st.file_uploader(
    "Upload your resume (PDF)",
    type=["pdf"],
)

if uploaded_file:
    st.success(f"Selected: {uploaded_file.name}")

    if st.button("Generate"):
        with st.spinner("Loading..."):
            resume_text = extract_pdf_text(uploaded_file)

            prompt = f"{RESUME_SCHEME_PROMPT}\n\n{resume_text}"

            response = ask_ai(prompt)

        st.subheader("AI Response")

        st.code(
            response,
            # language="json",  # اگر خروجی JSON است
        )
