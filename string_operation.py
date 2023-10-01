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

str1 = "WelcomeToTheConsole"
print(str1.isalnum())  # it will check the string is alpha numeric or not and print true or false.

str1 = "welcome"    # if string has A-Z or a-z then  it will return true otherwisw false
print(str1.isalpha())

str1 = "Welcome22"   # it has 22 at last so it will return false
print(str1.isalpha())


str2 = "hello all "  # if all the element in string is in lower case then return true 
print(str2.islower())  # of any one element is capital then return false.

str1 = "we wish you a happy diwali"
print(str1.isprintable())  # if all the char in string is printable then return true 

str1 = "we wish you a happy diwali\n"  # it will return false bcz \n is not a printable char.
print(str1.isprintable())

str1 = "  "
print(str1.isspace()) # if spaces are there return true 

str1 = "World Health Organization"  # if first letter of each word in string is capital then return true otherwise false
print(str1.istitle())

str1 = "World health organization" # it will convert all first charactor of string in to capital
print(str1.title()) # usefull in blog writting 

print(str1.startswith("World")) # check the starting of string if matches return true

str1 = "Python Is a interpret3d language" # it will swap capital letters to small and small to capital
print(str1.swapcase())

