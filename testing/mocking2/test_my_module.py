import mock
import pytest
from my_module2 import database
from my_module import Employee
import my_mock


emp = Employee('ishtiaq', 'Python')

@mock.patch.object(database, 'get_salary', side_effect=my_mock.mocked_get_salary)
def test_salary(self, ):
    sal = emp.salary()
    args = sal.split(':')
    assert int(args[1].lstrip()) == 100

    