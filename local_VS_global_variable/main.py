x = 10  #global variable

def my_function():
    y = 5   #local variable
    print(y)
my_function()

print(x) #it will print value of x bcz x is globally declared
# print(y)  #it gets error bcz y is property of my_function only and it is declared in function ,we dont call or use this from outside of funtion

####  global keyword  ####

x = 10  #global variable
def my_function():
    global x      # here by using global keyword i can chnage value of x from 10 to 4 under function 
    x = 4        #not a good practice to chnage global variable from fucntion. write logic which will didnt led to chnage global variable. 
    y = 5   #local variable
    print(y)
my_function()

print(x) 