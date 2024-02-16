from flask import Flask, request, jsonify
from pymongo import MongoClient
import logging
import os

app = Flask(__name__)

# Setup logging
if not os.path.exists('logs'):
    os.makedirs('logs')
logging.basicConfig(filename='c', level=logging.DEBUG)

# Connect to MongoDB
client = MongoClient('mongodb://mongoadmin:secret@172.17.0.2:27017/')

db = client.course_enrollments

@app.route('/enroll', methods=['POST'])
def enroll_student():
    data = request.json
    student_name = data.get('student_name')
    course_name = data.get('course_name')
    
    if student_name and course_name:
        db.enrollments.insert_one({'student_name': student_name, 'course_name': course_name})
        logging.info(f"Student {student_name} enrolled in {course_name}")
        return jsonify({'message': f'Successfully enrolled {student_name} in {course_name}'}), 200
    else:
        return jsonify({'message': 'Missing student name or course name'}), 400

@app.route('/students', methods=['GET'])
def list_students():
    # Fetch all students and courses from the database without filtering
    students = db.enrollments.find({}, {'_id': 0})
    return jsonify(list(students)), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
