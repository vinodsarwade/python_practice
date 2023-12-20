#typecasting in python 
#conversion of one data type in to another data type  is known as type conversion or typecasting.
#python supports a wide varity of function and methods like set(), list(), dict(),ord(),int(),float(),str(),tuple()for the typecasting in python.

a =  "1"  #  2 str need to add so first need to convert it into int so use typecasting
b = "2" 
print(int(a)+int(b))

# explicit typecasting :- which is done by programmer explictly.
# implicit typacasting:- in python every data type it's leval .some are lower leval and some are higher leval .while performing operation
#python interprator convert it to required leval implicitely. ...

c= 2.4          #implicit typecast, python convert autometically int to float 
print(type(c))
d= 4
print(type(d))

print((c)+(d))