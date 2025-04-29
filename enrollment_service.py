from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

# Simpan semua data enrollment di memory
enrollments = []

@app.route("/enrollments", methods=["POST"])
def enroll():
    data = request.json

    # Ambil data dari service lain
    student = requests.get(f"http://localhost:5008/students/{data['student_id']}").json()
    course = requests.get(f"http://localhost:5005/courses/{data['course_id']}").json()

    # Simpan ke daftar enrollment
    enrollments.append({
        "student_id": student["id"],
        "student_name": student["name"],
        "course_id": course["id"],
        "course_name": course["name"],
        "semester": "Genap 2024"
    })

    # Kirim response
    return jsonify({
        "message": "Enrollment success!",
        "student": student,
        "course": course,
        "semester": "Genap 2024"
    })

@app.route("/students/<int:student_id>/enrollments", methods=["GET"])
def get_student_enrollments(student_id):
    # Filter data enrollment berdasarkan student_id
    student_enroll = [e for e in enrollments if e["student_id"] == student_id]

    if not student_enroll:
        return jsonify({"message": "No enrollments found for this student"}), 404

    return jsonify(student_enroll)

if __name__ == "__main__":
    app.run(port=5003)
