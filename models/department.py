from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db
from sqlalchemy import *

#    "Department": {
#       "Name": "String",
#       "abbreviation": "String",
#       "college": "String",

class Department(db.Model):
    __tablename__ = 'department'

    name = db.Column(db.String(255), nullable = False, primary_key = True)
    abbreviation = db.Column(db.String(255), default=None)
    college = db.Column(db.String(255), default=None)

    def __repr__(self):
        return '<Department %r>' % self.name