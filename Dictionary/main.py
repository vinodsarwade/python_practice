# key value pair combination  mostly used for mapping
dict = {
    "vinod":133,
    "shyam":233,
    "parth":333
    }
print(dict["parth"]) # it will print id of parth
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


for key in info.keys(): # we can print values using for loop also 
    print(f"the values corrosponding to keys {key} are {info[key]}") # it will print values of corrosponding keys



'''TECHGUN'''

#we can make dict using this below also
# dic1 = dict(name = "vinod", branch = "AI")

info1 = {
    "name":"vinod",
    "age":19,
    "eligible":True}

info1["name"] = "shyam"
info1["contact no"] = 354667676
print(info1)

#using if else we can check weather item is present or not
if "name" in info1 :
    print(info1["name"])


# or we can use  .get fun also to access elements in dict
print(info1.get("name"))


print(info1.get("mobile")) # here in this case "mobile" is not present in info1 dict so it will return None

print(info1.get("mobile", 44564539))# if we dont want to return None then we can pass default value.
                                    # if the item is not present then it will autometically take default item and return it. 
