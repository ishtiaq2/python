import argparse
import sys

from my_module2 import database

class Employee:
    db = database()

    def __init__(self, lang, name='abbas'):
        self.lang = lang
        self.name = name
    

    def salary(self):
        salary = self.db.get_salary(self.name)
        if salary > 0:
            return ', salary is: {}'.format(salary)
        else:
            return ' not found'

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

    def __init__(self, name, role):
        self.name = name
        self.role = role

    def get_emp(self):
        emp = db_get_emp()
        
    def db_get_emp(self):
        return 'ishtiaq'


