from .auth import auth_blueprint
from .chat import chat_blueprint


def init_app(app):
    app.register_blueprint(auth_blueprint)
    app.register_blueprint(chat_blueprint)
