
# num= int(input("enter a number: "))
# fact = 1

# if num < 0 :
#     print("does not exist")
# if num == 0 :
#     print("fact of o is 1")
# if num > 0:
#     for i in range(1,num+1):
#         fact = i * fact
# print(fact)

'''using recursion'''
def fact(a):
    if a == 0:
        return 1
    else:
        return((a)*fact(a-1))
num = int(input("enter number: "))
result = fact(num)
print(result)
    