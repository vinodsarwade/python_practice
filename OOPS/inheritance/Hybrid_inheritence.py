'''when two or multiple inheritence are combined then it's called hybrid '''
class BaseClass:
    pass

class DerivedClass1(BaseClass):
    pass
class DerivedClass2(BaseClass):
    pass

class subclass(DerivedClass1,DerivedClass2):
    pass



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

class GuideDog(Dog):
    def assist(self):
        print("Guide dog assists people")

class HybridLabrador(Labrador, GuideDog):
    pass

# Create an instance of HybridLabrador
hybrid_labrador = HybridLabrador()

# Call methods from the Animal class
hybrid_labrador.speak()  # Output: Animal speaks

# Call methods from the Dog class
hybrid_labrador.bark()   # Output: Dog barks

# Call method from the Labrador class
hybrid_labrador.color()  # Output: Labrador is golden in color

# Call method from the GuideDog class
hybrid_labrador.assist() # Output: Guide dog assists people
