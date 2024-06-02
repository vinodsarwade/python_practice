# solution 1

l = [12,434,56,334,776,39]
num = list(filter(lambda X: X % 13 == 0,l))
print(num)