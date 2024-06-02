import random,itertools

dec = list(itertools.product(range(1,14),["Spade","club","Hearts","diamond"]))
# print(dec)

random.shuffle(dec)
print(dec)

for i in range(5):
    print(dec[i][0],"of",dec[i][1])