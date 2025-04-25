# enrollment_service.py
from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/enrollments", methods=["POST"])
def enroll():
    data = request.json
    student = requests.get(f"http://localhost:5001/students/{data['student_id']}").json()
    course = requests.get(f"http://localhost:5002/courses/{data['course_id']}").json()

    return jsonify({
        "message": "Enrollment success!",
        "student": student,
        "course": course,
        "semester": "Genap 2024"
    })

if __name__ == "__main__":
    app.run(port=5003)
