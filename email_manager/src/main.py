from pathlib import Path

from dotenv import load_dotenv
from src.utils.helpers import send_mail
from src.db.db import DatabaseManager

load_dotenv(Path(__file__).resolve().parents[1] / ".env")


def main():
    # print(
    #     send_mail(
    #         to="amirbagjani@gmail.com",
    #         subject="Test",
    #         content="<p>Attached files.</p>",
    #         attachments=["esfand.xlsx", "book.pptx"],
    #     )
    # )
    pass


if __name__ == "__main__":
    main()
