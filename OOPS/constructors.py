#constructor is a special method in a class used to create and initialize an object of a class.
#constructor is invoked(called) autometically when a obejct of a class is created.
#constructor always return none.
#used to initialize a value
#when object is created constructor always called first.

#ex:
class person:   #class
    def __init__(self, name, occ):  #constructor with 2 parameter name and occ 
        print("constructor is called !!")
        self.name = name   #data nenbers
        self.occ = occ 

    def info(self):    #methods
        print(f"{self.name} is a {self.occ}")

a = person("shyam","developer")  #object
b = person("vinod","consultant") 

a.info()  #method calling
b.info()



#default constructor - which doesnt have any parameter only self is there
#parameterized constructor- which has parameter(above example)

