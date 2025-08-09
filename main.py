from sqlmapper.data_loader import DataLoader
from sqlmapper.db_config import PostgresDB
from sqlmapper.queries.rooms_count import RoomsCountQuery
from sqlmapper.queries.largest_age_diff import LargestAgeDifferenceQuery
from sqlmapper.queries.smallest_avg_age import SmallestAverageAgeCountQuery
from sqlmapper.queries.mixed_gender import MixedGenderRoomatesQuery
from sqlmapper.repository import Repository
from sqlmapper.schema_creator import SchemaCreator
from dotenv import load_dotenv
import json
import decimal
import os


def decimal_default(obj):
    if isinstance(obj, decimal.Decimal):
        return float(obj)
    raise TypeError


def save_to_json(filename, data):
    with open(filename, "w") as f:
        json.dump(data, f, indent=4, default=decimal_default)


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

    repo = Repository(db)
    loader = DataLoader(repo)
    loader.load_data(
        "./tests/fixatures/rooms.json", "./tests/fixatures/students.json"
    )

    save_to_json("output/room_counts.json", RoomsCountQuery(db).run())
    save_to_json(
        "output/smallest_avg_age.json", SmallestAverageAgeCountQuery(db).run()
    )
    save_to_json(
        "output/largest_age_diff.json", LargestAgeDifferenceQuery(db).run()
    )
    save_to_json(
        "output/mixed_gender_rooms.json", MixedGenderRoomatesQuery(db).run()
    )


if __name__ == "__main__":
    main()
