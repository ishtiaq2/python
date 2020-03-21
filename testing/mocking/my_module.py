class MyCalc:

    total = 4
    name = 'ishtiaq'

    def add(self, a, b):
        self.a = a
        self.b = b
        return self.a + self.b

    
    def sub(self, a, b):
        self.a = a
        self.b = b
        return self.a - self.b


    def get_total(self):
        self.response = MyCalc.total
        return self.response
    
    
    def foo(self, y):
        x = self.db_write(y)
        return x

    def db_write(self, x):
        return 10


    def foo_str(self, x):
        return x

    def get_name():
        return name

    
class Student:

    def callable(self, x):
        return 'temp'






########################################################################################## 2
def exception_handling(a, b):
    try:
        return a/b
    except Exception as e:
        raise ZeroDivisionError('Division by zero')


def raise_value_error():
    raise ValueError('Some error text')

############################################################################################## 3

class MultipleMatcher:
    
    def __init__(self, factor):
        self.factor = factor


    def __eq__(self, other):
        return other % self.factor == 0
        
        
    def __repr__(self):
        return 'Multiple of {}'.format(self.factor)

#mul_mat = MultipleMatcher(6)
#print mul_mat


#################################################################################################### 4

class User:

    def __init__(self):
        self.is_birthday = False
    
    def birthday(self):
        return self.is_birthday

    def greet(self):
        if self.is_birthday:
            return 'Happy Birthday!'
        raise Exception('No Birthday!')


####################################################################################################### 5
