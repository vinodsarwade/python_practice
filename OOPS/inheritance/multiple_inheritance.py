'''Multiple inheritance in Python refers to a class inheriting attributes and methods from more than one parent class.
 This means that a subclass can inherit from multiple superclasses. However, multiple inheritance can lead to complexities, 
 so it's essential to use it judiciously.'''


#here in multiple inheriteance sometimes ambiguity arises when if the two parent class has the same method name.
#here in below case in both Employee and dance class i have a method named show() which is same name in both class.
#when i created child class from this two parent class. due to same name it will just print the data in a single method.
class Employee:
    def __init__(self,name):
        self.name = name
    def show(self):
        print(f"name of emp is {self.name}")  

class dancer:
    def __init__(self,dance):
        self.dance = dance
    def show(self):
        print(print(f"he doing {self.dance}"))

class Employee_dancer(Employee,dancer): 
#here am taking  Employee class first as a parent class and then dancer class second
#when am calling show methods which is present in both class, it will print from employee class only.
#bcz we written it first in child class. it's a ambuguity.

    def __init__(self,name,dance):
        self.name = name
        self.dance = dance

obj = Employee_dancer("vinod","kathak")
print(obj.name)
print(obj.dance)

obj.show()

#to see which  class method is getting called first we can use mro() method.
#it will show you order of execution
print(Employee_dancer.mro())  



#'''example 2'''

class ClassA:
    def method_a(self):
        print("Method A from Class A")

class ClassB:
    def method_b(self):
        print("Method B from Class B")

class ClassC(ClassA, ClassB):
    def method_c(self):
        print("Method C from Class C")

# Create an instance of ClassC
obj = ClassC()

# Call methods from ClassA
obj.method_a()

# Call methods from ClassB
obj.method_b()

# Call method from ClassC
obj.method_c()
