'''All the variables and methods in python are by default public.
Any instance variable in a class followed by the "self" keyword ie.self.var_name are public accessed.'''
class Employee:
    def __init__(self):
        self.name = "vinod"

obj= Employee()
print(obj.name)