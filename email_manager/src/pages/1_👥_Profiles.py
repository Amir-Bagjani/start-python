import streamlit as st

from db.db import DatabaseManager

db = DatabaseManager()

st.title("👥 Profiles")
st.write("Manage email profiles.")

with st.form("add_profile_form", clear_on_submit=True):
    name = st.text_input("Name")
    email = st.text_input("Email")
    title = st.text_input("Title")
    profession = st.text_input("Profession")

    submitted = st.form_submit_button("Add")

    if submitted:
        if not name or not email:
            st.error("Name and Email are required.")
        else:
            profile_id = db.add_profile(
                name=name,
                email=email,
                title=title,
                profession=profession,
            )
            st.success(f"Profile #{profile_id} added successfully!")

st.divider()

st.subheader("Profiles")

profiles = db.get_all_profiles()

if not profiles:
    st.info("No profiles found.")
else:
    for profile in profiles:
        with st.container(border=True):
            col1, col2 = st.columns([5, 1])

            with col1:
                st.write(f"**Name:** {profile['name']}")
                st.write(f"**Email:** {profile['email']}")
                st.write(f"**Title:** {profile['title']}")
                st.write(f"**Profession:** {profile['profession']}")

            with col2:
                if st.button(
                    "🗑️ Delete",
                    key=f"delete_{profile.doc_id}",
                    type="primary",
                ):
                    db.delete_profile(profile.doc_id)
                    st.success("Profile deleted successfully!")
                    st.rerun()
