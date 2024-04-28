'''using for loop'''

num = int(input("enter a number: "))
sum = 0
if num <= 0:
    print("enter a positive integer")
for i in range(1,num+1):
    sum = sum + i
print(sum)



'''using while loop'''
num = int(input("enter a number: "))
sum = 0
if num <= 0:
    print("enter a positive integer")
else:
    sum = 0
    while num > 0:
        sum = sum + num
        num = num - 1  
    print(sum)

