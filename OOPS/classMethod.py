'''class methods are the methods associated with class only
we can change variable of class using class method.'''

class Employee:
    company = "Apple" #class var
    def show(self):
        print(f"name is {self.name} and company name is {self.company}")

    def changeCompany(self,newCompany):
        self.company = newCompany


e1 = Employee()
e1.name = "Harry"  #here we passing name to class methods using instance. 
e1.show()

e1.changeCompany("tesla") # here we are changing company name  Apple to tesla  using instance.
e1.show()
print(Employee.company,"\n") # but the if we print comapny name then also it is showing Apple. bcz we are changing it using instance.
                        #class methods is not changed using instance we can change it for that specific method only. so it will show Apple only.
           
           
           #to change this use below code


#
class Employee:
    company = "Apple"
    def show(self):
        print(f"name is {self.name} and company name is {self.company}")

    @classmethod  #here we add classmethod decorator to change class var 
    def changeCompany(cls,newCompany):
        cls.company = newCompany   
    # at the place of 'cls' we can give self also or any name,first paramater is considered as default parameter.

e1 = Employee()
e1.name = "Harry"
e1.show()

e1.changeCompany("tesla") # now i am changing company name to tesla so it will print tesla.
e1.show()
print(Employee.company)  #and in class var also it can change tesla. bcz  we used  classmethod decorator here.