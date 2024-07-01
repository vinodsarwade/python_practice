
names = ["vinod","sarwade","techgun", 1,2,3,"CG"]
'''if i need to unpack this list items and store in a seperate variable '''

# first = names[0]
# second = names[1]
# third = names[2]
# #like wise we can do in a normal way
# print(first,second,third)


# first , second, third = names
# print(first,second,third) # it will gives you error bcz in list we have 6 items but we storing only 3 


first , second, third ,*list2,fourth = names
print(first,second,third,list2,fourth)
'''in *list2 it will store remaining all items bcz we used * '''
#but here in this  case we are storing one 'CG' elemet of list also so compiler first reserve one last variable to that element
# and remain all in *list2 . if there is no var after * then it will store all elements in *list2