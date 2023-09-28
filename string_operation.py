#strings are immutable 
a = "vinod !!!!!!  vinod "

print(len(a))
print(a.upper())    #capital letters
print(a.lower())   # small letters
print(a.rstrip("!"))  # it will remove or strip the ! mark at the end only/...if ! is at starting it will not stripped.
print(a.replace("vinod","jhon"))  # it will replace vinod to jhon
print(a.split("  "))           #it will find a space between string and split it by quama.

name = "vinOd  RagHunath sarwade"
print(name.capitalize())  # it will capitalize the first charactor of string and all other char. converted in to small
                            # if the string is already in capitalize format then it will no affect on string.

print(a.count("vinod")) # count the number of times vinod word is occured in a varaible.

str1 = "hello all am going to school !!"
print(str1.endswith("!!"))   # check if the string is ending with !! if it is true then it will print true.

str1 = "there anyone whos name is vinod"
print(str1.find("is"))         #it will  first find the element is present or not if present then it will give index of that 
                           # if not present then it will give  -1 as output.

print(str1.index("is"))  # but in index if the element is present in string it will print index 
                          # but if it is not present it will throw error. 