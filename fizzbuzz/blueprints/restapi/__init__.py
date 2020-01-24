from .auth import auth_blueprint
from .chat import chat_blueprint
from .bot import bot_blueprint


def init_app(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(chat_blueprint)
    app.register_blueprint(bot_blueprint)
