'''*args is a function arguments used when you need to pass multiple arguments to function.
for that we dont need to call/ or pass parameter in function many time.
using *args it will accept unlimited arguments  '''

def add(*args):
    result = 0
    for i in args:
        result =  result + i
    print(result)

#here in case we can add unlimited argd in add fun. and it will return addition.
add(2,3,4)