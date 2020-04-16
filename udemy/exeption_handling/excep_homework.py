def find_square():
    list = ['a', 'b', 'c']
    try:
        for i in range(list):
            print (i ** 2)
    except TypeError:
        print ('Looks like you are trying input other than digits')
    

find_square()

print('************************************************************')

def zero_div(a, b):
    try:
        print ( a / b)
    except ZeroDivisionError:
        print ('divide by zero error')
    finally:
        print ('Done with zero_div')

zero_div(10, 0)


print ('*************************************************************')

def ask():
    while True:
        try:
            n = int(input('Plese enter a number: '))
        except TypeError:
            print ('Please try again')
            continue
        except ValueError:
            print ('Value error, please try again')
            continue
        else:
            s = n ** 2
            print ('square of {} = {}'.format(n, s))
            break
                

ask()