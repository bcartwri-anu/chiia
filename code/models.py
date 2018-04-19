import database as db
from flask import Flask
import sqlalchemy as sa
import datetime

class User(db.Base):
    __tablename__ = 'users'
    id = sa.Column(sa.Integer, primary_key=True)
    fname = sa.Column(sa.String, nullable=False)
    lname = sa.Column(sa.String, nullable=False)
    email = sa.Column(sa.String, nullable=False)
    language = sa.Column(sa.Boolean, nullable=False) # true is english alone, false is mandarin, too.
    pw_hashed = sa.Column(sa.String, nullable=False)

    def __repr__(self):
        return '<Details {fname}, {lname}, {email}, with language skills: {language}>'.format(fname=self.fname, lname=self.lname, email=self.email, language=self.language)
    def get_id(self):
        return self.id

    def is_active(self):
        return self._user.enabled

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True
