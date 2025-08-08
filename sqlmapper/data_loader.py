import json
from sqlmapper.repository import Repository


class DataLoader:
    def __init__(self, repo: Repository):
        self.repo = repo

    def load_data(self, rooms_file, students_file):
        with open(rooms_file) as f:
            rooms = json.load(f)
        with open(students_file) as f:
            students = json.load(f)

        for r in rooms:
            self.repo.insert_room(r["id"], r["name"])

        for s in students:
            self.repo.insert_student(
                s["id"], s["name"], s["birthday"], s["sex"], s["room"]
            )
