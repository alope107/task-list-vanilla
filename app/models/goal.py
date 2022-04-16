class Goal:
    db = None

    def __init__(self, id, title, due_date):
        self.id = id
        self.title = title
        self.due_date = due_date

    @classmethod
    def create_and_insert(cls, title, due_date=None):
        result = Goal.db.query("""INSERT INTO Goal(title, due_date)
                                  VALUES (%s, %s) 
                                  RETURNING id""", (title, due_date))
        id = result[0][0]
        return cls(id, title, due_date)

    @classmethod
    def fetch_all(cls):
        rows = Goal.db.query("""SELECT id, title, due_date
                                  FROM Goal""")
        goals = []
        for id, title, due_date in rows:
            goals.append(cls(id, title, due_date))
        return goals

    def __repr__(self):
        return f"Goal({self.id}, {self.title}, {self.due_date})"