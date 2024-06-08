def natural_number(n):
    sum = 0
    if n <= 1:
        return n
    else:
        return n + natural_number(n-1)
    

num = int(input("enter a number: "))
print(natural_number(num))