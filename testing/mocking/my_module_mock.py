def mock_mycalc_add(*args):
    
    value = args[0] * args[1] * 10   
    print'##########################'
    print 'mock add is called, returning: {}'.format(value)
    print'##########################'  
    return value


def mock_mycalc_sub(*args):
    return args[2]


def mock_get_total(y):
    return y + y


def mock_get_name():
    return 'Abbas'