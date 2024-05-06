from os import path

from . import DB_NAME, db


def create_db(app):
    with app.app_context():
        if not path.exists('website/' + DB_NAME):
            db.create_all()
            print('Database Created!')