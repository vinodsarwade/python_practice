'''in pyhton variables can be defined at the instance leval or the class leval.
instance variable are those variable which can assigned by using object of a class and we can chnage it using  perticular object/instance of class
but the class variable is not associated with object.it is independent and  ti will same throught the program.
if we want change class variable then need to make instnace/object that variable then we can chnage.'''

'''while running the code compiler first check instance . if instance is present for any var/ method then it will take that data as a instance  for var.
if instance/object is not present then the var is associated with only class.'''

'''class variable we usally defined outside of method.'''


class Employee:

    companyName = "Apple"  # here companyName is a class associated var,it is same throught the code untill and unless instance is created.

    def __init__(self,name):
        self.name = name  #here this name and increment are instance var.bcz we created object for same
        self.increment = 10

    def showDetails(self):
        print(f"name of emp is {self.name} and his increment is {self.increment}% in {self.companyName}")
    
 
emp1 = Employee("vinod")
emp1.increment = 20 #we are changing value of increment by creating instance so it's a instance variable.
emp1.showDetails() #here not creating instance for class var(ie:companyName) so it will take by default name.
# print(emp1.companyName)

emp2 = Employee("Rohan")
emp2.companyName = "Google" #here i have created instance for class variable ,so compiler first check instance var and update it. so here is no class var now.
emp2.showDetails()