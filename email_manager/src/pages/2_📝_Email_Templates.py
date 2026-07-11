import streamlit as st

from db.db import DatabaseManager

db = DatabaseManager()

st.title("📝 Email Templates")
st.write("Create and manage your email templates.")

with st.form("add_template_form", clear_on_submit=True):
    name = st.text_input("Template Name")

    body = st.text_area(
        "Template Body",
        height=200,
        placeholder="Write your email template here...",
    )

    submitted = st.form_submit_button("Add Template")

    if submitted:
        if not name or not body:
            st.error("Template name and body are required.")
        else:
            template_id = db.add_template(name, body)
            st.success(f"Template #{template_id} added successfully!")
            st.rerun()

st.divider()

st.subheader("Saved Templates")

templates = db.get_all_templates()

if not templates:
    st.info("No templates found.")
else:
    for template in templates:
        with st.container(border=True):
            col1, col2 = st.columns([5, 1])

            with col1:
                st.write(f"### {template['name']}")
                st.text(template["body"])

            with col2:
                if st.button(
                    "🗑️ Delete",
                    key=f"delete_template_{template.doc_id}",
                    type="primary",
                ):
                    db.delete_template(template.doc_id)
                    st.success("Template deleted successfully!")
                    st.rerun()
