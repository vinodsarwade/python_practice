'''
*
* *
* * *
* * * * 
* * * * * 
'''
# for i in range(1, 6):
#     for x in range(1, i+1):
#         print("*", end = "")
#     print("")


line = 1
while line <= 5:
    star = 1
    while star <= line:
        print("*", end="")
        star = star + 1
    print("")
    line = line+1