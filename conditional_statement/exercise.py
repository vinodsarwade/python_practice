import time

currentTIme = time.strftime("%H. %M. %S")    # print current time in hour, minute and sec. 
print("Current time is : ",currentTIme)   # strftime is a method of time library

currentTIme = int(time.strftime("%H"))
print("Hours:", currentTIme)

currentTIme_minute = int(time.strftime("%M"))
print("minutes:", currentTIme_minute)

currentTIme_second = int(time.strftime("%S"))
print("seconds:", currentTIme_second)

if currentTIme >= 5  and currentTIme < 12 :
    print("good morning")
elif currentTIme >= 12 and currentTIme <= 18:
    print("Good afternoon")
elif currentTIme > 18 and currentTIme <= 20:
    print("good evening")

else :
    print("good night")




