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
    
    
