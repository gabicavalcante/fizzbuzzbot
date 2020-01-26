import telegram
import logging
from flask import Blueprint, request, jsonify
from dynaconf import settings
from fizzbuzz.models import Chat

bot_blueprint = Blueprint("bot", __name__, url_prefix="/")
logger = logging.getLogger(__name__)

bot = None
if settings.current_env != "ci":
    bot = telegram.Bot(token=settings.get("TELEGRAM_BOT_TOKEN"))


def get_response(text: str) -> str:
    try:
        number = int(text)
        return "Fizz" * (number % 3 == 0) + "Buzz" * (number % 5 == 0) or number
    except ValueError:
        return f"Hey, '{text}' is not a valid input :("


@bot_blueprint.route(f"/{settings.get('TELEGRAM_BOT_TOKEN')}", methods=["POST"])
def respond():
    # retrieve the message in JSON and then transform it to Telegram object
    update = telegram.Update.de_json(request.get_json(force=True), bot)

    chat_id = update.message.chat.id
    user = update.message.chat.username
    msg_id = update.message.message_id

    # Telegram understands UTF-8, so encode text for unicode compatibility
    text = update.message.text.encode("utf-8").decode()
    logger.info("Update received! {text}")

    response = get_response(text)

    Chat.save(user, text, response, update)
    bot.sendMessage(chat_id=chat_id, text=response, reply_to_message_id=msg_id)

    return jsonify({"message": "message send"}), 200


@bot_blueprint.route("/setwebhook", methods=["GET", "POST"])
def set_webhook():
    # we use the bot object to link the bot to our app which live
    # in the link provided by URL
    hook = "{URL}/{HOOK}".format(
        URL=settings.get("BOT_HOST"), HOOK=settings.get("TELEGRAM_BOT_TOKEN")
    )
    logger.debug(hook)
    s = bot.set_webhook(hook)

    if s:
        return jsonify({"message": "webhook setup ok"}), 200
    else:
        return jsonify({"message": "webhook setup failed"}), 200
