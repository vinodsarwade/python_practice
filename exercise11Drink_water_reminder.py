
'''using notification'''
import time
from plyer import notification

time_hour = float(input("Set the time interval (in hours) for your notification: "))

while True:
    time.sleep(3600 * time_hour)
    notification.notify(title="Water Reminder", message="Remember to drink water!", timeout=2)



'''using voice note'''
import time
import pyttsx3

# Initialize the text-to-speech engine
engine = pyttsx3.init()

def speak(text):
    engine.say(text)
    engine.runAndWait()

time_hour = float(input("Set the time interval (in hours) for your notification: "))

while True:
    time.sleep(3600 * time_hour)
    speak("Remember to drink water!")
