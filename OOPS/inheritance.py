'''inheritance is a piller of opps  in which we ca create multiple classes which inherites the properties and methods
of it's parnts class, data members and methods of class autometically called once object is created'''


'''in inheritance child class will inherites all the properties from parent class so can call all the methods using object of child class.
  but we can not call methods of child class from parents class'''
class Employee: 
    def __init__(self,name,salary): #constructor
        self.name = name   
        self.salary = salary

    def show(self): 
        print("name of emp is :",self.name,"& salary is:",self.salary)

class Manager(Employee):  #child class or inherited class from parents class Employee
    def show_language(self): #methods of child class
        print("the defalult language of manager is python")
       
obj = Employee("vinod",40000)  #object 1
obj.show()      #object to called methods of parents class

obj2 = Manager("vishal",100000)  #object 2
obj2.show()       # here we can call show function as well bcz show method is in Employee class,all the properties and 
                   #methods are inherited using Manager class.so we can call it using child class object as well.
                # manager class will inherites properties from Employee class.
obj2.show_language()
           #but this show_language method we can't call from object of Employee Class.