import random


def computerplay():
  while True:

    print("1. rock")
    print("2. paper")
    print("3. scisors")
    try:
      user = int(input("your turn (1, 2 or 3): "))
      selector = random.randint(1, 3)
      if selector == 1:

        print("")
        print("Rock")
        print("")
      elif selector == 2:
        print("")
        print("paper")
        print("")
      elif selector == 3:
        print("")
        print("scisors")
        print("")

      if selector == user:

        print("----------")
        print("")
        print("draw")
        print("")
        print("----------")
      elif selector == 1 and user == 2:
        print("----------")
        print("")
        print("You win")
        print("")
        print("----------")
      elif user == 1 and selector == 2:
        print("----------")
        print("")
        print("computer wins")
        print("")
        print("----------")
      elif selector == 2 and user == 3:
        print("----------")
        print("")
        print("You Win")
        print("")
        print("----------")
      elif user == 2 and selector == 3:
        print("----------")
        print("")
        print("computer wins")
        print("")
        print("----------")
      elif selector == 1 and user == 3:
        print("----------")
        print("")
        print("computer wins")
        print("")
        print("----------")
      elif user == 1 and selector == 3:
        print("----------")
        print("")
        print("you win")
        print("")
        print("----------")
    except ValueError:
      print("==========================")
      print("==========================")
      print("")
      print(" invalid entry, try again")
      print("")
      print("==========================")
      print("==========================")



computerplay()
