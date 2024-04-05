from flask import Flask

import Routes

from db import *

app = Flask(__name__, template_folder="site/templates", static_folder="Site/Static")


# SQLAlchemy configurations
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://test@test.com:1234!@localhost/chatbot'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

# Create all database tables
with app.app_context():
    db.create_all()


app.register_blueprint(Routes.static_blueprint)
app.register_blueprint(Routes.chatbot)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="3000", debug=True)