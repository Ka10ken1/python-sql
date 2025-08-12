from typing import List
from psycopg2.extras import execute_values

from entities.room import Room


class RoomRepository:
    def __init__(self, db):
        self.db = db

    def add(self, room_id: int, name: str) -> None:
        self.db.execute(
            "INSERT INTO rooms (id, name) VALUES (%s, %s);",
            (room_id, name),
        )

    def add_all(self, rooms: List[Room]) -> None:
        sql = """
            INSERT INTO rooms (id, name)
            VALUES %s
        """
        values = [(room["id"], room["name"]) for room in rooms]
        with self.db.cursor() as cur:
            execute_values(cur, sql, values)
