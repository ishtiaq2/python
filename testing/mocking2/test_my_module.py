import mock
import pytest
import my_module
from my_module2 import database
from my_module import Employee
import my_mock


emp = Employee('Python', 'ishtiaq')

@mock.patch.object(database, 'get_salary', side_effect=my_mock.mocked_get_salary)
def test_salary(self, ):
    sal = emp.salary()
    args = sal.split(':')
    assert int(args[1].lstrip()) == 100

@mock.patch('my_module.Employee2.db_get_emp', mock.MagicMock(return_value='ishtiaq'))
def test_db_get_emp():
    assert my_module.Employee2.db_get_emp() == 'ishtiaq'