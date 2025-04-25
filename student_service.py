# student_service.py
from flask import Flask, jsonify

app = Flask(__name__)

students = {
    101: {"id": 101, "name": "Aulia Fajar", "major": "Informatika"},
    102: {"id": 102, "name": "Sinta Dewi", "major": "Sistem Informasi"},
    103: {"id": 103, "name": "Budi Santoso", "major": "Teknik Komputer"},
    104: {"id": 104, "name": "Citra Lestari", "major": "Teknik Informatika"},
    105: {"id": 105, "name": "Dian Puspita", "major": "Manajemen Informatika"},
    106: {"id": 106, "name": "Eko Prasetyo", "major": "Sains Data"},
    107: {"id": 107, "name": "Fajar Nugroho", "major": "Sistem Komputer"},
    108: {"id": 108, "name": "Gita Sari", "major": "Rekayasa Perangkat Lunak"},
}

@app.route("/students/<int:student_id>")
def get_student(student_id):
    return jsonify(students.get(student_id, {"message": "Student not found"}))

if __name__ == "__main__":
    app.run(port=5001)
