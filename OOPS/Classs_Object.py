# class person:   #class
#     name = "vinod"     #data members
#     occupation = "software engineer"
#     age = 25 

# a = person()   #object
# print(a.name, a.occupation,a.age) #print


#example 2 using methods
class person:   
    name = "vinod"
    occupation = "software engineer "
    age = 25 
    def info(self): #methods
        print(f"{self.name} is a {self.occupation}")

a = person() #object 1
b = person()  #object 2
c = person() #object 3   #am not changing data using object c ,so it will print by default data which is given in class person.

a.name = "Shyam"   # here am changing tha data using object a
a.occupation = "Software engineer"

b.name = "nitika"
b.occupation = " HR"

a.info()  #calling to method  using object a
b.info()  #calling to method  using object b
c.info() 