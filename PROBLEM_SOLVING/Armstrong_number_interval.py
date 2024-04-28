lower = int(input("enter a lower limit number: "))
upper = int(input("enter a upper limit number: "))

for num  in range(lower, upper):
    order = len(str(num)) 
    sum = 0
    temp = num
    while temp > 0:
        n = temp % 10 
        cube = n**order
        sum = sum + cube 
        temp = temp // 10  
    if sum == num:
        print(num)


