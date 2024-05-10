a = input("enetr the number: ")
print(f"Multiplication  table of {a} is :")
  
#here we use try and except keyword to handle exception. if user gives int input then program exicute succesfully.
#but user gives other than int like string boolean then program gives error. so that error handling is done by using try and except.
#if try block gives error then it will print exception error and again  below remaining program will exicute.
try:    
    for i in range(1, 11):
        print(f"{int(a)} X {i} = {int(a)*i}")
except Exception as e: #or we can write only except: 
    print(e)

print("below are some imp lines of code")

## Ex 2:

try:
    num = int(input("enter an integer input :"))
    a = [5,6,3]    # here we have only 3 index list which is 0,1,2
    print(a[num]) #it will print the element of index [num] which is given by user 
                   #if index element is present then it will give element present in index. if index is not present in list then throw error.
except ValueError:
    print("entered nuber is not an integer")

except:
    print("index error")

        