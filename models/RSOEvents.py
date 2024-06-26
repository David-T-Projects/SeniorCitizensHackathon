from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db
from sqlalchemy import *

class RSOEvents(db.Model):
    __tablename__ = 'rsoevents'

    name = db.Column(db.String(255), primary_key = True)
    date = db.Column(db.String(255), primary_key = True)
    time = db.Column(db.String(255), nullable = False)
    location = db.Column(db.String(255), nullable = False)
    RSO = db.Column(db.String(255), nullable = False)
    description = db.Column(db.String(255), nullable = False)
    themes = db.Column(db.ARRAY(String(255)), nullable = False)
    categories = db.Column(db.ARRAY(String(255)), nullable = False)
    perks = db.Column(db.ARRAY(String(255)), nullable = False)
