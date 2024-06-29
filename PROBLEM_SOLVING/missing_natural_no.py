numbers =[3,0,1,2,5,6]

length = len(numbers)
print(f"length of given list is",length)

addition = int(length*(length + 1)/2)
print(f"sum of natural numbers up to length of list:",addition)

total = 0
for i in numbers:
    total += i

print(f"sum of numbers given in list: ",total)

missing_number =  addition-total
print(f"sum of all numbers up to length - sum of elements present in list: ",missing_number)
