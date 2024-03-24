from flask import *
from datetime import time
from extensions import db
import DeptGrabber
import ProgramGrabber
from models.courses import Course

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route('/courses')
def getAllCourses():
    courses = Course.query.all()  # Query all courses from the database
    # Convert courses to a list of dictionaries for JSON serialization
    courses_data = [{'name': course.name, 'department': course.department_name} for course in courses]
    return jsonify(courses_data)

@app.route('/colleges')

@app.route('/majors')

@app.route('/department')

@app.route('/faculty')

@app.route('/events')

if __name__ == '__main__':
    with app.app_context():
        # Drop existing tables, create new ones, and populate data
        db.drop_all()
        db.create_all()
        DeptGrabber.getCourses()
        ProgramGrabber.getPrograms()

    
    # Start Flask server after database preparation
    app.run(debug=True, use_reloader=False)
