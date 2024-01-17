### update() ###
emp1 = {122:45, 123:89, 124:69, 125:71}
emp2 = {222:67,223:80}
emp1.update(emp2)
print(emp1)

### clear() ###
emp1 = {122:45, 123:89, 124:69, 125:71}
emp1.clear()
print(emp1)

### empty dict ###
empt = {}
print(empt)

### pop() ###
emp1 = {122:45, 123:89, 124:69, 125:71}
emp1.pop(122)
print(emp1)

### popitem() ###
emp1 = {122:45, 123:89, 124:69, 125:71}
emp1.popitem()
print(emp1) # it will autometically pop last item in the dict

### del ###
del emp1  # to delete whole dict
print(emp1)
