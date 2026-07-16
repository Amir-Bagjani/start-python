from typing import Any, cast

from tinydb import Query, TinyDB


class DatabaseManager:
    def __init__(self, db_path: str = "messages.json"):
        self.db = TinyDB(db_path)
        self.messages = self.db.table("messages")

    def save_message(self, message_data: dict) -> int:
        return self.messages.insert(message_data)

    def get_message(
        self,
        chat_id: int,
        message_id: int,
    ) -> str | None:
        Message = Query()

        result = self.messages.get(
            (Message.chat_id == chat_id) & (Message.message_id == message_id)
        )

        if result is None:
            return None

        result = cast(dict[str, Any], result)

        return result.get("text")
