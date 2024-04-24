# table = int(input("enter a number to form a table: "))

# for i in range(1, 11):
#     result =  i * table
#     print(result)


table = int(input("enter a number to form a table: "))
i = 1
while i <= 10:
    result = table * i
    print(f"{table} * {i} = {result}")
    i = i + 1