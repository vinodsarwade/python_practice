'''write a program to pronounce list of names using win32 API.
if you are given a list as follows.
l = ["vinod", "rahul","Harry"]
your program should pronounce: 
shoutout to vinod
shoutout to rahul'''

import win32com.client as vin
speaker = vin.Dispatch("SAPI.Spvoice")
list = ["Rahul","Nishant","Vinod"]

for i in list:
    print("shoutout to "+i)

for name in list:
    names = name.split()
    shoutout = f"Shoutout to {names[0]}"
    speaker.Speak(shoutout)