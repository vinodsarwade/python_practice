#tell() method is used to find current location of us , where am in code 
#which is used to find at which position seek() is started 
#finding out the from where seek is operating and current location 


with open('main.txt','r') as f:
    f.seek(5) 
    print(f.tell()) #it will print 5 bcz our seek started from 5th char in file.
    data = f.read(4) 
    print(data)