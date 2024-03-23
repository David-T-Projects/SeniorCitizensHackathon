from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db
from sqlalchemy import *

# "faculty": {
#       "Name": "String",
#       "Department: String",
#       "Positions: Array",
#       "Office Location: String",
#       "Phone #: String",
#       "Email: String"
#     },

class Faculty(db.Model):
    __tablename__ = 'faculty'

    name = db.Column(db.String(255), primary_key=True)
    office = db.Column(db.String(255), nullable = False)
    positions = db.Column(db.ARRAY(String), nullable = False)
    email = db.Column(db.String(255), nullable = False)
    department = db.Column(db.String(255), primary_key=True)
    phoneNumber = db.Column(db.String(255), nullable = False)

    def __repr__(self):
        return '<Faculty %r>' % self.name
    
    __tableargs__ = (
        PrimaryKeyConstraint('name', 'department')
    )
    
