import streamlit as st

st.set_page_config(
    page_title="Email Management System",
    page_icon="📧",
    layout="wide",
)

st.title("📧 Email Management System")

st.write("Here you'll see an overview of your email activity and statistics.")

st.subheader("Recent Emails")

st.table(
    {
        "Recipient": ["John Doe", "Jane Smith"],
        "Subject": ["Meeting Tomorrow", "Project Update"],
        "Date": ["2026-07-10", "2026-07-09"],
    }
)

st.subheader("Statistics")

col1, col2, col3 = st.columns(3)

col1.metric("Emails Sent", "50")
col2.metric("Open Rate", "75%")
col3.metric("Response Rate", "40%")
