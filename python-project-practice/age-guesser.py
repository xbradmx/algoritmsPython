import time
from datetime import datetime, timedelta


def ageguesser(years, months, dayss):
  years = years * 365.25
  months = months * 28
  summedup = dayss + years + months
  now = datetime.now()
  print(now)
  delta = timedelta(days=summedup)
  
  print(delta)
  birthyear = now - delta
  print("===========")
  print("")
  print(f"your birthday is {birthyear}")
  print("")
  print("===========")





userinputyears = int(input("enter your age in years: "))
userinputmonths = int(input("enter your aditional months: "))
userinputdays = int(input("enter your aditional days: "))

ageguesser(userinputyears, userinputmonths, userinputdays)
