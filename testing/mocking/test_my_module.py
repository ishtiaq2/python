import pytest
import mock
from my_module import MyCalc
import my_module_mock as my_mock 


calc = MyCalc()

@mock.patch.object(MyCalc, 'add', side_effect=my_mock.mock_mycalc_add)
def test_add(self, ):
    assert calc.add(2, 2) == 40
    

@mock.patch.object(MyCalc, 'sub', side_effect=my_mock.mock_mycalc_sub)
def test_sub(self, ):
    assert calc.sub(2, 10, 20) == 20


@mock.patch.object(MyCalc, 'get_total', side_effect=my_mock.mock_get_total)
def test_get_total(self, ):
    assert calc.get_total() == 10