## map filter and reduce function are built in function that allows you to apply a function to a sequence  of elements 
## and return a new sequence. these fun are known as higher order funcion. as they take other function as a argument.

#  MAP  #
#map is used with list only
l = [1,2,4,6,7,8,9]
# newl = []
# for item in l:
#     newl.append(cube(item))   #insted of using for loop we can write like below.

newl = list(map(lambda x: x* x* x ,l))
print(newl)



# Filter

def filter_function(a):
    return a > 3
newnewl = list(filter(filter_function,l))
print(newnewl)


# reduce 
# to use reduce we need import it first otehrwise it will throw error
from functools import reduce 

numbers = [1,2,3,4,5,6]
# sum = reduce(lambda x ,y : x + y,numbers)  
###  above lambda function we can write like below as well

def mysum(x ,y):
    return x + y
sum = reduce(mysum,numbers)
print(sum)

