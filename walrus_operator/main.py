'''walrus operator is a new addition in python 3.8 and above.
it allows you yo assign a value to a variable within an expression. this can be usefull when you need to use a value multiple times in a loop.
but dont want to repeat the calculation.

the walrus operator is represented by := syntax and can be used in a variety of contexts including while loop and if statement. '''

#1
a = True
print(a := False) #here will print false using walrus .

#2
numbers = [1,2,3,4,5]
while(n := len(numbers)) > 0:
    print(numbers.pop())


'''ex: using normal way'''
# foods = list()
# while True:
#     food = input("what food do you like:")
#     if food == "quit":
#         break
#     foods.append(food)


'''above same ex. using walrus operator'''
foods = list()
while (food := input("what food do u like: ")) != "quit":
    foods.append(food)