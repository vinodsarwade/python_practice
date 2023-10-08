
#list is a ordered collection of data items
#list items seperated by quamas and enclosed with square brackets. 
#list are changable / mutable
l = [12,20,30,44,52]
print(l)
print(type(l))
print(l[0])
print(l[1])

l = [20,21,67,"vinod",]  # we can add any data type in list
print(l[-3])    #negative indexing .to find negative index first find length of list then minus the index from len(list)
print(len(l))     # which will give you a easest way to find negative index
print(l[len(l)-3])   # this 4 lines of code has same output .
print(l[4-3])



#find elements in list
if 20 in l:
    print("yes")
else:
    print("no")

#find charactor in string which is in list
if "no" in "vinod":
    print("yes")
else:
    print("no")

