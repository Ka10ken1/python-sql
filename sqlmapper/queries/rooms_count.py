from sqlmapper.interfaces import IQuery


class RoomsCountQuery(IQuery):
    def __init__(self, db):
        self.db = db

    def run(self):
        return self.db.fetchall(
            """
            SELECT r.name AS room, COUNT(s.id) AS student_count
            FROM rooms r
            LEFT JOIN students s ON s.room_id = r.id
            GROUP BY r.name
            ORDER BY student_count DESC;
        """
        )
