name = "vinod"
print("hello, "+name)

fullName= "hello all my name is vinod sarwade "
print(fullName)

address= "hello all am good"
"what about you"
print(address)         # it will print only string present in first line.

address='''hello all am good
what about you
how are you'''
print(address)      # it will print both  string present in line1 and line2. use 3 ''' colon for multi line string

#to print each charactor of string  for name variable
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[4])
# print(name[5])  #it will throw error bcz name has only 4 index if trying to print got error 


# for printing multiple lines of strings charactor then it is not possible to use indexins bcz we don't know how many
#charactor are present and spaces in string 
#for we can use for loop to print

print("\n using for loop")
for charactor in address:
    print(charactor)   #it will print all the charactor with spaces and new line .