'''static methods in python are methods that belongs to a class rather than an instnace of a class
they are defined using @staticmethod decorator and do not have the access to the instance of a class.(ie:self)
they are called on the class itself, not on an instance of a class.
static methods are often used to  create utility function that don't need access from instance data.'''

class Math:
    def __init__(self,num):
        self.num = num

    def addToNum(self, n):
        self.num = self.num + n
    
    @staticmethod
    def add(a,b):
        return a + b
    
a =  Math(5)
print(a.num)
a.addToNum(8)
print(a.num)


print(Math.add(7, 2))  #in static method we didnt any instace of a class we can call using Math. add .
# print(a.add(7,2))  #or we can do like this also

# print(add(2,7))   #we can  call like this also(like a normal fun calling),but the add function need to be outside of a class.
                   # here in above case add method is within the class so we can not call like this.
