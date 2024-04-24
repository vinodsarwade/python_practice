'''using variable'''
# num = int(input("enter a number: "))
# a = 0
# b = 1
# if num >= 1:
#     for i in range(2, num):
#         c = a + b
#         a = b
#         b = c
#         print(c)


'''using recursion'''
def fibonacci(n):
    if n <= 1:
        return n
    else:
        return (fibonacci(n-1) + fibonacci(n-2))

num = int(input("enter a number:"))
fibonacci(num)

for i in range(num):
    print(fibonacci(i))