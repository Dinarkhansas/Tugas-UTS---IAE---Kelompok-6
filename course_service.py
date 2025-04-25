# course_service.py
from flask import Flask, jsonify

app = Flask(__name__)

courses = {
    301: {"id": 301, "name": "Pemrograman Web", "sks": 3},
    302: {"id": 302, "name": "Sistem Operasi", "sks": 4},
    303: {"id": 303, "name": "Struktur Data", "sks": 3},
    304: {"id": 304, "name": "Kecerdasan Buatan", "sks": 3},
    305: {"id": 305, "name": "Jaringan Komputer", "sks": 3},
    306: {"id": 306, "name": "Pengolahan Citra Digital", "sks": 2},
    307: {"id": 307, "name": "Pemrograman Mobile", "sks": 3},
    308: {"id": 308, "name": "Etika Profesi", "sks": 2},
}

@app.route("/courses/<int:course_id>")
def get_course(course_id):
    return jsonify(courses.get(course_id, {"message": "Course not found"}))

if __name__ == "__main__":
    app.run(port=5002)
