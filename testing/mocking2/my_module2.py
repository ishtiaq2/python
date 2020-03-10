class Database:

    employees = ['ishtiaq', 'abbas', 'Rayan']
    salaries = [150000, 40000, 30000]

    def get_salary(self, name='Rayan'):
        if name in self.employees:
            salary = self.salaries[self.employees.index(name)]
        else:
            salary = 0
        return salary
