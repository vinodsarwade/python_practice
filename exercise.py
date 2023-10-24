import time

currentTIme = time.strftime("%H. %M. %S")    # print current time in hour, minute and sec. 
print("Current time is : ",currentTIme)   # strftime is a method of time library

hours = int(time.strftime("%H"))
print("Hours:", hours)
hours= int(input("enter hours"))

# currentTIme_minute = int(time.strftime("%M"))
# print("minutes:", currentTIme_minute)

# currentTIme_second = int(time.strftime("%S"))
# print("seconds:", currentTIme_second)

if hours>= 5  and hours < 12 :
    print("good morning")
elif hours >= 12 and hours <= 17:
    print("Good afternoon")
elif hours > 17 and hours <= 20:
    print("good evening")
else :
    print("good night")




