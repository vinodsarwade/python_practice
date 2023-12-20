# #recursion is a process of defining something in terms of itself
# #we can call a function in same function itself

# #ex: Factorial
def factorial(n):
    if(n==0 or n==1):
        return 1
    else:
        return n * factorial(n-1) # factorial function is called again itself

print(factorial(5))

# # #ex:Fibonacci series using recursion
def fibonacci(n):
    if (n==0 or n==1):
        return 1
    else:
        return fibonacci(n-1)+fibonacci(n-2)
print(fibonacci(6))


# #fibonacci using  while loop(practice)
def fibonacci(n):
    num1 = 0
    num2 = 1
    count = 0
    while (count <= n):
     num1,num2=num2,num1+num2    # ex 2, 3 = 3, 5
     print(num2)                 # ex 3, 5 = 5 , 8
     count += 1
fibonacci(8)


    