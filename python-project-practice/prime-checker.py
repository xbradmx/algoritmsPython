

def primecheck():
  userinput = int(input("enter a number to see if its a prime: "))
  numberchecker = userinput

  while numberchecker != 1:
    numberchecker = numberchecker - 1

    isitwhole = userinput % numberchecker
    
    
    if isitwhole == 0 and numberchecker != 1:
      print("-------")
      print("")
      #print (numberchecker) #this should print what number also goes into the input besides 1 and itself
      print ("this should NOT be a prime number")
      print("")
      print("-------")
      break
    elif isitwhole == 0:
      print("-------")
      print("")
      print("this should be a prime number")
      print("")
      print("-------")
      break
    




    





primecheck()




#if user % 1 == 0 and user/user == 1 and user % 2 != 0 and



