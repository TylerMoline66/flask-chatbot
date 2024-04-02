import Controllers
from flask import Blueprint

static_blueprint = Blueprint("static_blueprint", __name__)

@static_blueprint.route("/")
@static_blueprint.route("/home")
def homework():
  return Controllers.home()

@static_blueprint.route("/chats")
def previous_chats():
  return Controllers.previous_chats()