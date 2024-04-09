'''method overriding means  a class has a same method same name but differnt in parameter called method overrding.'''
class Shape:
    def __init__(self,x ,y):
        self.x = x
        self.y = y
    
    def area(self):
        return self.x * self.y
    
class Circle(Shape):
    def __init__(self,radius):
        self.radius = radius
        super().__init__(radius,radius)

    def area(self):
        return 3.14 * super().area()
    
c = Circle(5)
print(c.area())


'''Method overriding in Python refers to the ability of a subclass to provide a specific implementation of a method that is already defined in its superclass.
 When a method in a subclass has the same name and signature as a method in its superclass, it overrides the superclass method.'''

class Animal:
    def make_sound(self):
        print("Some generic sound")

class Dog(Animal):
    def make_sound(self):
        print("Woof!")

class Cat(Animal):
    def make_sound(self):
        print("Meow!")

animal = Animal()
dog = Dog()
cat = Cat()

animal.make_sound()  # Output: Some generic sound
dog.make_sound()     # Output: Woof!
cat.make_sound()     # Output: Meow!


    