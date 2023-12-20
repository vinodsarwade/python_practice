s1 = {1,2,5,6}
s2 = {3,6,7,5}

#UNION 
s3=(s1.union(s2)) #union ->result of two merge set.
print(s3)

#UPDATE
#if i want to update the set values from s1 to s2 or s2 to s1 then 
s1.update(s2) #s1 gets updated from s2's value
print(s1,s2) #those values are not present in s1. will take this value from s2 and update in s1


#UNION(it will combine all the value from both set)

cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
cities3 = cities.union(cities2)
print(cities3)

#INTERSECTION (combined same/duplicate value)
#common values that are present in both set 
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
cities3 = cities.intersection(cities2)
print(cities3)

#UPDATE intersection
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
cities3 = cities.intersection_update(cities2) # cities will update from intersection values from cities and cities2
print(cities)# common value getting updated in cities from both set


#SYMETRIC DIFFERENCE (different value are printed from both set,duplicate/same are ignored.,opposite to intersection)
cities = {"Tokyo","Madrid","Berlin","Delhi"}
cities2 = {"Tokyo","Seoul","Kabul","Madrid"}
cities3 = cities.symmetric_difference(cities2) 
print(cities3)