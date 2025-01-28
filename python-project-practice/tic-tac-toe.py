


#player 1
# player 2 
# def wincheck(Theboard):
#    #the check to see if win or not
#       # Check rows
  





def TTTgame(player1, player2):
  #probably use matrix 
  TheBoard = [
    ['I', 'I','I'],
    ['I', 'I','I'],
    ['I', 'I','I']
  ]
  #welcome code and print board 
  print("---------------------")
  print("")
  print("       col1 col2 col3")
  print(f"Row 1) {TheBoard[0]}")
  print(f"Row 2) {TheBoard[1]}")
  print(f"Row 3) {TheBoard[2]}")
  print("")
  print("---------------------")
  print("")
  print(f"Hello {player1} and {player2}!")
  print("")
  print(f"{player1} you are going first:")

  while True:
    try:

      turn1Row = int(input(f"{player1} choose a row: "))
      turn1Col = int(input(f"{player1} choose a column: "))

      TheBoard[turn1Row - 1][turn1Col - 1] = 'X' 
      print("---------------------")
      print("")
      print("       col1 col2 col3")
      print(f"Row 1) {TheBoard[0]}")
      print(f"Row 2) {TheBoard[1]}")
      print(f"Row 3) {TheBoard[2]}")
      print("")
      print("---------------------")
      print("")

      ########
      for row in TheBoard:
        if row[0] == row[1] == row[2] == 'X':
            print(f"{player1} has won!")
            return False
            
        elif row[0] == row[1] == row[2] == 'O':
            print(f"{player2} has won!")
            return False
        else:
          # Check columns
          for col in range(3):
              if TheBoard[0][col] == TheBoard[1][col] == TheBoard[2][col] == 'X':
                  print(f"{player1} has won!")
                  return False
              elif TheBoard[0][col] == TheBoard[1][col] == TheBoard[2][col] == 'O':
                  print(f"{player2} has won!")
                  return False
          else:
              # Check diagonals
              if TheBoard[0][0] == TheBoard[1][1] == TheBoard[2][2] == 'X' or TheBoard[0][2] == TheBoard[1][1] == TheBoard[2][0] == 'X':
                  print(f"{player1} has won!")
                  return False
                  
              elif TheBoard[0][0] == TheBoard[1][1] == TheBoard[2][2] == 'O' or TheBoard[0][2] == TheBoard[1][1] == TheBoard[2][0] == 'O':
                  print(f"{player2} has won!")
                  return False
              else:
                  
                  continue
      #######

      turn2Row = int(input(f"{player2} choose a row: "))
      turn2Col = int(input(f"{player2} choose a column: "))

      TheBoard[turn2Row - 1][turn2Col - 1] = 'O' 
      #for row in TheBoard:
        #print(row)
      print("---------------------")
      print("")
      print("       col1 col2 col3")
      print(f"Row 1) {TheBoard[0]}")
      print(f"Row 2) {TheBoard[1]}")
      print(f"Row 3) {TheBoard[2]}")
      print("")
      print("---------------------")
      print("")

      
      ########
      for row in TheBoard:
        if row[0] == row[1] == row[2] == 'X':
            print(f"{player1} has won!")
            break
        elif row[0] == row[1] == row[2] == 'O':
            print(f"{player2} has won!")
            break
        else:
          # Check columns
          for col in range(3):
              if TheBoard[0][col] == TheBoard[1][col] == TheBoard[2][col] == 'X':
                  print(f"{player1} has won!")
                  break
              elif TheBoard[0][col] == TheBoard[1][col] == TheBoard[2][col] == 'O':
                  print(f"{player2} has won!")
                  break
          else:
              # Check diagonals
              if TheBoard[0][0] == TheBoard[1][1] == TheBoard[2][2] == 'X' or TheBoard[0][2] == TheBoard[1][1] == TheBoard[2][0] == 'X':
                  print(f"{player1} has won!")
                  
              elif TheBoard[0][0] == TheBoard[1][1] == TheBoard[2][2] == 'O' or TheBoard[0][2] == TheBoard[1][1] == TheBoard[2][0] == 'O':
                  print(f"{player2} has won!")
                  
              else:
                  
                  continue
      #######

    

    except ValueError:
      print("invalid entry please try again")



p1name = input("Enter the name of player 1: ")
p2name = input("Enter the name of player 2: ")
TTTgame(p1name, p2name)
