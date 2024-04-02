from flask import Flask
# import psycopg2
import Routes

from db import *

app = Flask(__name__, template_folder="site/templates", static_folder="site/static")

# app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://127.0.0.1:5432/homework"
# app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

# init_db(app, db)

# def create_tables():
#     with app.app_context():
#         print("creating tables...")
#         db.create_all()
#         print("tables created successfully")

 @app.before_first_request
  def create_tables():
      cur = mysql.connection.cursor()
      cur.execute('''CREATE TABLE IF NOT EXISTS users (
          id INT AUTO_INCREMENT PRIMARY KEY,
          username VARCHAR(255) NOT NULL,
          email VARCHAR(255) NOT NULL
      )''')
      mysql.connection.commit()
      cur.close()

# app.register_blueprint(Routes.categories)
# app.register_blueprint(Routes.products)
app.register_blueprint(Routes.static_blueprint)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port="10000", debug=True)