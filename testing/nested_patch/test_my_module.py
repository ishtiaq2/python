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


with mock.patch('my_module.open_function') as mck_car:
    with mock.patch('my_module.db', side_effect=mck.mocked_db_get_data) as mck_db:
        data = my_module.open_function()
        print 'hello {}'.format(data)
        #assert data == {'Car': 'BMW'}
