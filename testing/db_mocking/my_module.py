from db_module import EmployeeDB

class Employee:
    
    def __init__(self):
        self.emp_db = None
        self.row = None
      
    def fetch_db(self, id):
        db_conn = EmployeeDB.connect('json_file.json')
        cur = db_conn.execute(id)
        self.row = cur.fetchall()
        print "id: {1}\nName: {0}\nRole: {2}" \
            .format(self.row["name"], self.row["id"], self.row["role"])
    
        db_conn.close()