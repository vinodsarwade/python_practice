# while loop is running untill the condition is getting satisfied.

i = 0
while i < 10:   #check condition and print untill i < 10
    print(i)
    i = i+1     # increment the i by 1


i = int(input("enter a integer number: "))   # it will act as do while loop but python don't have do while loop 
while(i<=38):
    i = int(input("enter a integer number: "))
    print(i)
print("got a greater number condition satisfied")


count = 5
while count > 0:
    print(count)
    count = count - 1

else:  # we can use else with while loop also ..if condition gets satisfied then interpretor go in else loop
    print("done with the loop")


# do while emulate

while True:     # in python do while emulate like this it will execute first at least once then it will check for condition
    number = int(input("enter a positive number: "))
    print(number)
    if not number > 2:  #if number is not > 2 then come inside if statement and break the loop
        print("loop break")
        break
        
    print("entered number is greater than 2")



