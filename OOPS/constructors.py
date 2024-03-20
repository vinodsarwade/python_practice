#constructor is a special method in a class used to create and initialize an object of a class.
#constructor is invoked(called) autometically when a obejct of a class is created.
#constructor always return none.
#used to initialize a value
#when object is created constructor always called first.

#ex:
class person:   #class
    def __init__(self, name, occ):  #constructor with 2 parameter name and occ 
        print("constructor is called !!")
        self.name = name   #data members
        self.occ = occ 

    def info(self):    #methods
        print(f"{self.name} is a {self.occ}")

a = person("shyam","developer")  #object
b = person("vinod","consultant") 

a.info()  #method calling using object
b.info()



#default constructor - which doesnt have any parameter only self is there
#parameterized constructor- which has parameter(above example)

class Addition:
	first = 0
	second = 0
	answer = 0

	# parameterized constructor
	def __init__(self, f, s):
		self.first = f
		self.second = s

	def display(self):
		print("First number = " + str(self.first))
		print("Second number = " + str(self.second))
		print("Addition of two numbers = " + str(self.answer))

	def calculate(self):
		self.answer = self.first + self.second


# creating object of the class
# this will invoke parameterized constructor
obj1 = Addition(1000, 2000)

# creating second object of same class
obj2 = Addition(10, 20)

# perform Addition on obj1
obj1.calculate()

# perform Addition on obj2
obj2.calculate()

# display result of obj1
obj1.display()

# display result of obj2
obj2.display()


