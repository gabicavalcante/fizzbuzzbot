import telegram
import logging
from flask import Blueprint, request
from dynaconf import settings

bot_blueprint = Blueprint("bot", __name__, url_prefix="/bot")
logger = logging.getLogger(__name__)


def get_response() -> str:
    return "hello"


@bot_blueprint.route("/{}".format(settings.get("TELEGRAM_TOKEN")), methods=["POST"])
def respond():
    bot = telegram.Bot(token=settings.get("TELEGRAM_TOKEN"))

    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode("utf-8").decode()
    print("got text message :", text)

    response = get_response(text)
    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

    return "ok"
