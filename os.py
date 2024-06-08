import os 
from pathlib import Path

items = os.listdir("C:\\Users\\VSARWADE\\Desktop\\python")
print(items)

size = os.path.getsize("C:\\Users\\VSARWADE\\Desktop\\python")
print(size)

print(os.getcwd())



file_path = "C:\\Users\\VSARWADE\\Desktop\\python\\exercise.py"

if os.path.exists(file_path):
    print("File exists")
else:
    print("File does not exist")


file_path = "C:\\Users\\VSARWADE\\Desktop\\python\\exercise.py"

if os.path.isfile(file_path):
    print("It is a file")
else:
    print("It is not a file")




file_path = "C:\\Users\\VSARWADE\\Desktop\\python\\exercise.py"

try:
    with open(file_path, 'r') as file:
        contents = file.read()
        print(contents)
except FileNotFoundError:
    print("File not found.")
