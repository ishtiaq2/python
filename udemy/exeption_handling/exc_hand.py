def add_1(a, b):
    try:
        result = a + b
    except:
        print ('It looks like the values are not numbers')
    else:
        print ('adding {} + {} = {}'.format(a, b, result))



def add_2(a, b):
    try:
        result = a + b
    except Exception as e:
        print (e)
    else:
        print ('adding {} + {} = {}'.format(a, b, result))


'''
add_1(10, 20)
add_1(10, '20')

print ('**************************************************************')

add_2(10, 20)
add_2(10, '20')
'''

def write_to_file():
    try:
        f = open('testfile.txt', 'r') # introduce OSError by changing 'w' to 'r'
        f.write("Hi test file")
    except TypeError:
        print('There was a type error')
    except OSError:
        print ('There was an OS Error')
    finally:
        print ('finally always execute')


def read_from_file():
    try:
        f = open('testfile.txt', 'r')
        lines = f.readlines()
        for i in range(len(lines)):
            print (lines[i])
    except TypeError:
        print('There was a type error')
    except OSError:
        print ('There was an OS Error')
    finally:
        print ('finally always execute')


write_to_file()
# read_from_file()
