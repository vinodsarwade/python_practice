# number = int(input("enter a number: "))
# if number % 2 == 0:
#     print("number is even")
# else:
#     print("number is odd")


# #using function
# def even_odd(number):
#     if number % 2 == 0:
#         print("even")
#     else:
#         print("odd")

# even_odd(10)


number = [1, 23, 4, 5, 66, 7, 89]
def even_odd(num_list):
    for num in num_list:
        if num % 2 == 0:
            print(num, "is even")
        else:
            print(num, "is odd")

even_odd(number)
