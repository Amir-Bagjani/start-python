from datetime import date
from pathlib import Path

from tinydb import Query, TinyDB


class DatabaseManager:
    def __init__(self, db_path: str | Path = "email_manager.json"):
        self.db = TinyDB(db_path)
        self.profiles = self.db.table("profiles")
        self.user_profile = self.db.table("user_profiles")
        self.templates = self.db.table("templates")
        self.sent_emails = self.db.table("sent_emails")
        self.reminders = self.db.table("reminders")
        self.schedules = self.db.table("schedules")

    # profiles
    def add_profile(self, name: str, email: str, title: str, profession: str):
        return self.profiles.insert(
            {
                "name": name,
                "email": email,
                "title": title,
                "profession": profession,
            }
        )

    def get_profile(self, profile_id: int):
        return self.profiles.get(doc_id=profile_id)

    def update_profile(
        self, profile_id: int, name: str, email: str, title: str, profession: str
    ):
        return self.profiles.update(
            doc_ids=[profile_id],
            fields={
                "name": name,
                "email": email,
                "title": title,
                "profession": profession,
            },
        )

    def delete_profile(self, profile_id: int):
        return self.profiles.remove(doc_ids=[profile_id])

    def get_all_profiles(self):
        return self.profiles.all()

    # email template managers
    def add_template(self, name: str, body: str):
        return self.templates.insert(
            {
                "name": name,
                "body": body,
            }
        )

    def get_template(self, template_id: int):
        return self.templates.get(doc_id=template_id)

    def update_template(self, template_id: int, name: str, body: str):
        return self.templates.update(
            doc_ids=[template_id],
            fields={
                "name": name,
                "body": body,
            },
        )

    def delete_template(self, template_id: int):
        return self.templates.remove(doc_ids=[template_id])

    def get_all_templates(self):
        return self.templates.all()

    # sent emails managers
    def add_sent_emails(self, recipient: str, subject: str, body: str, sent_date: date):
        return self.sent_emails.insert(
            {
                "recipient": recipient,
                "subject": subject,
                "body": body,
                "sent_date": sent_date.isoformat(),
            }
        )

    def get_sent_email(self, email_id: int):
        return self.sent_emails.get(doc_id=email_id)

    def get_all_sent_emails(self):
        return self.sent_emails.all()

    # reminder managment
    def add_reminder(
        self, recipient: str, subject: str, body: str, reminder_date: date
    ):
        return self.reminders.insert(
            {
                "recipient": recipient,
                "subject": subject,
                "body": body,
                "reminder_date": reminder_date.isoformat(),
            }
        )

    def get_reminder(self, reminder_id: int):
        return self.reminders.get(doc_id=reminder_id)

    def update_reminder(self, reminder_id: int, reminder_date: date):
        return self.reminders.update(
            doc_ids=[reminder_id], fields={"reminder_date": reminder_date.isoformat()}
        )

    def delete_reminder(self, reminder_id: int):
        return self.reminders.remove(doc_ids=[reminder_id])

    def get_all_reminders(self):
        return self.reminders.all()

    # schedules managements
    def add_schedule(
        self, recipient: str, subject: str, body: str, schedule_date: date
    ):
        return self.schedules.insert(
            {
                "recipient": recipient,
                "subject": subject,
                "body": body,
                "schedule_date": schedule_date.isoformat(),
            }
        )

    def get_schedule(self, schedule_id: int):
        return self.schedules.get(doc_id=schedule_id)

    def update_schedule(self, schedule_id: int, schedule_date: date):
        return self.schedules.update(
            doc_ids=[schedule_id], fields={"schedule_date": schedule_date.isoformat()}
        )

    def delete_schedule(self, schedule_id: int):
        return self.schedules.remove(doc_ids=[schedule_id])

    def get_all_schedules(self):
        return self.schedules.all()

        # profiles

    # user profile management
    def set_user_profile(
        self,
        name: str,
        title: str,
        degree: str,
        profession: str,
        university: str,
        github: str,
        linkedin: str,
        x: str,
        website: str,
        signature: str,
    ):
        self.user_profile.truncate()

        return self.user_profile.insert(
            {
                "name": name,
                "title": title,
                "degree": degree,
                "profession": profession,
                "university": university,
                "github": github,
                "linkedin": linkedin,
                "x": x,
                "website": website,
                "signature": signature,
            }
        )

    def get_user_profile(self):
        profiles = self.user_profile.all()
        return profiles[0] if profiles else None

    def update_user_profile(
        self,
        name: str,
        title: str,
        degree: str,
        profession: str,
        university: str,
        github: str,
        linkedin: str,
        x: str,
        website: str,
        signature: str,
    ):
        profile = self.get_user_profile()

        if profile:
            self.user_profile.update(
                {
                    "name": name,
                    "title": name,
                    "degree": degree,
                    "profession": profession,
                    "university": university,
                    "github": github,
                    "linkedin": linkedin,
                    "x": x,
                    "website": website,
                    "signature": signature,
                },
                doc_ids=[profile.doc_id],
            )
        else:
            self.set_user_profile(
                name,
                title,
                degree,
                profession,
                university,
                github,
                linkedin,
                x,
                website,
                signature,
            )

    # search functionality
    def search_sent_emails(self, query: str):
        Email = Query()
        return self.sent_emails.search(
            (Email.recipient.search(query))
            | (Email.subject.search(query))
            | (Email.body.search(query))
        )
