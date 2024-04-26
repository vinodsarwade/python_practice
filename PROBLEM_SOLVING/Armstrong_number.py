# num = int(input("enter a number: "))
# sum = 0
# temp = num
# while temp > 0:
#     n = temp % 10   #here we finding the last digit of a number using modulus logic.
#     cube = n**3    # once we get last digit we are finding it's cube and stored in cube.
#     sum = sum + cube # then we adding that cube in a sum 
#     temp = temp // 10  #we got cube of last digit so we need to pop out last digit so here we are using floor division method to pop out last digit

# if sum == num:
#     print("yes,it is a armstrong number ")
# else:
#     print("not a armstrong number")



'''if we need to find 4 digits of armstrong number'''

num = int(input("enter a number: "))
digits = len(str(num))  # need to find length and pass that length to cube
sum = 0
temp = num
while temp > 0:
    n = temp % 10   #here we finding the last digit of a number using modulus logic.
    cube = n**digits    # once we get last digit we are finding it's 4th order and stored in cube.
    sum = sum + cube # then we adding that cube in a sum 
    temp = temp // 10  #we got cube of last digit so we need to pop out last digit so here we are using floor division method to pop out last digit

if sum == num:
    print("yes,it is a armstrong number ")
else:
    print("not a armstrong number")