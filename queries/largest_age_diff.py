class LargestAgeDifferenceQuery:
    def __init__(self, db):
        self.db = db

    def run(self):
        return self.db.fetchall(
            """
                select r.id as room_id, (max(extract(year from age(s.birthday))) - min(extract(year from age(s.birthday)))) as age_diff
                from rooms r
                join students s on r.id = s.room_id
                group by r.id
                order by age_diff desc
                limit 5;
            """
        )
