#fib series using recurssion
def fibonnaci(n):
    if n <= 1:
        return n 
    else:
       return fibonnaci(n -1) + fibonnaci(n -2) 

length = 20
for i in range(length):
    print(fibonnaci(i))
    




#fib series for find  n'th fib number
def fib(n):
    a = 0
    b = 1

    if n < 0:
        print("enter greater number")
    elif n == 0:
        return a
    elif n == 1:
        return b
    else:
        for i in range(2,n+1):
            c = a + b
            a = b
            b = c
        return b
    
print (fib(5))





