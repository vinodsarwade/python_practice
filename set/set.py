#set is a collection of well defined objects 
#set has no repeated values, it is a unordered collection of values 
#it has a quama seperated values, set has no duplicate value
#set are not changable/immutable
#list - []
#tuple - ()
#set - {,}
#dic = {"":""}

s = {2,3,4,5,5,6,6,7} 
print(s)

info = {"carla",19,False,3,5.5}
print(info)
print(type(info))

average = {} # if we want to create empty set but it will create Dic using this.
print(type(average))

#to create empty set write like this
average = set() 
print(type(average))


#to access set value 
for i in info:
    print(i)



