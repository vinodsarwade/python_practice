'''in python the convention for indicating that is member is protectd is to be 
by prefixing it's name with single underscore(_).'''

""" the important to note that the single udnerscore is just a naming convention,and does not actually
provide any protection or restrict access to members. 
a syntax we followd for make any variable protected is to be prefix single underscore(_) with variable name.ie: _varName"""

class Student:
    def __init__(self):
        self._name = "vinod"
    
    def _funName(self):    #protected method
        return "VinodBadBoy"

class Subject(Student):  #inherited subclass 
    pass

obj = Student()
obj1 = Subject()

#calling by object from student class 
print(obj._name)
print(obj._funName())

#calling by object from subject class
print(obj1._name)
print(obj1._funName())



#if we want to use data from both parent as well subclass then we can create object for subclass
# subclass object will access data from parent as well it's own class


#it's depend on requirment like how you want to use class. if we want to use data from parent class only then we can make object for that .
# if we want to use data from bith class parent as well child class then we can make object for both class or we can make object for child class only 
#bcz it will access data from parent as well.