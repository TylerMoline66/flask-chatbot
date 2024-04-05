import uuid
from sqlalchemy.dialects.mysql import UUID
import marshmallow as ma



from db import db 

class Chat(db.Model):
    __tablename__ = "Chat"

    chat_id = db.Column(UUID(as_uuid=True), primary_key=True, default=uuid.uuid4())
    user_input = db.Column(db.String(), unique=True, nullable=False)
    ai_output = db.Column(db.String(), nullable=False, default=True)

    def __init__(self, chat_id, user_input, ai_output):
        self.chat_id = chat_id
        self.user_input = user_input
        self.ai_output = ai_output

    def get_new_chat():
        return Chat("", True)
    
class ChatSchema(ma.Schema):
    class Meta:
            fields = ['chat_id', 'user_input', 'ai_output']

chat_schema = ChatSchema()