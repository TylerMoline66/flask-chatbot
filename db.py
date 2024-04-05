from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def init_db(app):
    if isinstance(app, Flask):
        db.init_app(app)
    else:
        raise ValueError('cannot init db without app object')

    # Create all database tables
    with app.app_context():
        db.create_all()

    return app


 
