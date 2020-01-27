import logging

from flask import Blueprint, abort, jsonify

from fizzbuzz.models import Chat
from fizzbuzz.schemes import ChatAPISchema
from fizzbuzz.annotations import login_required

chat_blueprint = Blueprint("chats", __name__, url_prefix="/chats")
logger = logging.getLogger(__name__)


@chat_blueprint.route("/all", methods=["GET"])
@login_required
def get_chats():
    try:
        chats = Chat.query.all()
        schema = ChatAPISchema(many=True)
        result = schema.dump(chats)
        return jsonify(result), 200
    except Exception:
        abort(404, description="Resource not found")


@chat_blueprint.route("/<int:id>", methods=["GET"])
@login_required
def get_one_chat(id: int):
    try:
        chat = Chat.query.filter_by(id=id).first()
        schema = ChatAPISchema()
        result = schema.dump(chat)
        return jsonify(result), 200
    except Exception:
        abort(404, description="Resource not found")
