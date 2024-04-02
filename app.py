from flask import Flask
import psycopg2
import routes

from db import *

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://127.0.0.1:5432/homework"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

init_db(app, db)

def create_tables():
    with app.app_context():
        print("creating tables...")
        db.create_all()
        print("tables created successfully")

app.register_blueprint(routes.categories)
app.register_blueprint(routes.products)

if __name__ == "__main__":
    app.run(host="0.0.0.0", port="8086", debug=True)