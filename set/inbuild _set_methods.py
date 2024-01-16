### isdisjoint() ###
#there is no match from both the sets,and there is no element is common from both sets.
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}# in this case it will print false bcz it has same city in both sets

print(cities.isdisjoint(cities2))

cities = {"Mumbai","Pune","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}# in this case it will print true bcz there is no common element from both sets.

print(cities.isdisjoint(cities2))

###  issuperset() ###
#if you have 2 sets,  and all the element in 2nd sets is present in set1 then set1 is superset of set2. and vise-varsa
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Seoul","Kabul"}
print(cities.issuperset(cities2)) #false bcz element is cities2 set, is not present in set1 so set1 not a superset of set2.

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Berlin","Delhi"}
print(cities.issuperset(cities2)) #true bcz set2's element is present in set1, so set1 is superset of set2.


### issubset() ### 
# is is opposite to superset, if set2's element is present in set1 then set2 is subset of set1.

### add() ###
#it is used to add a items in  existing set
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities.add("Mumbai")
print(cities)

### remove/discard() ### 
# to remove or discard items in sets
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities.remove("Tokyo")
print(cities)

### Pop ###
#pop out last element is set but due to set is unordered it will pop out any element in set.
cities = {"Tokyo","Seoul","Kabul","Madrid"}
item =cities.pop()
print(item) #print poped element
print(cities) #print remaining set

### clear() ###
# what if we dont want to delete enrire sets but want to delete only elements in the sets.
#then we can use clear method.
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities.clear() #clear all teh elements in sets, and show empty sets.
print (cities)

### del ### 
# delete is a keyword used to delete all set
# cities = {"Tokyo","Seoul","Kabul","Madrid"}
# del cities # set is deleted
# print(cities) #it will throw an error bcz above line we deleted set and then we are trying to print that deleted sets.
