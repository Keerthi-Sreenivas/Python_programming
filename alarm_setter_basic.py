from datetime import datetime 
from playsound import playsound
import tkinter

alarm_time = input("Set alarm time in HH:MM:SS\n") #input in 24-hour clock format

alarm_hour = alarm_time[0:2] #Takes HH
alarm_minute = alarm_time[3:5] #Takes MM
alarm_seconds = alarm_time[6:8] #Takes SS

print("Setting Alarm..")

while True:
    current_time = datetime.now()
    current_hour = current_time.strftime("%H")
    current_minute = current_time.strftime("%M")
    current_seconds = current_time.strftime("%S")
    
    #debugging statements
    #print("Current hour: {}, Current min:{} ,current sec:{}".format(current_hour,current_minute,current_seconds))
    #print("The time is : {}".format(current_time))
    
    if(current_hour == alarm_hour):
        if(current_minute == alarm_minute):
            if(current_seconds == alarm_seconds):
                 print("Wake Up!")
                 playsound('rooster.wav')
                 break
