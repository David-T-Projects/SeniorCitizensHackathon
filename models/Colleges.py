from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db
from sqlalchemy import *


class Colleges(db.Model):
    __tablename__ = 'colleges'

    name = db.Column(db.String(255), nullable = False, primary_key = True)
    department = db.Column(db.String(255), nullable = False)
    scholarships = db.Column(db.ARRAY(String(255)), nullable = False)

    def __repr__(self):
        return '<Colleges %r>' % self.name
    
    