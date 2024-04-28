nterms = int(input("enter number of terms here: "))

result = list(map(lambda x: 2**x,range(nterms+1)))
print(result)

for i in range(nterms+1):
    print(f"the value of 2 raised {i} is {result[i]}")



'''normal lambda fun'''
list1 =[1,5,3,6,8,4,2,87]
nterms = list(map(lambda x: x*2, list1))
print(nterms)