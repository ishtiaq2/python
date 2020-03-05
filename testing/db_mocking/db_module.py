import json


class EmployeeDB:

    def __init__(self, db):
        self.db = db
        self.table = None
        self.row = None

    def load_db(self):
        with open(self.db) as json_file:
            table = json.load(json_file)
            return table

    @classmethod
    def connect(cls, db):
        return cls(db)

    def execute(self, query):
        self.table = self.load_db()
        for id in self.table['employees']:
            if id['id'] == query:
                self.row = id
        return self

    def fetchall(self):
        return self.row

    def close(self):
        self.table = None
