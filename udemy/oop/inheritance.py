class Animal():

    def __init__(self):
        print ('Animal created')
    
    def eat(self):
        print ('I am eating')

    def who_am_i(self):
        print ('I am an animal')


class Dog(Animal):

    def __init__(self):
        Animal.__init__(self)
        print ('Dog created')

my_dog = Dog()
my_dog.eat()
my_dog.who_am_i()

print('****************************************')
#Method Overriding

class Horse(Animal):

    def __init__(self):
        Animal.__init__(self)
        print ('Horse created')

    def eat(self):
        print ('I am eating grass')

    def who_am_i(self):
        print ('I am a horse')


my_horse = Horse()
my_horse.who_am_i()
my_horse.eat()

print('****************************************')
# extending by adding more method

class Horse(Animal):

    def __init__(self):
        Animal.__init__(self)
        print ('Horse created')

    def eat(self):
        print ('I am eating grass')

    def who_am_i(self):
        print ('I am a horse')

    def run(self):
        print ('I can run fast')


my_horse = Horse()
my_horse.who_am_i()
my_horse.eat()
my_horse.run()

