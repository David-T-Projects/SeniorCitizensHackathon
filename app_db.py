from flask import *
from datetime import time
from extensions import db
<<<<<<< HEAD
import DeptGrabber
import ProgramGrabber
from models.courses import Course
from models.Colleges import Colleges
from models.department import Department

=======
from DataGrabber import scrape_course_information
from courseScrapy import scrape_schedule_information
>>>>>>> main

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route('/courses')
def getAllCourses():
    courses = Course.query.all()  # Query all courses from the database
    # Convert courses to a list of dictionaries for JSON serialization
    courses_data = [{'name': course.name, 'department': course.department_name} for course in courses]
    return jsonify(courses_data)

<<<<<<< HEAD
@app.route('/colleges')
def getAllColleges():
    colleges = Colleges.query.all() #Query all colleges from the database
    #convert the colleges to a list of dictionaries for JSON serialization
    college_data = [{'name': colleges.name} for colleges in colleges]
    return jsonify(college_data)

# @app.route('/majors')

@app.route('/department')
#    "Department": {
#       "Name": "String",
#       "abbreviation": "String",
#       "college": "String",

def getAllDepartments():
    departments = Department.query.all()
    #Convert the departments to a list of dictionaries for JSON serialization
    department_data = [{'name':departments.name, 'abbreviation':departments.abbreviation, 'college':departments.college_name} for departments in departments]
    return jsonify(department_data)

# @app.route('/faculty')

# @app.route('/events')

if __name__ == '__main__':
    with app.app_context():
        # Drop existing tables, create new ones, and populate data
        db.drop_all()
        db.create_all()
        DeptGrabber.getCourses()
        ProgramGrabber.getPrograms()
        
    # Start Flask server after database preparation
    app.run(debug=True, use_reloader=False)
=======
    # Prepping the database
    db.drop_all()
    db.create_all()
    scrape_course_information()
    scrape_schedule_information()
    print("courses database populated")
>>>>>>> main
