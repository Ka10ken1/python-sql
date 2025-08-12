from db.student_data_access import StudentDataAccess
from loader.data_loader import DataLoader
from db.db_config import PostgresDB
from queries.rooms_count import RoomsCountQuery
from queries.largest_age_diff import LargestAgeDifferenceQuery
from queries.smallest_avg_age import SmallestAverageAgeCountQuery
from queries.mixed_gender import MixedGenderRoomatesQuery
from db.schema_creator import SchemaCreator
from db.room_data_access import RoomDataAccess
from dotenv import load_dotenv
import os


def main():

    load_dotenv()

    connection = (
        f"dbname={os.getenv('DB_NAME')} "
        f"user={os.getenv('DB_USER')} "
        f"password={os.getenv('DB_PASSWORD')} "
        f"host={os.getenv('DB_HOST')} "
        f"port={os.getenv('DB_PORT')}"
    )

    db = PostgresDB(connection)

    schema = SchemaCreator(db)
    schema.create_schema()

    room_repo = RoomDataAccess(db)
    student_repo = StudentDataAccess(db)

    loader = DataLoader(room_repo, student_repo)
    loader.load_data(
        "./tests/fixatures/rooms.json", "./tests/fixatures/students.json"
    )

    room_count = RoomsCountQuery(db).run()
    smallest_avg_age = SmallestAverageAgeCountQuery(db).run()
    largest_age_diff = LargestAgeDifferenceQuery(db).run()
    mixed_gender = MixedGenderRoomatesQuery(db).run()

    print(f"Room count: {room_count}")
    print(f"Smallest average age: {smallest_avg_age}")
    print(f"Largest age difference: {largest_age_diff}")
    print(f"Mixed gender roommates present: {mixed_gender}")


if __name__ == "__main__":
    main()
