'''A class inherites a properties and behaviour from a single parent class.
this is a simplest and most common type of inheritence.'''

'''syntax
Class Childclass(Parentclass):
class body '''

class Animal:
    def __init__(self,name,species):
        self.name = name
        self.species = species

    def make_sound(self):
        print("Sound made by animal")

class Dog(Animal):
    def __init__(self, name, breed):
        Animal.__init__(self,name,species="Dog")
        
        self.breed = breed
    
    def make_sound(self):
        print("bark")
    
d = Dog("tommy","doggerman")
# print(d.name)
d.make_sound()

a = Animal("robert","jangali")
a.make_sound()



