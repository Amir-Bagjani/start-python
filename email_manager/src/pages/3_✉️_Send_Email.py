from datetime import datetime

import streamlit as st

from db.db import DatabaseManager

db = DatabaseManager()

st.title("✉️ Send Email")

profiles = db.get_all_profiles()
templates = db.get_all_templates()
user = db.get_user_profile()

if not profiles:
    st.warning("Please create at least one profile first.")
    st.stop()

if not templates:
    st.warning("Please create at least one email template first.")
    st.stop()

# -------------------------------------------------------------------
# Top Section
# -------------------------------------------------------------------

selected_profiles = st.multiselect(
    "Recipients",
    options=profiles,
    format_func=lambda p: f"{p['name']} <{p['email']}>",
)

selected_template = st.selectbox(
    "Template",
    options=templates,
    format_func=lambda t: t["name"],
)

subject = st.text_input("Subject")

include_signature = st.toggle(
    "Include Signature",
    value=True,
)

# -------------------------------------------------------------------
# Build Preview
# -------------------------------------------------------------------

raw_body = selected_template["body"]


def inject_variables(body: str, recipient):
    result = body

    variables = {
        "{{name}}": recipient.get("name", ""),
        "{{email}}": recipient.get("email", ""),
        "{{recipient_title}}": recipient.get("title", ""),
        "{{recipient_profession}}": recipient.get("profession", ""),
        "{{my_name}}": user.get("name", "") if user else "",
        "{{my_title}}": user.get("title", "") if user else "",
        "{{my_degree}}": user.get("degree", "") if user else "",
        "{{my_profession}}": user.get("profession", "") if user else "",
        "{{my_university}}": user.get("university", "") if user else "",
        "{{github}}": user.get("github", "") if user else "",
        "{{linkedin}}": user.get("linkedin", "") if user else "",
        "{{x}}": user.get("x", "") if user else "",
        "{{website}}": user.get("website", "") if user else "",
    }

    for key, value in variables.items():
        result = result.replace(key, value)

    if include_signature and user and user.get("signature"):
        result += "\n\n" + user["signature"]

    return result


preview = ""

if selected_profiles:
    preview = inject_variables(raw_body, selected_profiles[0])

# -------------------------------------------------------------------
# Body / Preview
# -------------------------------------------------------------------

left, right = st.columns(2)

with left:
    st.subheader("Raw Template")

    st.text_area(
        "",
        value=raw_body,
        height=500,
        disabled=True,
    )

with right:
    st.subheader("Preview")

    st.markdown(
        f"""
<div style="border:1px solid #DDD;padding:15px;border-radius:8px;height:500px;overflow:auto;">
<pre style="white-space:pre-wrap;font-family:inherit;">{preview}</pre>
</div>
""",
        unsafe_allow_html=True,
    )

# -------------------------------------------------------------------
# Bottom Actions
# -------------------------------------------------------------------

st.divider()

col1, col2, col3 = st.columns(3)

# --------------------------------------------------------
# Send Now
# --------------------------------------------------------

with col1:
    if st.button(
        "📨 Send Now",
        use_container_width=True,
    ):
        if not selected_profiles:
            st.error("Select at least one recipient.")
        else:
            for recipient in selected_profiles:
                body = inject_variables(raw_body, recipient)

                db.add_sent_emails(
                    recipient=recipient["email"],
                    subject=subject,
                    body=body,
                    sent_date=datetime.now(),
                )

            st.success(f"{len(selected_profiles)} email(s) added to sent emails.")

# --------------------------------------------------------
# Schedule
# --------------------------------------------------------

with col2:
    schedule_time = st.datetime_input(
        "Schedule Time",
        value=datetime.now(),
    )

    if st.button(
        "📅 Schedule",
        use_container_width=True,
    ):
        if not selected_profiles:
            st.error("Select at least one recipient.")
        else:
            for recipient in selected_profiles:
                body = inject_variables(raw_body, recipient)

                db.add_schedule(
                    recipient=recipient["email"],
                    subject=subject,
                    body=body,
                    schedule_date=schedule_time,
                )

            st.success(f"{len(selected_profiles)} email(s) scheduled.")

# --------------------------------------------------------
# Reminder
# --------------------------------------------------------

with col3:
    reminder_time = st.datetime_input(
        "Reminder Time",
        value=datetime.now(),
        key="reminder",
    )

    if st.button(
        "⏰ Add Reminder",
        use_container_width=True,
    ):
        if not selected_profiles:
            st.error("Select at least one recipient.")
        else:
            for recipient in selected_profiles:
                body = inject_variables(raw_body, recipient)

                db.add_reminder(
                    recipient=recipient["email"],
                    subject=subject,
                    body=body,
                    reminder_date=reminder_time,
                )

            st.success(f"{len(selected_profiles)} reminder(s) created.")
