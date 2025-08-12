import json
from typing import List
from entities.room import Room
from entities.student import Student
from db.room_data_access import RoomDataAccess
from db.student_data_access import StudentDataAccess


class DataLoader:
    def __init__(
        self, room_repo: RoomDataAccess, student_repo: StudentDataAccess
    ):
        self.room_repo = room_repo
        self.student_repo = student_repo

    def load_data(self, rooms_file: str, students_file: str) -> None:
        rooms = self._load_json(rooms_file)
        students = self._load_json(students_file)

        self._load_rooms(rooms)
        self._load_students(students)

    def _load_json(self, path: str) -> List[dict]:
        with open(path, "r") as f:
            return json.load(f)

    def _load_rooms(self, rooms: List[dict]) -> None:
        room_entities = [Room(**r) for r in rooms]
        self.room_repo.add_all(room_entities)

    def _load_students(self, students: List[dict]) -> None:
        student_entities = [Student(**s) for s in students]
        self.student_repo.add_all(student_entities)
