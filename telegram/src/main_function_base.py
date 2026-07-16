import telebot
from src.config import ADMINS, BOT_TOKEN, VALID_GROUPS

bot = telebot.TeleBot(BOT_TOKEN, parse_mode="HTML")


def is_admin_reply(message) -> bool:
    """Return True if an admin replies inside a valid group"""
    username = (message.from_user.username or "").lower()
    chat = (message.chat.username or "").lower()

    return (
        (message.reply_to_message is not None)
        and username in ADMINS
        and chat in VALID_GROUPS
    )


@bot.message_handler(commands=["start", "help"])
def send_welcome(message):
    bot.reply_to(message, "Hi, how are you doing?")


@bot.message_handler(func=is_admin_reply)
def echo_all(message):
    bot.reply_to(
        message,
        f"You are replying to a message.\n\nYour reply: {message.text}",
    )


if __name__ == "__main__":
    print("Bot is running...")
    bot.infinity_polling()
