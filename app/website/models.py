"""
This module contains the models for the website application.
"""

from flask_login import UserMixin
from sqlalchemy.sql import func

from . import db


class Note(db.Model):
    """
    Represents a note in the application.
    """

    id = db.Column(db.Integer, primary_key=True)
    data = db.Column(db.String(10000))
    date = db.Column(db.DateTime(timezone=True))
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'))  # This is a foreign key that links the note to the user that created it

    def __init__(self, data, user_id):
        self.data = data
        self.user_id = user_id

    def save(self):
        """
        Save the note to the database.
        """
        db.session.add(self)
        db.session.commit()


class User(db.Model, UserMixin):
    """
    Represents a user in the application.
    """

    id = db.Column(db.Integer, primary_key=True)
    email = db.Column(db.String(150), unique=True)
    password = db.Column(db.String(150))
    username = db.Column(db.String(150), unique=True)
    notes = db.relationship('Note')  # This is a list of all the notes that the user has created
