age = int(input("Enter your current age : "))
print("age is :",age)

#conditional statement
#> , < , >= , <= , == , !=

if age >= 18:
    print("congrats !!")
    print("You are eligible foe voting")
else:
    print("not eligible")
    

price = 200
budget = int(input("enter your budget :"))

if budget >= price:
    print("alexa add 1 kg of apple in cart")
else:
    print("alexa do not add apple in  cart budget is low")