#seek() and tell() function is used to  work with file objects and there positions within file.

# seek() method  provides you to change from specific location in a file
with open('main.txt','r') as f:
    f.seek(5) # in this case it will start reading from 5th char in main.txt file
    data = f.read(4) # after 5th char it will read 4 char in file.
    print(data)