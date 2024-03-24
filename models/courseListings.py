from flask_sqlalchemy import SQLAlchemy
from flask import Flask
from extensions import db

class CourseListings(db.Model):
    __tablename__ = 'course_listings'

    sectionType = db.Column(db.String(255), nullable=False)
    CRN = db.Column(db.Integer, nullable=False)
    department = db.Column(db.String(255), primary_key=True)
    course = db.Column(db.String(255), primary_key=True)
    title = db.Column(db.String(255), nullable=False)
    credit = db.Column(db.Float)
    max_enrollment = db.Column(db.Integer, nullable=False)
    enrollment = db.Column(db.Integer, nullable=False)
    availability = db.Column(db.String(255), nullable=False)
    wait_list = db.Column(db.Integer, nullable=False)
    days= db.Column(db.String(255), nullable=False)
    start= db.Column(db.String(255), nullable=False)
    end = db.Column(db.String(255), nullable=False)
    building = db.Column(db.String(255), nullable=False)
    room = db.Column(db.String(255), nullable=False)
    instructor= db.Column(db.String(255), nullable=False)