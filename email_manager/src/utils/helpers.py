import os
import smtplib
from email import encoders
from email.mime.base import MIMEBase
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from pathlib import Path


def send_mail(
    to: str, subject: str, content: str, attachments=None
) -> tuple[bool, str]:
    """Send an email within sender credentials from environment varables

    Args:
        to (str or list): The email address(es) of the to(s)
        subject (str): the subject of the email
        content (str or list): The contents of the email
        attachments (str or list, optional): Path(s) to file(s) to be attached. Defaults to None.

    Returns:
        (bool, message): True if the email was sent successfully, False otherwise, message
    """

    sender_email = os.getenv("MAIL_SENDER", "")
    password = os.getenv("MAIL_PASS", "")

    if not sender_email or not password:
        return False, "MAIL_SENDER and MAIL_PASS environment variables are required."

    msg = MIMEMultipart()
    msg["From"] = sender_email
    msg["To"] = to
    msg["Subject"] = subject

    msg.attach(MIMEText(content, "html"))

    if attachments:
        if not isinstance(attachments, list):
            attachments = [attachments]

        for attachments_path in attachments:
            file_path = Path(attachments_path)

            if not file_path.exists():
                return False, f"Attachment not found: {file_path}"

            with file_path.open("rb") as file:
                attachment = MIMEBase("application", "octet-stream")
                attachment.set_payload(file.read())

            encoders.encode_base64(attachment)
            attachment.add_header(
                "Content-Disposition", f"attachment; filename={file_path.name}"
            )

            msg.attach(attachment)

    smtp_server = "smtp.gmail.com"
    port = 587

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            server.quit()

    except Exception as e:
        return False, str(e)

    return True, "Email sent successfully"
