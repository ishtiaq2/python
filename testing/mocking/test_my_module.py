import pytest
import mock
import my_module
import my_module_mock as my_mock 


calc = my_module.MyCalc()
std = my_module.Student()
'''
@mock.patch.object(MyCalc, 'add', side_effect=my_mock.mock_mycalc_add)
def test_add(self, ):
    assert calc.add(2, 2) == 40
    

@mock.patch.object(MyCalc, 'sub', side_effect=my_mock.mock_mycalc_sub)
def test_sub(self, ):
    assert calc.sub(2, 10, 20) == 20


@mock.patch.object(MyCalc, 'get_total', side_effect=my_mock.mock_get_total)
def test_get_total(self, ):
    assert calc.get_total() == 10

'''

@mock.patch.object(calc, 'db_write', side_effect=my_mock.mock_get_total)
def test_foo(self, ):
    x = calc.foo(10)
    assert x == 20

@mock.patch('my_module.MyCalc.total', new=20)
def test_get_total():
    x = calc.total
    assert x == 20