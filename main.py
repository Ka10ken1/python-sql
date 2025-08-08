from sqlmapper.data_loader import DataLoader
from sqlmapper.db_config import PostgresDB
from sqlmapper.queries.rooms_count import RoomsCountQuery
from sqlmapper.repository import Repository
from sqlmapper.schema_creator import SchemaCreator
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

    repo = Repository(db)
    loader = DataLoader(repo)
    loader.load_data(
        "./tests/fixatures/rooms.json", "./tests/fixatures/students.json"
    )

    print("Room counts:", RoomsCountQuery(db).run())


if __name__ == "__main__":
    main()
