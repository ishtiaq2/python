from db_module import EmployeeDB

class Employee:
    
    def __init__(self):
        self.emp_db = EmployeeDB()
        
    def fetch_db(self):
        db_con = self.emp_db.connect('json_file.json')
        cur = self.emp_db.execute('ishtiaq')
        row = self.emp_db.fetchall()
        print "id: {1}\nName: {0}\nRole: {2}" \
            .format(row["name"], row["id"], row["role"])

        


emp = Employee()
emp.fetch_db()