from flask import Flask, request, jsonify, render_template_string
from pymongo import MongoClient
import logging
import os

app = Flask(__name__)

# Setup logging
if not os.path.exists('logs'):
    os.makedirs('logs')
logging.basicConfig(filename='logs/log-file.log', level=logging.DEBUG)

# Connect to MongoDB - Adjust as needed
client = MongoClient('mongodb://admin:Admin12345@172.17.0.2:27017/')
db = client.course_enrollments

@app.route('/')
def index():
    # HTML with enhanced CSS and JavaScript
    return render_template_string('''
        <html>
            <head>
                <title>Student Enrollment</title>
                <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/4.7.0/css/font-awesome.min.css">
                <script src="https://ajax.googleapis.com/ajax/libs/jquery/3.5.1/jquery.min.js"></script>
                <style>
                    body { font-family: Arial, sans-serif; text-align: center; margin-top: 50px; }
                    input[type="text"], button {
                        padding: 10px;
                        margin: 10px 0;
                        border: 1px solid #ddd;
                        border-radius: 5px;
                        width: 20%;
                    }
                    button {
                        background-color: #4CAF50;
                        color: white;
                        cursor: pointer;
                    }
                    button:hover {
                        opacity: 0.8;
                    }
                    table {
                        margin: auto;
                        width: 50%;
                        border-collapse: collapse;
                    }
                    th, td {
                        padding: 8px;
                        text-align: left;
                        border-bottom: 1px solid #ddd;
                    }
                    th {
                        background-color: #4CAF50;
                        color: white;
                    }
                </style>
                <script>
                    $(document).ready(function(){
                        $("#enrollButton").click(function(){
                            var studentName = $("#studentName").val();
                            var courseName = $("#courseName").val();
                            $.ajax({
                                url: '/enroll',
                                type: 'POST',
                                contentType: 'application/json',
                                data: JSON.stringify({"student_name": studentName, "course_name": courseName}),
                                success: function(response){
                                    alert(response.message);
                                    // Optionally clear the form fields
                                    $("#studentName").val('');
                                    $("#courseName").val('');
                                    // Automatically refresh the list
                                    $("#getStudentsButton").click();
                                },
                                error: function(response){
                                    alert('Error enrolling student');
                                }
                            });
                        });
                        $("#getStudentsButton").click(function(){
                            $.ajax({
                                url: '/students',
                                type: 'GET',
                                success: function(response){
                                    var table = "<table><tr><th>Student Name</th><th>Course Name</th></tr>";
                                    $.each(response, function(index, student){
                                        table += "<tr><td>" + student.student_name + "</td><td>" + student.course_name + "</td></tr>";
                                    });
                                    table += "</table>";
                                    $("#studentsList").html(table);
                                },
                                error: function(response){
                                    alert('Error fetching students');
                                }
                            });
                        });
                    });
                </script>
            </head>
            <body>
                <h2>Student Enrollment Form</h2>
                <input type="text" id="studentName" placeholder="Student Name">
                <input type="text" id="courseName" placeholder="Course Name">
                <br>
                <button id="enrollButton"><i class="fa fa-user-plus"></i> Enroll Student</button>
                <button id="getStudentsButton"><i class="fa fa-list"></i> Get Enrolled Students</button>
                <div id="studentsList"></div>
            </body>
        </html>
    ''', code=200)

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
    students = db.enrollments.find({}, {'_id': 0})
    return jsonify(list(students)), 200

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
