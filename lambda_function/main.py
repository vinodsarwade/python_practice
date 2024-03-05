def double(x):
    return x * 2
print(double(5))

#using lambada we can write above function like below
double = lambda x: x * 2  #we can write function like a variable that is "lamdda X:" and it will return "X * 2"
print(double(5))


avg = lambda x ,y:(x + y)/2
print(avg(5,6))