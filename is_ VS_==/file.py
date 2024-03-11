# 'is' keyword is used to compare exact location of object in memory 
# '=='  it will used to compare value present in memory


a = "vinod"
b = "vinod"   

print(a is b) #exact location of object in memory
print(a == b) # value


a = "vinod"
b = "vishal"   

print(a is b) #exact location of object in memory
print(a == b)


a = [1,2,3,4]
b = [1,2,3,4]  

print(a is b) #at this time it gives false bcz python will understand list have multiple objectso it has many location in memory and location could be chnaged .that is list is mutable to it gives false  for 'a is b'
print(a == b)# but vlaue for list is same so it gives true