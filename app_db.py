from flask import *
from datetime import time
from extensions import db
import _grabbers.DeptGrabber as DeptGrabber
import _grabbers.ProgramGrabber as ProgramGrabber
import _grabbers.FacultyGrabber as FacultyGrabber
from models.courses import Course
from models.Colleges import Colleges
from models.department import Department
from models.courseListings import CourseListings
from models.majors import Majors
from models.faculty import Faculty
from _grabbers.CourseGrabber import scrape_schedule_information
import requests

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

@app.route('/courses')
def getAllCourses():
    courses = Course.query.all()  # Query all courses from the database
    # Convert courses to a list of dictionaries for JSON serialization
    courses_data = [{'name': course.name, 'department': course.department_name} for course in courses]
    # return jsonify(courses_data)
    return render_template('courses.html', data=courses_data)


@app.route('/colleges')
def getAllColleges():
    colleges = Colleges.query.all() #Query all colleges from the database
    #convert the colleges to a list of dictionaries for JSON serialization
    college_data = [{'name': colleges.name} for colleges in colleges]
    # return jsonify(college_data)
    return render_template('colleges.html', data=college_data)


@app.route('/majors')
def getAllMajors():
    majors = Majors.query.all()
    major_data = [{'name': major.name,
                   'program type': major.degreeType,
                   'college': major.college} for major in majors]
    # return jsonify(major_data)
    return render_template('majors.html', data=major_data)

@app.route('/department')
#    "Department": {
#       "Name": "String",
#       "abbreviation": "String",
#       "college": "String",
def getAllDepartments():
    departments = Department.query.all()
    #Convert the departments to a list of dictionaries for JSON serialization
    department_data = [{'name':departments.name} for departments in departments]

    # return jsonify(department_data)
    return render_template('departments.html', data=department_data)

@app.route('/faculty')
def getAllFaculty():
    faculty = Faculty.query.all()
    faculty_data = [{'name':fac.name,  
                     'Position':fac.positions, 
                     'Phone Number':fac.phoneNumber, 
                     'email':fac.emailAddress,} 
                     for fac in faculty]
    # return jsonify(faculty_data)
    return render_template('faculty.html', data=faculty_data)

@app.route('/courselistings')
def getAllCourseListings():
    course_listings = CourseListings.query.all()
    course_data = [{'CRN':course_listing.CRN,
                    'Department':course_listing.department,
                    'course':course_listing.course, 
                    'title':course_listing.title,
                    'max_enrollment':course_listing.max_enrollment,
                    'start':course_listing.start,
                    'end':course_listing.end,
                    'days':course_listing.days,}
                    for course_listing in course_listings]
    # return jsonify(course_data)
    return render_template('courseListings.html', data=course_data)

@app.route('/rooms')
def list_room_endpoints():
    endpoints = [
        '/rooms/ELC',
        '/rooms/BEV',
        '/rooms/JEM',
        '/rooms/TBA',
        '/rooms/OPB',
        '/rooms/HOSP',
        '/rooms/UFC',
        '/rooms/OKT',
        '/rooms/A&M',
        '/rooms/ENG',
        '/rooms/CRH',
        '/rooms/SPR',
        '/rooms/SST',
        '/rooms/MSB',
        '/rooms/SWI',
        '/rooms/MOR',
        '/rooms/Outdr',
        '/rooms/FFH',
        '/rooms/ROB',
        '/rooms/WIL',
        '/rooms/SSB',
        '/rooms/JRC',
        '/rooms/LIB',
        '/rooms/NUR',
        '/rooms/BAB',
    ]
    return render_template('endpoints.html', endpoints=endpoints)


@app.route('/rooms/ELC')
def getELCRoomInfo():
    response = requests.get("https://uah.quietroom.app/availability/ELC?day=S&startTime=0100&endTime=0200")
    response_list = list(response)
    html_table = '<ELC Rooms>\n'
    for i in response_list:
        html_table += '  <tr>\n'
        html_table += f'    <td>{i}</td>\n'
    return render_template('html_table.html', data=html_table)
    

@app.route('/rooms/BEV')
def getBEVRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/BEV?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/JEM')
def getJEMRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/JEM?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/TBA')
def getTBARoomInfo():
    return requests.get("https://uah.quietroom.app/availability/TBA?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/OPB')
def getOPBRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/OPB?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/HOSP')
def getHOSPRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/HOSP?day=S&startTime=0100&endTime=0200")
    

@app.route( '/rooms/UFC')
def getUFCRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/UFC?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/A&M')
def getAMRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/A&M?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/ENG')
def getENGRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/ENG?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/CRH')
def getCRHRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/CRH?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/SPR')
def getSPRRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/SPR?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/SST')
def getSSTRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/SST?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/MSB')
def getMSBRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/MSB?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/SWI')
def getSWIRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/SWI?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/MOR')
def getMORRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/MOR?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/Outdr')
def getOutdrRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/Outdr?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/FFH')
def getFFHRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/FFH?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/ROB')
def getROBRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/ROB?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/WIL')
def getWILRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/WIL?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/SSB')
def getSSBRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/SSB?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/JRC')
def getJRCRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/JRC?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/LIB')
def getLIBRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/LIB?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/NUR')
def getNURRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/NUR?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/BAB')
def getBABRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/BAB?day=S&startTime=0100&endTime=0200")
    

@app.route('/rooms/OKT')
def getOKTRoomInfo():
    return requests.get("https://uah.quietroom.app/availability/OKT?day=S&startTime=0100&endTime=0200")
    


@app.route('/')
def list_endpoints():
    # Define a list of endpoint URLs
    endpoints = [
        '/department',
        '/courses',
        '/colleges',
        '/courselistings',
        '/faculty',
        '/majors',
        '/rooms'
        # Add more endpoints as needed
    ]
    return render_template('endpoints.html', endpoints=endpoints)

if __name__ == '__main__':
    with app.app_context():
        # Drop existing tables, create new ones, and populate data
        db.drop_all()
        db.create_all()
        DeptGrabber.getCourses()
        ProgramGrabber.getPrograms()
        scrape_schedule_information()
        FacultyGrabber.populateFaculty()
       

        
    # Start Flask server after database preparation
    app.run(debug=True, use_reloader=False, port = 5001)
