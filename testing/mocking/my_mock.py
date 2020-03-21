import my_module
import pytest
import mock


my_mock = mock.Mock(usr='ishtiaq')
my_mock.usr2 = "Hussain"
my_mock.get_name()
my_mock.get_name.return_value = 'Muhammad Ishtiaq Hussain'
my_mock.get_name_of_usr()
my_mock.get_name_of_usr.return_value = my_mock.usr

print my_mock.usr, my_mock.usr2
print my_mock.get_name()
print my_mock.get_name_of_usr()

my_mock.get_name_of_usr.return_value = my_mock.usr2
print my_mock.get_name_of_usr()

mock_ex = mock.Mock()
mock_ex.side_effect = Exception
mock_ex.side_effect = lambda x: x ** 2
assert mock_ex(3) == 9
assert mock_ex(4) == 16
mock_ex.assert_called_with(4)
mock_ex.assert_has_calls([mock.call(3), mock.call(4)])
mock_mul_side_eff = mock.Mock()
mock_mul_side_eff.side_effect = [1, 2, ValueError, 3]
print mock_mul_side_eff()
# print mock_mul_side_eff()
print mock_mul_side_eff()
















##################################################################################################### 2
def test_exception_handling():
    with pytest.raises(ZeroDivisionError) as e:
        my_module.exception_handling(1, 0)
    assert 'Division by zero' in str(e.value)


def test_raise_value_error():
    with pytest.raises(ValueError) as ve:
        my_module.raise_value_error()
    #assert 'Some error tex' in str(ve.value)
####################################################################################################### 3

multiple_match_mock_func = mock.Mock()
multiple_match_mock_func(25)
multiple_match_mock_func.assert_called_with(my_module.MultipleMatcher(5))
multiple_match_mock_func(16)
multiple_match_mock_func.assert_called_with(my_module.MultipleMatcher(4))












####################################################################################################### 4
def test_greeting_1():
    user = my_module.User()
    with pytest.raises(Exception) as e:
        greeting = user.greet()
    assert e.value[0] == 'No Birthday!'

def test_greeting_2():
    user = my_module.User()
    user.greet = mock.Mock(return_value = 'Happy Birthday!')
    greeting = user.greet()
    assert greeting == 'Happy Birthday!'

def test_greeting_3():
    user = my_module.User()
    if not user.birthday():
        with pytest.raises(Exception) as e:
            greeting = user.greet()
        assert e.value[0] == 'No Birthday!'


def test_greeting_4():
    user = my_module.User()
    user.is_birthday = mock.Mock(return_value=True)
    greeting = user.greet()
    assert greeting == 'Happy Birthday!'

def test_greeting_5():
    user = my_module.User()
    user.birthday = mock.Mock(return_value=True)
    if user.birthday:
        with pytest.raises(Exception) as e:
            user.greet()
        assert e.value[0] == 'No Birthday!'

with pytest.raises(Exception) as e:
    user = my_module.User()
    user.greet()
assert e.value[0] == 'No Birthday!'


###################################################################################################### 5