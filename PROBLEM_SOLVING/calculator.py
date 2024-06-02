print("_____mini calculator_______")

num1 = float(input("enter a number: "))
num2 = float(input("enter second number: "))

operation = "+","-","*","/"
print(operation)

choice = input("choose from above operation to perform: ")

if choice == "+":
    add = num1 + num2 
    print(add)

elif choice == "-":
    sub = num1 - num2
    print(sub)

elif choice == "*":
    mul = num1 * num2
    print(mul)

elif choice == "/":
    div = num1 / num2
    print(div)

else:
    print("invalid input")