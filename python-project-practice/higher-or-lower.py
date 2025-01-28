import random



def NumberGeneratorInput():
  userinput = None
  randomNumber = random.randint(1, 20)
  print("guess a number between 1 and 20 inclusive: ")
  while randomNumber != userinput:
    try:
      userinput = int(input("Your guess: "))

      if randomNumber == userinput:
        print("")
        print("well done, you are correct")
        print("")
      elif randomNumber > userinput:
        print("")
        print("higher")
        print("")
      elif randomNumber < userinput:
        print("")
        print("lower")
        print("")
    except ValueError:
      print("")
      print("invalid entry please try again!")
      print("")
  return randomNumber

NumberGeneratorInput()


