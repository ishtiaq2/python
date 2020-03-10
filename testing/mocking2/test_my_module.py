import mock
import pytest
import my_module
from my_module2 import Database
from my_module import Employee, Employee2
import my_mock


emp = Employee('Python', 'ishtiaq')
emp2 = Employee2('ishtiaq-emp2', 'Dev-emp2')


class Obj:

    def __init__(self, name, id):
        self.name = name
        self.id = id


obj = Obj('Muqadas', 2)

'''
@mock.patch('my_module.Employee2.db_get_emp', return_value='abbas')
def test_get_emp1(self, ):
    assert my_module.Employee2.get_emp(emp2) == 'abbas'
'''

@mock.patch('my_module.Employee.get_name')
def test_get_emp2(mock_get_nm):
    mock_get_nm.return_value = 'Rayan'
    assert 'Rayan' == Employee.get_name()


@mock.patch.object(Database, 'get_salary', side_effect=my_mock.mocked_get_salary)
def test_salary(self, ):
    sal = emp.salary()
    args = sal.split(':')
    assert int(args[1].lstrip()) == 102


@mock.patch.object(Employee2, 'get_emp', side_effect=my_mock.mocked_get_emp)
def test_get_emp3(self, ):
    with pytest.raises(Exception) as e:
        assert emp2.get_emp() == 'isht'


@mock.patch.object(Employee, 'salary', side_effect=my_mock.mocked_emp1_salary)
def test_get_emp1_sal(self, ):
    assert emp2.get_emp1_sal() == 200


with mock.patch('my_module.Employee2.db_get_emp', return_value=obj) as my_mck:
    res = emp2.get_emp()
    print res.name
