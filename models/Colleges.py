from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db
from sqlalchemy import *


class Colleges(db.Model):
    __tablename__ = 'colleges'

    name = db.Column(db.String(255), nullable = False, primary_key = True)
    short_form = db.Column(db.String(255))
    
    # department = db.relationship('Department', uselist=False, backref='department', lazy=True)
    # department_name = db.Column(db.String(255), db.ForeignKey('department.name'), nullable=True)

    
    #department = db.Column(db.ARRAY(String(255)), nullable = False)
    
    #scholarships = db.Column(db.ARRAY(String(255)), default = None)

    def __repr__(self):
        return '<Colleges %r>' % self.name
    
    