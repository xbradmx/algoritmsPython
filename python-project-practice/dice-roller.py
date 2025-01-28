import random as rm

def DiceRoll():

  while True:
    TheRoller = rm.randint(1,6)
    userinput = input("would you like to roll? y/n: ").lower()
    if userinput == 'y':

      print("--------")
      print("")
      print(f"the dice landed on: {TheRoller}")
      print("")
      print("--------")
    elif userinput =='n':
      print("--------")
      print("")
      print(f"Thank you for playing!")
      print("")
      print("--------")
      break
    else:
      print("invalid entry please try again!")
  
  



DiceRoll()
