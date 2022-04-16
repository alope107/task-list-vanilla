import importlib.resources as pkg_resources
import sys

from app import schemas
from app.simple_psyco.database import Database

def main():
    if len(sys.argv) != 3:
        print('Usage: python create_schema.py DBNAME USER')
    
    create_schemas = pkg_resources.read_text(schemas, 'schemas.sql')
    
    dbname, user = sys.argv[1:]
    db = Database(dbname, user)
    db.clear_db()
    db.query(create_schemas)
    print('Database cleared and new schemas created!')


if __name__ == '__main__':
    main()
