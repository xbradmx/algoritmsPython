

def DisplayOptions():
  print ("Options:")
  print ("1. Add task")
  print ("2. View Tasks")
  print ("3. Update Task")
  print ("4. Delete task")
  print ("5. Exit program")
  

def TasksFunction():
  Tasks = [
    {"id": 1, "task": "Buy groceries", "completed": False},
    {"id": 2, "task": "Do laundry", "completed": True},
  ]



def MainTaskFunction():


  while True:
    # Displays the option menu
    DisplayOptions()
    UserInput = input("Your Selection: ")

    if UserInput == '1':
        # Adding a task to the list
        pass  # Placeholder for future code
    elif UserInput == '2':
        # Viewing tasks
        pass  # Placeholder for future code
    elif UserInput == '3':
        # Updating a task
        pass  # Placeholder for future code
    elif UserInput == '4':
        # Deleting a task
        pass  # Placeholder for future code
    elif UserInput == '5':
        # Exit program
        break
    else:
        print("Invalid input, please try again.")


