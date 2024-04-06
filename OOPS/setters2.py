# class Person:
#     def __init__(self, name, age):
#         self._name = name
#         self._age = age
    
#     # Getter method for name
#     def get_name(self):
#         return self._name
    
#     # Setter method for name
#     def set_name(self, name):
#         self._name = name
    
#     # Getter method for age
#     def get_age(self):
#         return self._age
    
#     # Setter method for age
#     def set_age(self, age):
#         if age >= 0:
#             self._age = age
#         else:
#             print("Age cannot be negative.")
    
# # Creating an instance of Person
# person = Person("Alice", 30)

# # Using getters to access the attributes
# print("Name:", person.get_name())
# print("Age:", person.get_age())

# # Using setters to modify the attributes
# person.set_name("Bob")
# person.set_age(25)  

# # Checking the modified attributes
# print("Updated Name:", person.get_name())
# print("Updated Age:", person.get_age())


class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    
    def get_name (self):
        return self.name
    
    def get_age(self):
        return self.age
    
    def set_name(self,name):
        self.name= name
    
    def set_age(self,age):
        self.age = age

obj = Person("vinod",24)

print("name is:",obj.get_name())
print("age is:",obj.get_age())

#for setters

obj.set_name("vishal")
obj.set_age(26)

print("updated age is:",obj.get_age())
print("updated name is:",obj.get_name())

