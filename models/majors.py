from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db
from sqlalchemy import *

class Majors(db.Model):
    __tablename__ = 'majors'

    name = db.Column(db.String(255), nullable = False, primary_key = True)
    creditHours = db.Column(db.Integer, nullable = False)
    degreeType = db.Column(db.String(255), nullable = False)
    concentration = db.Column(db.ARRAY(String(255)), nullable = False)
    department = db.Column(db.String(255), nullable = False)
    college = db.Column(db.String(255), nullable = False)

    def __repr__(self):
        return '<Majors %r>' % self.name