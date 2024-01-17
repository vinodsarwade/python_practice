##with range
for i in range(5):
    print(i)
else:
    print("sorry no i")

#with empty list
for i in []:
    print(i)
else:
    print("list is empty")

##
for i in range(6):
    print(i)
    if i == 4: # in this case we are using if in for loop and break if i ==4,
        break    #once i == 4 then break the loop and else statement is not exicute bcz loop has break susscesfully
else:
    print("sorry no i")

## with while loop
i = 0 
while i < 7:
    print(i)
    i = i + 1
    if i == 4: #if i comment this break then else also exicute
        break
else:
    print("else exicuted")


###
for x in range(5):
    print("iteration no {} in for loop".format(x+1))
else:
    print("else block in loop")

print("out of the loop")


