class RoomsCountQuery:
    def __init__(self, db):
        self.db = db

    def run(self):
        return self.db.fetchall(
            """
                select r.id, count(s.id) as student_count
                from rooms r
                left join students s on r.id = s.room_id
                group by r.id;
            """
        )
