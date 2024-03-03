#truncate is used to truncate the file up to some charactor.
#suppose my file has 10 char and i want to print only first 5 then i use truncate(5), it will print first 5 letter and truncate remaining char in file.

#to write
with open('main.txt','w') as f:
    f.write('Hello world')
    f.truncate(5)

#to read()
    with open('main.txt','r') as f:
        print(f.read())