'''magic methods are those methods are called when there is an event
ex: __init__() method is called when an object of class is created.
ex: __str__() method is called when you need to print object itself.'''


# #__init__ method
# class Humen:
#     def __init__(self, name , age):
#         self.name = name
#         self.age = age
#     def info(self):
#         return f"{self.name},{self.age}"

    
# obj = Humen("vinod", 24)
# print(obj.info())
# print(obj.name)


#__str__() method

'''in this case we cant print the object itself to print object we need to add __str__() method'''
class Humen:
    def __init__(self, name , age):
        self.name = name
        self.age = age
    # def __str__(self):
    #     return f"{self.name},{self.age}"

    
obj = Humen("vinod", 24)
print(obj)
