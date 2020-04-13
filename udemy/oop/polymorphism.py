# sharing of the same method name by different objects of the different classes
#The benefit is iteration
#commonly used in abstraction and inheritance

class Dog():

    def __init__(self, name):
        self.name = name
    
    def sounds(self):
        return (self.name + ' sounds woof!')


class Cat():

    def __init__(self, name):
        self.name = name
    
    def sounds(self):
        return (self.name + ' sounds meow!')


my_dog = Dog('Moto')
my_cat = Cat('Niki')

for pet in [my_cat, my_dog]:
    print(pet.sounds())


print('*******************************************************')

def pet_sounds(pet):
    print (pet.sounds())


pet_sounds(my_dog)
pet_sounds(my_cat)

