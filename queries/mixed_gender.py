class MixedGenderRoomatesQuery:
    def __init__(self, db):
        self.db = db

    def run(self):
        return self.db.fetchall(
            """
                select r.id as room_id
                from rooms r
                join students s on r.id = s.room_id
                group by r.id
                having count(distinct s.sex) > 1;
            """
        )
