# arguments is a fuction parameter which will we pass in function within braces.
# argumets has 4 types 
#1: default arguments 2:required arguments., 3: keyword argu. 4:variable length arguments 


#required arguments
def average(a,b):  
    average = ((a+b)/2)
    print("the average is: ",average)

average(5,6)

#default arguments
def average(a=5,b=6):  
    average = ((a+b)/2)
    print("the average is: ",average)

average()

def name(firstName, middleName,lastName="Sarwade"): # 1 default argumets from here
    print("hello",firstName,middleName,lastName)

name("vinod","raghunath")  #it will take 2 required arguments from here


#keyword arguments
#order of the passing arguments does not matter then we can use keyword arguments
def average(a,b):  
    average = ((a+b)/2)
    print("the average is: ",average)

average(b=10,a=20)

#variable length arguments
def average(*numbers):  #*numbers is a fun arguments which is a type of tuple
    # print(type(numbers))
    sum = 0             #it will take argument as a tuple we can give many arguments same time
    for i in numbers:
        
        sum = sum + i
        average = sum / len(numbers)
    print(average)
average(4,5,6,7,8)


def name(**name): #**name is a fun arguments which has a type is dictionary
    # print(type(name))
    print("Hello",name["firstName"],name["middleName"],name["lastName"])

name(firstName="vinod",lastName="Sarwade",middleName="Raghunath")  # key value pair arguments



#return statement
def average(*number):  #called fun
    sum = 0
    for i in number: #iterate over a given parameter
        sum = sum + i    #sum at each iteration
        average = (sum/len(number))   # find average
        return average               # return average value to calling fun
c = average(9,10,11,12)   #calling fun
print(c)

#in return statement it will return a average value to it's calling function 
#so while printing use a variable in which you can assign a calling function and then print it ex: here is "c"