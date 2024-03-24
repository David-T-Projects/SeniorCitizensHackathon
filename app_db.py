from flask import Flask
from datetime import time
from extensions import db
from DataGrabber import scrape_course_information
from courseScrapy import scrape_schedule_information

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////tmp/test.db'
db.init_app(app)

# need to perform database operations within app_context
with app.app_context():

    # Prepping the database
    db.drop_all()
    db.create_all()
    #scrape_course_information()
    scrape_schedule_information()
    print("courses database populated")
