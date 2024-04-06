


class MyClass:  #class
    def __init__(self,value) : #constructor
        self.value = value    #data members
    
    def show(self):   #method
        print(f"value is {self.value}")
    
    @property      #decorator
    def ten_values(self):
        return 10* self.value

obj = MyClass(10)  #object
obj.show()     #method calling
print(obj.ten_values)

        