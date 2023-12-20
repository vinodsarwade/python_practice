#fucntion is a block of code that perform a specific task when it is called
#function it is used in code for reducing code size and length
#ex: if you want to add number each time then you need to add logic for that every time 
#rather than this we build a function for additing numbers and write logic in that, and called it whenever you want to use it 

#insted of writting logic every time we create a function named calculateGmin and write logic in it 
#and call it whenever you want.
def calculateGmin(a,b):
    mean = (a*b)/(a+b)
    print(mean)

a = 5
b = 10
# gmean = (a*b)/(a+b)
# print(gmean)
calculateGmin(a,b)  # calling the function

c = 8
d = 4
# gmean2 = (c*d)/(c+d)
# print(gmean2)
calculateGmin(c,d)       # calling the function