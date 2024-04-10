class Vector:
    def __init__(self,i,j,k):
        self.i = i
        self.j = j
        self.k = k
    
    def __str__(self):
        return f"{self.i}i + {self.j}j + {self.k}k"
    
    def __add__(self, x):
        return Vector(self.i + x.i, self.j + x.j, self.k + x.k)

v1 = Vector(3,5,7)
print(v1)

v2 = Vector(1,4,5)
print(v2)

print(v1 + v2)

'''Operator overloading in Python refers to the ability to define custom behavior for built-in operators such as +, -, *, /, ==, !=, <, <=, >, >=, etc., 
for user-defined classes. This allows instances of those classes to work with these operators just like built-in types such as integers, strings, and lists.'''

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    def __add__(self, other):
        """Overloading the + operator"""
        return Point(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        """Overloading the - operator"""
        return Point(self.x - other.x, self.y - other.y)

    def __eq__(self, other):
        """Overloading the == operator"""
        return self.x == other.x and self.y == other.y

    def __str__(self):
        """String representation of the Point object"""
        return f"({self.x}, {self.y})"

# Creating two Point objects
point1 = Point(1, 2)
point2 = Point(3, 4)

# Using overloaded operators
sum_point = point1 + point2
diff_point = point2 - point1
equality = point1 == point2

print("Sum of points:", sum_point)  # Output: (4, 6)
print("Difference of points:", diff_point)  # Output: (2, 2)
print("Equality of points:", equality)  # Output: False
