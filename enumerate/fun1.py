#enumeration fun is a built in function in python that allows you to loop/traverse over a 
#sequence (such as list,tuple,string)& get the index and value of each element in the 
# sequence at the same time.

marks = [12,56,32,12,45,1,4] #below this type of code is longer and inefficient we can use enum rather than this
index = 0
for mark in marks:
    print(mark)
    if(index == 3):
        print("vinod,awasome")
    index += 1



#enum example
marks = [12,56,32,12,45,1,4] 
for index, mark in enumerate(marks):
    print(mark)
    if(index == 3):
        print("vinod cool")

# in this above case index will start from 0 but we can change index also
#using start==1

marks = [12,56,32,12,45,1,4] 
for index, mark in enumerate(marks,start=1):
    print(mark)
    if(index == 3):
        print("vinod cool")


#ex 2
fruits = ["Apple","banana","Greps"]   # it will print all the list from 1st index to last
for index,fruit in enumerate(fruits,start= 1): #enumerate fun will give index of that element
    print(index ,fruit)


    
    

