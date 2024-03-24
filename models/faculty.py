from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db
from sqlalchemy import *

#    "Faculty": {
#       "Name": "String",
#       "Department": "String",
#       "Positions": [{"PositionName": "String"}],
#       "Office Location": "String",
#       "Phone #": "String",
#       "Email": "String"

class Faculty(db.Model):
    __tablename__ = 'faculty'

    #Note: Removed nullable from department just to get something running, added a id number that should be changed later
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(255), nullable = False, primary_key = True)
    department = db.Column(db.String(255))
    positions = db.Column(String(255), nullable = False)
    officeLocation = db.Column(db.String(255))
    phoneNumber = db.Column(db.String(255))    #Not every faculty member seems to have a phone # attached
    emailAddress = db.Column(db.String(255))

    def __repr__(self):
        return '<Faculty %r>' % self.name