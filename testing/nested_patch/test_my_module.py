'''
run as: pytest test_my_module.py -s
'''
import pytest
import mock
from my_module import Database, Car
import mocked_my_module as mck
import my_module

car = Car('Toyota', '2020')

@mock.patch.object(Car, 'get_car_data', side_effect=mck.mocked_db_get_data)
def test_get_car_data(self, ):
    data = car.get_car_data()
    assert data == {'Car': 'BMW'}


with mock.patch.object(Database, 'get_data', return_value={'Car': 'Lexus'}):
    assert my_module.open_function() == {'Car': 'Lexus'}

with mock.patch.object(Database, 'get_data') as mck_db_get_data:
    mck_db_get_data.return_value = {'Car': "Tesla"}
    assert my_module.open_function() == {'Car': 'Tesla'}    

with mock.patch('my_module.open_function', side_effect=mck.mocked_db_get_data) as mck_none:
    assert my_module.open_function() == {'Car': 'BMW'}


car2 = Car('temp', 'temp')
with mock.patch.object(Database, 'get_data') as mck_db_get_data:
    mck_db_get_data.return_value = {'Car': "Tesla"}
    with mock.patch.object(Car, 'get_car_data', side_effect=Database.get_data):
        assert car2.get_car_data() == {'Car': 'Tesla'}


with mock.patch('my_module.open_function', side_effect=car.get_car_data):
    assert my_module.open_function() == { 'Model': 'Corolla', "Year": 2020, 'Price': 100000 }


with mock.patch('my_module.open_function', side_effect=car.get_car_data):
    with mock.patch.object(Database, 'get_data') as mck_db_get_data2:
        mck_db_get_data2.return_value = {'Car': "Tesla1"}
        with mock.patch.object(Car, 'get_car_data', side_effect=Database.get_data):
            assert car2.get_car_data() == {'Car': 'Tesla1'}


with mock.patch('my_module.open_function', side_effect=car.get_car_data):
    with mock.patch.object(Car, 'get_car_data', side_effect=Database.get_data):
        with mock.patch.object(Database, 'get_data', return_value={'Car': "Tesla2"}) as mck_db_get_data2:
            assert my_module.open_function() == {'Car': 'Tesla2'}