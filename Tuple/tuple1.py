tup = (12,27,31,57,68,"vinod",True)
print(type(tup),tup)

print(tup[4])
print(tup[5])


tup1 = (2,)
print(type(tup1),tup1) #it will print as a type of int bcz only 1 element so python get 
#confused for thatwe need tog= give quama ex: tup = (2,)

if 31 in tup:
    print("31 is present")

tup2 = tup[1:4]  #while slicing in tuple it will create new tuple
print(tup2)   #here in tup2 1-4 elements are added .
