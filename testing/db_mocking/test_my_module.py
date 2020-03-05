import pytest
import mock
import my_module

emp = my_module.Employee()

@pytest.fixture(scope='function')
def setup_module():
    print '###########################'
    print '############ Setup ########'
    print '###########################'


def teardown_module():

    print '###########################'
    print '############ Teardown #####'
    print '###########################'
    

def test_fetch_db():
    emp.fetch_db(2)
    assert emp.row['id'] == 2
