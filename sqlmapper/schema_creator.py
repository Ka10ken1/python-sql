class SchemaCreator:
    def __init__(self, db):
        self.db = db

    def create_schema(self):
        self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS rooms (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL UNIQUE
            );
        """
        )
        self.db.execute(
            """
            CREATE TABLE IF NOT EXISTS students (
                id SERIAL PRIMARY KEY,
                name TEXT NOT NULL,
                birthday DATE NOT NULL,
                sex CHAR(1) NOT NULL,
                room_id INT REFERENCES rooms(id) ON DELETE SET NULL ON UPDATE CASCADE
            );
        """
        )

        self.db.execute(
            "CREATE INDEX IF NOT EXISTS idx_students_room_id ON students(room_id);"
        )
        self.db.execute(
            "CREATE INDEX IF NOT EXISTS idx_students_birthday ON students(birthday);"
        )
        self.db.execute(
            "CREATE INDEX IF NOT EXISTS idx_students_sex ON students(sex);"
        )
