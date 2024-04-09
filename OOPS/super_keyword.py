'''used to refer to the parent class.
by using super keyword we can directly access the methods of parent class from child class.'''
class Employee:
    def __init__(self,name,id):
        self.name = name
        self.id = id

class Programmer(Employee):
    def __init__(self,name,id,lang):
        # self.name = name             #here this name and age methods are already have in my parent class.then whay i can repeat it in my child class
        # self.age = age               #so i just use super keyword to take attributes from parent clsss and just give parameters.
        super().__init__(name,id)        #by using this we dont need to write repeated code.code if flexible,less and nonrepeatable. 
        self.lang = lang
    

rohan = Employee("rohan","43431")
vinod = Programmer("vinod","2324","pyhton")

print(vinod.name)
print(vinod.id)
print(vinod.lang)


