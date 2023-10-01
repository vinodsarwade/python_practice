# break statement enables a program to skip over a part of a code ...which terminate the loop 
# break means loop ko chodkar nikal jao
# using break statement once the condition is gets satisfied it will directly break the loop and come out of loop body

for i in range(12):
    if (i == 10):
        break
    print("5 X",i, "=", 5 *(i))
print("for loop over")  

# continue means iteration ko chodkr nikal jao
# continue is used to skip that perticular iteration and again the loop will continue 
#here is case if (i == 10) means condition gets satisfied so it will not iterating 10th iteration and directly goes to 11th one.

for i in range(15):
    if (i == 10):
        print("skipped 10th ineration")
        continue
    print("5 X",i, "=", 5 *(i))
print("for loop over")  

# continue example
for i in (2,3,4,5,6,7):
    if (i % 2 != 0):   # here if modulus is != 0 then it will skip that iteration  and check foe next
        continue       # if modulus is 0 then print it and continue to next iteration
    print(i)


