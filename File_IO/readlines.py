
#readline is a function which is read all the present line in a file 


# f = open('main.txt','r')
# while True:
#     line = f.readline()
#     if not line:
#         break
#     print(line)

#example 2
f = open('main2.txt','r')
i = 0
while True:
    i = i + 1
    line = f.readline()
    if not line:
        break
    m1 = line.split(",")[0]
    m2 = line.split(",")[1]
    m3 = line.split(",")[2]
    print(f"Marks of student {i} in maths is:{m1}")
    print(f"Marks of student {i} in english is:{m2}")
    print(f"Marks of student {i} in history is:{m3}")
    # print(line)
