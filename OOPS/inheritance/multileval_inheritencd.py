'''in this inheritance one class is derived from it's parent class
and agin one more class id derived from child class.   class-->childclass-->subclass'''

class Animal:
    def __init__(self,name, species):
        self.name = name
        self.species = species

    def show_details(self):
        print(f"name is:{self.name}")
        print(f"the species is:{self.species}")

class Dog(Animal):
    def __init__(self,name ,breed):
        Animal.__init__(self, name,species="Dog")
        self.breed = breed
    
    def show_details(self):
        Animal.show_details(self)
        print(f"Breed:{self.breed}")

class GoldenRetriver(Dog):
    def __init__(self,name,color):
        Dog.__init__(self,name,breed="Doberman")
        self.color = color
    
    def show_details(self):
        Dog.show_details(self)
        print(f"color is:{self.color}")

obj = GoldenRetriver("tommy","Black")
obj.show_details()
        


#example 2 
class Animal:
    def speak(self):
        print("Animal speaks")

class Dog(Animal):
    def bark(self):
        print("Dog barks")

class Labrador(Dog):
    def color(self):
        print("Labrador is golden in color")

# Create an instance of Labrador
labrador = Labrador()

# Call methods from the Animal class
labrador.speak()  # Output: Animal speaks

# Call methods from the Dog class
labrador.bark()   # Output: Dog barks

# Call method from the Labrador class
labrador.color()  # Output: Labrador is golden in color
   

