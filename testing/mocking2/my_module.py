import argparse
import sys

from my_module2 import Database

db = Database()


class Employee:

    def __init__(self, lang, name='abbas'):
        self.lang = lang
        self.name = name

    def salary(self):
        salary = db.get_salary(self.name)
        if salary > 0:
            return ', salary is: {}'.format(salary)
        else:
            return ' not found'

    def get_name(self):
        return self.name

'''
def main():
    parser = argparse.ArgumentParser('Get employee data')
    parser.add_argument('-n', '--name', help='Enter emp name', required=True)
    parser.add_argument('-l', '--lang', help='Emp language', required=True)
    args = parser.parse_args()

    emp = Employee(args.name, args.lang)
    salary = emp.salary()
    print '{} {}'.format(args.name, salary)

if __name__ == '__main__':
    sys.exit(main())

'''


class Employee2:
    emp1 = Employee('Rayan', 'Soft Eng')

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_emp(self):
        emp = self.db_get_emp()
        print 'emp ############################: name: {}, id: {}'.format(emp.name, emp.id)
        print emp.name
        return emp

    def db_get_emp(self):
        return 'ishtiaq'

    def get_emp1_sal(self):
        sal = self.emp1.salary()
        return sal