class Bird(object):
    def __init__(self):
        print("Bird")

    def whatIsThis(self):
        print("This is bird which can not swim")

class Animal(Bird):
    def __init__(self):
        super(Bird,self).__init__()
        print("Animal")

    def whatIsThis(self):
        print("THis is animal which can swim")

a1 = Animal()
a1.whatIsThis()

