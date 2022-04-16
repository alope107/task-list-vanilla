import atexit
import importlib.resources as pkg_resources

import psycopg2

from . import static

def _init_database(dbname, user):
    db = psycopg2.connect(f"dbname='{dbname}' user='{user}'")
    atexit.register(db.close)
    return db

class Database:
    def __init__(self, dbname, user):
        self._db = _init_database(dbname, user)

    def query(self, query, params=None):
        cur = self._db.cursor()
        try:
            cur.execute(query, params)
            rows = None
            if cur.description is not None:
                rows = cur.fetchall()
            self._db.commit()
        finally:
            cur.close()
        return rows

    def clear_db(self):
        clear_db = pkg_resources.read_text(static, 'clear_db.sql')
        self.query(clear_db)
