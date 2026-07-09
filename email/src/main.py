import os
import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from src.constant import HTML_TEMPLATE
from pathlib import Path

file_path = Path(__file__).parent / "book.pptx"


def send_mail(sender: str, recipient: str, subject: str, body: str):
    html = HTML_TEMPLATE.format(
        name=recipient.split("@")[0], message=body, sender="Amir"
    )

    msg = MIMEMultipart()
    msg["Subject"] = subject or "This is test subject"
    msg["From"] = sender
    msg["To"] = recipient

    msg.attach(MIMEText(html, "html"))

    try:
        with open(file_path, "rb") as file:
            attachment = MIMEBase("application", "octet-stream")
            attachment.set_payload(file.read())
    except Exception as e:
        return False, f"An error occurred: {e}"

    encoders.encode_base64(attachment)
    attachment.add_header(
        "Content-Disposition", f"attachment; filename={file_path.name}"
    )

    msg.attach(attachment)

    smtp_server = "smtp.gmail.com"
    port = 587
    sender_email = "amirbagjani@gmail.com"
    password = os.environ.get("MAIL_PASS", "")

    try:
        with smtplib.SMTP(smtp_server, port) as server:
            server.starttls()
            server.login(sender_email, password)
            server.send_message(msg)
            server.quit()

            return True, "Email sent successfully"
    except Exception as e:
        return False, f"An error occurred: {e}"


def main():
    while True:
        recipient = input("\nEnter recipient: ").strip()
        if not recipient:
            print("This is required field!")
            continue

        subject = input(
            "\nEnter subject(defult value is 'This is test subject'): "
        ).strip()
        body = input("\nEnter message(default value is 'This is test email'): ").strip()

        is_success, msg = send_mail(
            sender="amirbagjani@gmail.com",
            recipient=recipient,
            subject=subject,
            body=body,
        )
        print(msg)

        if not is_success:
            continue

        break


if __name__ == "__main__":
    main()
