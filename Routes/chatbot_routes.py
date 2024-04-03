from flask import request, Response, Blueprint

import Controllers

chatbot = Blueprint('chatbot', __name__)

@chatbot.route('/chat', methods=['POST'])
def chat() -> Response:
  return Controllers.chat()

