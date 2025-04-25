# student_service.py
from flask import Flask, jsonify

app = Flask(__name__)

students = {
    101: {"id": 101, "name": "Aulia Fajar", "major": "Informatika"},
    102: {"id": 102, "name": "Sinta Dewi", "major": "Sistem Informasi"},
}

@app.route("/students/<int:student_id>")
def get_student(student_id):
    return jsonify(students.get(student_id, {"message": "Student not found"}))

if __name__ == "__main__":
    app.run(port=5001)
