from flask import Flask, jsonify
from datetime import time
from extensions import db
import DataGrabber
from models.Courses import Course

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route('/courses')
def getAllCourses():
    courses = Course.query.all()  # Query all courses from the database
    # Convert courses to a list of dictionaries for JSON serialization
    courses_data = [{'name': course.name, 'department': course.department} for course in courses]
    return jsonify(courses_data)

if __name__ == '__main__':
    with app.app_context():
        # Drop existing tables, create new ones, and populate data
        db.drop_all()
        db.create_all()
        DataGrabber.getCourses()
    
    # Start Flask server after database preparation
    app.run(debug=True, use_reloader=False)
