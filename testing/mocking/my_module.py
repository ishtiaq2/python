class MyCalc:

    total = 4

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
    
class Student:

    def callable(self, x):
        return 'temp'
