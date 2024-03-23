from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db
from sqlalchemy import *

#  "Colleges": {
#       "College": {
#         "Name": "String",
#         "Dept": "String",
#         "Scholarships": [{"ScholarshipName": "String"}]
#         }


class Colleges(db.Model):
    __tablename__ = 'colleges'

    name = db.Column(db.String(255), nullable = False)
    department = db.Column(db.String(255), nullable = False)
    scholarships = db.Column(db.ARRAY(String(255)), nullable = False)

    def __repr__(self):
        return '<Colleges %r>' % self.name