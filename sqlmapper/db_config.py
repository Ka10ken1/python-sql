import psycopg2
from psycopg2.extras import RealDictCursor
from .interfaces import IDatabase


class PostgresDB(IDatabase):
    def __init__(self, dsn: str):
        self.dsn = dsn
        self.conn = None

    def connect(self):
        if not self.conn:
            self.conn = psycopg2.connect(self.dsn)
            self.conn.autocommit = True
        return self.conn

    def execute(self, query: str, params=None):
        with self.connect().cursor() as cur:
            cur.execute(query, params)

    def fetchall(self, query: str, params=None):
        with self.connect().cursor(cursor_factory=RealDictCursor) as cur:
            cur.execute(query, params)
            return cur.fetchall()
