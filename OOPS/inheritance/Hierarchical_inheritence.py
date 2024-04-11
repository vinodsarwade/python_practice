'''
Hierarchical inheritance is a type of inheritance in object-oriented programming where multiple derived classes (subclasses) 
inherit from a single base class (superclass). This creates a hierarchy where one superclass has multiple subclasses.'''

class Shape:
    def draw(self):
        print("Drawing a shape")

class Circle(Shape):
    def draw(self):
        print("Drawing a circle")

class Rectangle(Shape):
    def draw(self):
        print("Drawing a rectangle")

class Triangle(Shape):
    def draw(self):
        print("Drawing a triangle")

# Create instances of each subclass
circle = Circle()
rectangle = Rectangle()
triangle = Triangle()

# Call draw method for each subclass
circle.draw()     # Output: Drawing a circle
rectangle.draw()  # Output: Drawing a rectangle
triangle.draw()   # Output: Drawing a triangle
