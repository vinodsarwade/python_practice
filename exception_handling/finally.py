#finally keyword is always exicuted weather the try block exicuted or except block exicuted.
#code succefull run or it is throwing error finally block always exicuted.

# try:
#     lst = [3,5,7,9]
#     num = int(input("enter an integer number: "))
#     print(lst[num])
# except:
#     print("some error occured")

# finally:
#     print("am always exicuted. ")

#using function
def fun1():
    try:
        lst = [5,6,7,8]
        num = int (input("enter an integer input : "))
        print(lst[num])
    except:
        print("some error occured !!")
    
    finally:
        print("am always exicuted:!")
fun1()
