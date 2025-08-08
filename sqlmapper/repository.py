class Repository:
    def __init__(self, db):
        self.db = db

    def insert_room(self, id, name):
        self.db.execute(
            "INSERT INTO rooms (id, name) VALUES (%s, %s);",
            (id, name),
        )

    def insert_student(self, id, name, birthday, sex, room_id):
        self.db.execute(
            """
            INSERT INTO students (id, name, birthday, sex, room_id)
            VALUES (%s, %s, %s, %s, %s);
            """,
            (id, name, birthday, sex, room_id),
        )
