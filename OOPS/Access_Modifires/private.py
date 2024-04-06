'''in python there is no strict concept of private access modifires like in other language.
however it's convenction has been established to indicate that the variable and method be considered as a a private
by prefixing it's name with double underscore(__).'''

# class Employee:
#     def __init__(self,name):
#         self.__name = name  #__name is a private access modifore we can not access it like this it will throw error.

# a = Employee("vinod")
# print(a.__name)



'''to access private data in a class we can use name Mangling.
here in below case we are using _Employee it is a name mangling'''
class Employee:
    def __init__(self,name):
        self.__name = name

a = Employee("vinod")
print(a._Employee__name) #by doing this we can access private modifires also.