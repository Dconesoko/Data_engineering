from contextlib import contextmanager
import psycopg2
from psycopg2.extras import DictCursor
from dataclasses import dataclass



@dataclass
class DBConnection:
    user: str
    password: str
    db: str
    host: str
    port: int = 5432

    def conn_url(self) -> str:
        return (
            f'postgresql://{self.user}:{self.password}@'
            f'{self.host}:{self.port}/{self.db}'
        )
    def __post_init__(self):
        self.conn_url = self.conn_url()

class WarehouseConnection:
    def __init__(self, db_conn: DBConnection):
        self.conn_url = db_conn.conn_url

    @contextmanager
    def managed_cursor(self, cursor_factory=None):
        self.conn = psycopg2.connect(self.conn_url)
        self.conn.autocommit = True
        self.curr = self.conn.cursor(cursor_factory=cursor_factory)
        try:
            yield self.curr
        finally:
            self.curr.close()
            self.conn.close()