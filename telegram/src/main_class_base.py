from datetime import datetime

import telebot
from src.config import ADMINS, BOT_TOKEN, VALID_GROUPS
from src.constants import WELCOME_MSG
from src.database import DatabaseManager
from src.llm import ask_ai
from telebot.types import Message, ReactionTypeEmoji


class YoooBot:
    def __init__(self):
        self.bot = telebot.TeleBot(BOT_TOKEN, parse_mode="markdown")
        self.db = DatabaseManager()
        self.setup_handlers()

    def setup_handlers(self):
        self.bot.message_handler(commands=["start", "help"])(self.send_welcome)
        self.bot.message_handler(func=lambda _: True)(self.store_messages)
        self.bot.message_handler(func=self.is_valid_admin_reply)(self.admin_reply)
        self.bot.message_reaction_handler(func=lambda update: update.new_reaction)(
            self.handle_reaction
        )

    def is_valid_admin_reply(self, message: Message) -> bool:
        """Return True if an admin replies inside a valid group"""
        if message.from_user is None or message.chat is None:
            return False

        username = (message.from_user.username or "").lower()
        chat = (message.chat.username or "").lower()

        return (
            (message.reply_to_message is not None)
            and username in ADMINS
            and chat in VALID_GROUPS
        )

    def store_messages(self, message: Message) -> None:
        data = {
            "message_id": message.message_id,
            "chat_id": message.chat.id,
            "chat_username": message.chat.username,
            "user_id": (message.from_user.id if message.from_user else None),
            "username": (message.from_user.username if message.from_user else None),
            "text": message.text,
            "date": datetime.fromtimestamp(message.date).isoformat(),
            "reply_to": (
                message.reply_to_message.message_id
                if message.reply_to_message
                else None
            ),
        }

        self.db.save_message(data)

    def send_welcome(self, message: Message) -> None:
        self.bot.reply_to(message, WELCOME_MSG)

    def admin_reply(self, message: Message) -> None:
        self.bot.reply_to(message, "test")

    def handle_reaction(self, update):
        reaction = update.new_reaction[-1]

        if isinstance(reaction, ReactionTypeEmoji):
            if reaction.emoji == "👍":
                mes = self.db.get_message(
                    chat_id=update.chat.id, message_id=update.message_id
                )

                loading_message = self.bot.send_message(
                    chat_id=update.chat.id,
                    text="wait for llm response...",
                    reply_to_message_id=update.message_id,
                )

                response = ask_ai(mes)
                if response is not None:
                    self.bot.edit_message_text(
                        chat_id=update.chat.id,
                        message_id=loading_message.message_id,
                        text=str(response),
                    )

    def run(self):
        print("Bot is running...")
        self.bot.infinity_polling(allowed_updates=["message", "message_reaction"])
