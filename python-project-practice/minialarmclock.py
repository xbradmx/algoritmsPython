from datetime import datetime
import time
import pygame



def alarmed():
  alarm = datetime(year=userinputyear, month=userinputmonth, day=userinputday, hour=userinputhours, minute=userinputminutes)
  alarm_formatted = alarm.strftime("%Y:%M:%D:%H:%M")
  print(f"{alarm_formatted} is the alarm time")
  
  now = datetime.now()
  now_formatted = now.strftime("%Y:%M:%D:%H:%M")
  print(f"{now_formatted} is the time now")
  print("")
  print("--------------------------")

  while True:
    now = datetime.now()
    now_formatted = now.strftime("%Y:%M:%D:%H:%M")

    if now_formatted == alarm_formatted:

      print(f"{now_formatted} is the time now")
      print(f"{alarm_formatted} is the alarm time")
      print("")
      print("--------------------------")

      pygame.init()
      pygame.mixer.music.load("python-project-practice/pianos.mp3")
      pygame.mixer.music.play()

      time.sleep(60)
      break



print("----Please set your alarm----")
userinputyear = int(input("please enter the year:"))
userinputmonth = int(input("please enter the month:"))
userinputday = int(input("please enter the day:"))
userinputhours = int(input("please enter the hours:"))
userinputminutes = int(input("please enter the minutes:"))
print("-----------------------------") 

alarmed()
