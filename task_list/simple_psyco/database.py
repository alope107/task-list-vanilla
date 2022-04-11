import atexit
import psycopg2

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
            rows = cur.fetchall()
            self._db.commit()
        finally:
            cur.close()
        return rows