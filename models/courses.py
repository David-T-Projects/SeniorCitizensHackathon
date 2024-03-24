from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db

class Course(db.Model):
    __tablename__ = 'course'

    courseID = db.Column(db.String(255), primary_key=True)
    name = db.Column(db.String(255), nullable=False)
    department_name = db.Column(db.String(255), db.ForeignKey('department.name'), nullable=False, )
    description = db.Column(db.String(5000))
    credits = db.Column(db.Float)

    department = db.relationship('Department', uselist=False, backref='course', lazy=True)

    def __repr__(self):
        return f'<Course {self.name}>'
