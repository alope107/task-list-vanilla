class Goal:
    db = None

    def __init__(self, id, title, due_date):
        self.id = id
        self.title = title
        self.due_date = due_date

    @classmethod
    def create_and_insert(cls, title, due_date=None):
        cur = cls.db.cursor()
        cur.execute("""INSERT INTO Goal(title, due_date)
                       VALUES (%s, %s) 
                       RETURNING id""", (title, due_date))
        id = cur.fetchone()[0]
        cls.db.commit()
        cur.close()
        return cls(id, title, due_date)

    @classmethod
    def fetch_all(cls):
        cur = cls.db.cursor()
        cur.execute("""SELECT id, title, due_date
                       FROM Goal""")
        rows = cur.fetchall()
        goals = []
        for id, title, due_date in rows:
            goals.append(cls(id, title, due_date))
        cur.close()
        return goals

    def __repr__(self):
        return f"Goal({self.id}, {self.title}, {self.due_date})"