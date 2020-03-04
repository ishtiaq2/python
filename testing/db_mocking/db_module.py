import json


class EmployeeDB:

    def __init__(self):
        self.emp_data = None
        self.row = None

    def connect(self, db_file):
        with open(db_file) as json_file:
            self.emp_data = json.load(json_file)
            
    def execute(self, query):
        for emp in self.emp_data['employees']:
            if emp['name'] == query:
                self.row = emp

    def fetchall(self):
        return self.row
