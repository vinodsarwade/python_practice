class MyClass:  #class
    def __init__(self,value) : #constructor
        self.value = value    #data members
    
    def show(self):   #method
        print(f"value is {self.value}")
    
    @property      #decorator
    def ten_values(self):
        return 10* self.value
    
    @ten_values.setter
    def ten_values(self, new_value):
        self.value = new_value/10

obj = MyClass(10)  #object

obj.ten_values = 67
print(obj.ten_values)
obj.show()     #method calling

        