class database:
    
    employees = ['ishtiaq', 'abbas']
    salaries = [50000, 40000]
    def get_salary(self, name):
        if name in self.employees:
            salary = self.salaries[self.employees.index(name)]
        else:
            salary = 0
        return salary