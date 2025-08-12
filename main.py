from repositories.data_loader import DataLoader
from repositories.db_config import PostgresDB
from queries.rooms_count import RoomsCountQuery
from queries.largest_age_diff import LargestAgeDifferenceQuery
from queries.smallest_avg_age import SmallestAverageAgeCountQuery
from queries.mixed_gender import MixedGenderRoomatesQuery
from repositories.schema_creator import SchemaCreator
from repositories.room_repository import RoomRepository
from repositories.student_repository import StudentRepository
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

    room_repo = RoomRepository(db)
    student_repo = StudentRepository(db)

    loader = DataLoader(room_repo, student_repo)
    loader.load_data(
        "./tests/fixatures/rooms.json", "./tests/fixatures/students.json"
    )

    room_count = RoomsCountQuery(db).run()
    smallest_avg_age = SmallestAverageAgeCountQuery(db).run()
    largest_age_diff = LargestAgeDifferenceQuery(db).run()
    mixed_gender = MixedGenderRoomatesQuery(db).run()

    print(room_count, smallest_avg_age, largest_age_diff, mixed_gender)


if __name__ == "__main__":
    main()
