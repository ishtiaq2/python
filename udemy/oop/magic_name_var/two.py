import one

def funct():
    print ('Function in TWO.PY')

print ('Top level in TWO.PY')

one.func()

if __name__ == '__main__':
    print('TWO.PY is being run directly')
else:
    print('TWO.PY have been imported')