
'''dunder methods are those methods who starts with __ and ends with __
ex: __init__ , __len__,__str__
while using we can use like "__len__" but when we create instance then we get it using "len" only,
 we didnt require '__' here. so it's called as magic method or dunder method.'''


# class Employee:
#     name = "vinod"
#     def __len__(self):
#         i = 0
#         for char in self.name:
#             i = i + 1
#         return i

# obj = Employee()
# print(obj.name)
# print(len(obj))


#1) __init__() -->   it is act as a constructor.

#2)__str__ and __repr__
'''str for string and repr for represent
'''

#i have created instance for this file in emp.py file bcz sometimes we have to work with packages and we dont
#know what code in the file. if that time if we need to print something then we can use  __str__ method.
# if we dont use __str__ then it will print garbage data 

class Employee:
    def __init__(self,name):
        self.name = name

    def __len__(self):
        i = 0
        for char in self.name:
            i = i + 1
        return i
    def __str__(self): # ir will gives us string formation of data in emp.py file
        return(f"name of emp is {self.name}")
    
    def __repr__(self):
        return f"Employe ({self.name})"
    
    def __call__(self):
        print("hey am good")
    



# #example by AI
# '''__str__ method:
# This method is called when the str() function is used or when an object is used in a string context (like when printing).
# It should return a string that is easy to read and understand for humans.
# It's generally used for creating informal or nicely formatted string representations of objects.'''
# class Person:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age
    
#     def __str__(self):
#         return f"Person: {self.name}, Age: {self.age}"

# person = Person("Alice", 30)
# print(str(person))  # Output: Person: Alice, Age: 30


# '''__repr__ method:
# This method is called when the repr() function is used or when an object is used in an interactive Python shell.
# It should return a string that represents a valid Python expression which could be used to recreate the object.
# It's generally used for debugging and development purposes.'''

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
    
#     def __repr__(self):
#         return f"Point({self.x}, {self.y})"

# point = Point(3, 4)
# print(repr(point))  # Output: Point(3, 4)

# ''' If __str__ is not defined, Python will fallback to __repr__.'''
