import database as db
from flask import Flask
import sqlalchemy as sa
import sqlalchemy.orm as sao
import datetime

class User(db.Base):
    __tablename__ = 'users'
    __table_args__ = {'extend_existing': True}

    id = sa.Column(sa.Integer, primary_key=True)
    fname = sa.Column(sa.String, nullable=False)
    lname = sa.Column(sa.String, nullable=False)
    email = sa.Column(sa.String, nullable=False)
    language = sa.Column(sa.Boolean, nullable=False) # true is english alone, false is mandarin, too.
    pw_hashed = sa.Column(sa.String, nullable=False)
    admin = sa.Column(sa.Boolean)
    confirmed = sa.Column(sa.Boolean, default=False)

    def __repr__(self):
        return '<Details {fname}, {lname}, {email}, with language skills: {language} where account conf = {conf}>'.format(fname=self.fname,
            lname=self.lname, email=self.email, language=self.language, conf=self.confirmed)
    def get_id(self):
        return self.id

    def is_valid(self):
        return self.confirmed

    def is_active(self):
        return self._user.enabled

    def is_anonymous(self):
        return False

    def is_authenticated(self):
        return True

    def is_admin(self):
        if self.admin:
            return True
        else:
            return False


class Admin(db.Base):
    __tablename__ = 'admin'
    id = sa.Column(sa.Integer, primary_key=True)
    search_names = sao.relationship('Search_Names', backref='admin', lazy=True)

class Search_Names(db.Base):
    __tablename__ = 'search-names'
    id = sa.Column(sa.Integer, primary_key=True)
    name = sa.Column(sa.String, nullable=False)
    admin_id = sa.Column(sa.Integer, sa.ForeignKey('admin.id'), nullable=False)
