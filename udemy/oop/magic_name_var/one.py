
def func():
    print ('Function inct ONE.PY')

print ('Top level in ONE.PY')

def func1():
    pass

def func2():
    pass

def func3():
    pass

if __name__ == '__main__':
    print('ONE.PY is being run directly')
    func1()
    func2()
    func3()

else:
    print('ONE.PY have been imported')