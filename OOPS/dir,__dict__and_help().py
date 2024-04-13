'''this methods are usefull in class. when you have to work with unknown class
and you want info about that class then you could use this methods to work with that class.'''

#dir() 
'''the dir() function returns a list of all the attributes and methods(including dunder method)available for an object.
it is a usefull tool for what you can do with an object'''

x = [1,2,3,4]
print(dir(x))  # will get all the methods related to this list x



#__dict__
'''it will any data is in dictionary .here in below ex we get name and age attribute in a dict. form'''
class person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
obj = person("vinod",24)
print(obj.__dict__)


#help()
'''by using this help() method we get discription of all the attributes.
using this we can get documentation also'''

print(help(person))
