number = int(input("enter a number: "))
if number % 2 == 0:
    print("number is even")
else:
    print("number is odd")


#using function
def even_odd(number):
    if number % 2 == 0:
        print("even")
    else:
        print("odd")

even_odd(10)