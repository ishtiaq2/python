# Abstract classes are never expected to be instantiated, no object is created but just used as a base class
# You can have single base class to open files and different implementation (derived) classes to operate on 
# different type of files, e.g., csv, txt pdf etc, sharing the same open and close methods.


class Animal():

    def __init__(self, name):
        self.name = name

    def sounds(self):
        raise NotImplementedError('Subclass must implement this abastract method')


#my_animal = Animal('Niki')
#my_animal.sounds() #raise NotImplementedError('Subclass must implement this abastract method')
                            #NotImplementedError: Subclass must implement this abastract method


class Dog(Animal):

    def sounds(self):
        return self.name + ' sounds woof!'


class Cat(Animal):

    def sounds(self):
        return self.name + ' sounds meo!'


my_dog = Dog('Niki')
my_cat = Cat('Piki')

print (my_dog.sounds())
print (my_cat.sounds())




