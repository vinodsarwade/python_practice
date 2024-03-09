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

