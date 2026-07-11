import streamlit as st

from db.db import DatabaseManager

db = DatabaseManager()

st.title("👤 User Profile")

profile = db.get_user_profile()

with st.form("user_profile_form"):
    st.subheader("Basic Information")

    col1, col2 = st.columns(2)

    with col1:
        title = st.text_input(
            "Title",
            value=profile["title"] if profile else "",
        )

        degree = st.text_input(
            "Degree",
            value=profile["degree"] if profile else "",
            placeholder="M.Sc. Computer Science",
        )

        university = st.text_input(
            "University",
            value=profile["university"] if profile else "",
        )

    with col2:
        name = st.text_input(
            "Name",
            value=profile["name"] if profile else "",
        )

        profession = st.text_input(
            "Profession",
            value=profile["profession"] if profile else "",
            placeholder="Software Engineer",
        )

    st.divider()

    st.subheader("Social Media")

    col1, col2 = st.columns(2)

    with col1:
        github = st.text_input(
            "GitHub",
            value=profile["github"] if profile else "",
            placeholder="https://github.com/username",
        )

        linkedin = st.text_input(
            "LinkedIn",
            value=profile["linkedin"] if profile else "",
            placeholder="https://linkedin.com/in/username",
        )

    with col2:
        x = st.text_input(
            "X (Twitter)",
            value=profile["x"] if profile else "",
            placeholder="https://x.com/username",
        )

        website = st.text_input(
            "Personal Website",
            value=profile["website"] if profile else "",
            placeholder="https://example.com",
        )

    st.divider()

    st.subheader("Email Signature")

    signature = st.text_area(
        "Signature",
        value=profile["signature"] if profile else "",
        height=180,
        placeholder="Kind regards,\nJohn Doe\nSoftware Engineer",
    )

    submitted = st.form_submit_button(
        "💾 Save Profile",
        use_container_width=True,
    )

    if submitted:
        if not name.strip():
            st.error("Name is required.")
        else:
            db.update_user_profile(
                title=title,
                name=name,
                degree=degree,
                profession=profession,
                university=university,
                github=github,
                linkedin=linkedin,
                x=x,
                website=website,
                signature=signature,
            )

            st.success("Profile saved successfully!")
            st.rerun()

st.divider()

profile = db.get_user_profile()

if profile:
    st.subheader("Preview")

    col1, col2 = st.columns([2, 1])

    with col1:
        st.markdown(f"## {profile['name']}")

        if profile["title"]:
            st.write(profile["title"])

        if profile["degree"]:
            st.write(f"🎓 **Degree:** {profile['degree']}")

        if profile["profession"]:
            st.write(f"💼 **Profession:** {profile['profession']}")

        if profile["university"]:
            st.write(f"🏫 **University:** {profile['university']}")

    with col2:
        st.markdown("### 🌐 Social Links")

        if profile["github"]:
            st.markdown(f"**GitHub**  \n{profile['github']}")

        if profile["linkedin"]:
            st.markdown(f"**LinkedIn**  \n{profile['linkedin']}")

        if profile["x"]:
            st.markdown(f"**X**  \n{profile['x']}")

        if profile["website"]:
            st.markdown(f"**Website**  \n{profile['website']}")

    if profile["signature"]:
        st.divider()
        st.subheader("Email Signature")
        st.code(profile["signature"], language="text")
