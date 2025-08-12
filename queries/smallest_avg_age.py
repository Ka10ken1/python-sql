class SmallestAverageAgeCountQuery:
    def __init__(self, db):
        self.db = db

    def run(self):
        return self.db.fetchall(
            """
                select r.id as room_id, round(avg(extract(year from age(s.birthday))),2) as avg_age
                from rooms r
                inner join students s on r.id = s.room_id
                group by r.id
                order by avg_age desc
                limit 5;
            """
        )
