#lambda is a anonymous function which is defined using lambda keyword.
#lambda function is mostly used  when we want to pass function as a argument
#and also used for single liner function.
#also we can pass function as a function.

def double(x):
    return x * 2
print(double(5))

#using lambada we can write above function like below
double = lambda x: x * 2  #we can write function like a variable that is "lamdda X:" and it will return "X * 2"
print(double(5))


def apply(fx, value):
    return 6 + fx(value) #here we return 6 + cube(2) = 14

cube = lambda x: x * x * x
avg = lambda x , y, z:(x + y + z)/2


print(cube(5))
print(avg(3,5,10))

print(apply(cube, 2)) # here we are passing  cube function and 2 as a argument to apply function.
print(apply(lambda x: x * x * x,2)) # above same we can wrote like this also




 #syntax -->lambda arguments: expression
'''lambda: This keyword is used to define a lambda function.
arguments: These are the input parameters to the function.
expression: This is the single expression or operation that the function performs. 
            The result of this expression is implicitly returned.'''

add = lambda x, y: x + y
print(add(3, 5))  # Output: 8


numbers = [1, 2, 3, 4, 5]
squared = list(map(lambda x: x**2, numbers))
print(squared)  # Output: [1, 4, 9, 16, 25]
