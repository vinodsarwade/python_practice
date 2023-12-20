#append
l =[1,2,4,6]
l.append(7)
print(l)

#sort
lst =[12,434,2,5,32,6,45]
lst.sort()  #assending order
print(lst)
lst.sort(reverse=True)  # decending order
print(lst)
#sort list of stings
lst = ["vinod","darshan","shyam","parth"]
lst.sort()
print(lst)

# reversing list
lst = ["vinod","darshan","shyam","parth"]
lst.reverse()
print(lst)

#index
lst=[2,34,43,13,454,665,13,33,54,1,32,43,13,13]
print(lst.index(13)) #will find index of 13 

#count
print(lst.count(13)) #count no of times 13 will occur in list

#copy
m = lst.copy() #will copy whole list as it is
m[0]=0
print(lst)

m = lst
m[0]=0  #store list in m and element present at index 0th is replace by 0
print(lst)

#insert
lst.insert(1,899) #insert 899 at 1st index in list.
print(lst)

#extend
m = [900,1000,1100]
lst.extend(m) #it will append list m at the end of list lst./extends list lst by adding list m at end
print(lst)

k = lst + m
print(k)  #will add two list
