# course_service.py
from flask import Flask, jsonify

app = Flask(__name__)

courses = {
    301: {"id": 301, "name": "Pemrograman Web", "sks": 3},
    302: {"id": 302, "name": "Sistem Operasi", "sks": 4},
}

@app.route("/courses/<int:course_id>")
def get_course(course_id):
    return jsonify(courses.get(course_id, {"message": "Course not found"}))

if __name__ == "__main__":
    app.run(port=5002)
