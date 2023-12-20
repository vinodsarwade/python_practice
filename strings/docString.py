#doc string is written at right below the function name or above the function body,
#doc string it is a snippet that will tell info about function.it is not a comment, and doc string will not be ignored by python interpreter.

def square(n):
    '''takes in a number n,returns square of n''' #doc string
    print(n**2)
    # print(n)
square(5)
print(square.__doc__) #printing doc string
    

