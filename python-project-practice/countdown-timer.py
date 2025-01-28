import time

# def countdownmain():
#   while True:
#     try:
#       userinput = int(input("Enter number of seconds"))

#       wait = time.sleep

#     except ValueError:
#       print("invalid entry please try again")



def county(wait):

  while wait != 0:
    print(wait)
    wait -= 1
    time.sleep(1)
  print("-----------")
  print("")
  print("TIMEEEEES UP!!!!")
  print("")
  print("-----------")



while True:
  try:
    userinput = int(input("Enter number of seconds: "))
    county(userinput)
    break

  except ValueError:
    print("invalid entry try again")
print("-----------")
print("")
print("End of programme")
print("")
print("-----------")

