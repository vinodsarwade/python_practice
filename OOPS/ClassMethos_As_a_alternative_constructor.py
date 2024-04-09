
class Employee:
    def __init__(self,name,salary):
        self.name = name
        self.salary = salary

    @classmethod
    def fromStr(cls,string):
        return cls(string.split("-")[0],int(string.split("-")[1]))

e1 = Employee("vinod",232232) #normal method
print(e1.name)
print(e1.salary)

string ="John-12737"  #class method
e2 = Employee.fromStr(string)
print(e2.name)
print(e2.salary)


#example 2
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age

    @classmethod
    def from_string(cls,string):
        name ,age = string.split(',')
        return cls(name ,int(age))

    
obj = person.from_string("john doe, 30")
print(obj.name,obj.age)



#example 3
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @classmethod
    def create_from_birth_year(cls, name, birth_year):
        current_year = 2024  # Assuming the current year is 2024
        age = current_year - birth_year
        return cls(name, age)

# Using the constructor
person1 = Person("Alice", 30)
print(person1.name, person1.age)  # Output: Alice 30

# Using the class method
person2 = Person.create_from_birth_year("Bob", 1990)
print(person2.name, person2.age)  # Output: Bob 34


'''Constructor (__init__ method):
The constructor in Python is typically defined using the __init__ method within a class.
It's automatically called when you create a new instance of the class.
It's primarily used for initializing instance variables and performing any setup needed for the object.

Class Method:
A class method is a method that is bound to the class rather than the instance of the class.
It's defined using the @classmethod decorator.
Class methods receive the class itself as the first argument, conventionally named cls.
They can be called on either the class (e.g., ClassName.method()) or on an instance of the class (e.g., instance.method()).'''