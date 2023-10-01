num = int(input("enter the value of num: "))

match num:          # it is new in python only in python 3.10 
                    # it is same as switch case in c and c++ java
    case 0:
        print("number is zero")   # if the num is 0 then case 0 will work ..otherwise go to next case like if else 

    case 1:
        print("case is 1")

    case _ if num != 90:         # _ is the default case in python. if condition is true then this one execute, 
                                 #  if condition is false then go to next default case.
        print(num,"is not 90")
    case _ if num != 80:
        print(num,"is not 80")
    case _:
        print(num)
        

    