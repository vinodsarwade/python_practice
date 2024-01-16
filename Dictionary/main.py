# key value pair combination  mostly used for mapping
dict = {
    "vinod":133,
    "shyam":233,
    "parth":333
    }
print(dict["parth"]) # it will five id of parth
print(dict) #will print whole dictionary.

info = {"name":"vinod","age":19,"eligible":True}
print(info)
print(info.get('name')) # it will return value  of key which we want to print.

info = {"name":"vinod","age":19,"eligible":True}
print(info)
print(info.get('name2')) #it will print none bcz name2 is not a key in info
#if we didnt use .get then it will throw an error but using get it wll print none.


info = {"name":"vinod","age":19,"eligible":True}
print(info.keys()) #print all the keys from info dict.


info = {"name":"vinod","age":19,"eligible":True}
print(info.values()) #print values forn dict.

print(info.items())# it will print all items in dict.


for key in info.keys(): # we can print values usinf for loop also 
    print(f"the values corrosponding to keys {key} are {info[key]}") # it will print values of corrosponding keys




