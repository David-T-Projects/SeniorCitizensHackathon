from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db
from sqlalchemy import *

'''
"RSO_Events": {
      "Name": "String",
      "Date": "String",
      "Time": "String",
      "Location": "String",
      "RSO": "String",
      "Description": "String",
      "Themes": [{"ThemeName": "String"}],
      "Categories": [{"CategoryName": "String"}],
      "Perks": [{"PerkName": "String"}]
'''

class Course(db.Model):
    __tablename__ = 'course'

    name = db.Column(db.String(255), primary_key = True)
    date = db.Column(db.String(255), primary_key = True)
    time = db.Column(db.String(255), nullable = False)
    location = db.Column(db.String(255), nullable = False)
    RSO = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    concentration = db.Column(db.ARRAY(String(255)), nullable = False)
    concentration = db.Column(db.ARRAY(String(255)), nullable = False)
    concentration = db.Column(db.ARRAY(String(255)), nullable = False)
