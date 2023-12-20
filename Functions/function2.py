
def calculateGmean(a,b): 
    mean = (a*b)/(a+b)
    print(mean)


def isGreater(a,b):      
    if (a > b):
        print("first number is greater")
    else:
        print("second number is greater")

def isLesser(a,b):      # created a function isLesser but i need to write it after some time . but for now i need to run code now 
    pass               # but python given indentation error bcz the function has no body. so for 
                      #to avoid this need to use "pass" keyword it will say like ...we can pass or go to next function /line of code.
a =  10
b = 15

calculateGmean(a,b)
isGreater(a,b)


c = 40 
d = 30
# if (c > d):
#     print("first number is greater!")
# else:
#     print("second number is greater")
calculateGmean(c,d)
isGreater(c,d)