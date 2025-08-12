from typing import List
from entities.student import Student
from psycopg2.extras import execute_values


class StudentDataAccess:
    def __init__(self, db):
        self.db = db

    def add(
        self, student_id: int, name: str, birthday: str, sex: str, room_id: int
    ) -> None:
        self.db.execute(
            """
            INSERT INTO students (id, name, birthday, sex, room_id)
            VALUES (%s, %s, %s, %s, %s);
            """,
            (student_id, name, birthday, sex, room_id),
        )

    def add_all(self, students: List[Student]) -> None:
        values = [
            (s["id"], s["name"], s["birthday"], s["sex"], s["room"])
            for s in students
        ]
        sql = """
        INSERT INTO students (id, name, birthday, sex, room_id)
        VALUES %s
        """
        with self.db.cursor() as cur:
            execute_values(cur, sql, values)
