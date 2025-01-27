

def DisplayOptions():
  print ("Options:")
  print ("1. Add task")
  print ("2. View Tasks")
  print ("3. Update Task")
  print ("4. Delete task")
  print ("5. Exit program")
  
def add_task_to_list(tasks_list, task_name, completed=False):
   task_id = len(tasks_list) + 1
   tasks_list.append({"id": task_id, "task": task_name, "completed": completed})
   return tasks_list



def updating_a_task(tasks_list, task_name, Completed):
   task_id = input("enter the ID of the task:")
   change_name = input("would you like to change the name? y/n:")
   if change_name.lower == 'y':
    task_name =input("enter the NEW NAME of the task:")
   elif change_name.lower == 'n':
      pass
   change_status = input("would you like to change the completion status? y/n:")
   if change_status.lower == 'y':
    if Completed == False:
       Completed = True

    else: 
       Completed = False

   elif change_status.lower == 'n':
      pass
   else:
      print("Invalid input, please try again")
   tasks_list.update({"id": task_id, "task": task_name, "completed": Completed})




def TasksFunction():
  Tasks = [
    {"id": 1, "task": "Buy groceries", "completed": False},
    {"id": 2, "task": "Do laundry", "completed": True},
  ]
  return Tasks






def MainTaskFunction():
  tasks_list = TasksFunction()

  while True:
    # Displays the option menu
    DisplayOptions()
    UserInput = input("Your Selection: ")
    

    if UserInput == '1':
        # Adding a task to the list
        #tasks_list = TasksFunction()
        task_name = input("Enter the task name: ")
        tasks_list = add_task_to_list(tasks_list, task_name )
        print("-----------")
        print("")
        print(f"{task_name} has been added ")
        print("")
        print("-----------")


        #NewTaskInput = input(" please enter your Task: ")
        #tasks = tasks.append("id": len(tasks) + 1, "task": NewTaskInput, "completed": False )


        # prints the task that has just been added // does not work 
        #print(f"Your Task has been added as : ID: {identification}, Task: {TaskName}, {TaskStatus}")

    elif UserInput == '2':
        # Viewing tasks
        #tasks_list = TasksFunction()
        print("---------------------")
        print("")
        for task in tasks_list:
           identification = task['id']
           task_name = task['task']
           TaskStatusCheck = task['completed']

           if TaskStatusCheck == True:
              TaskStatus = "Completed"
           else:
              TaskStatus = "NOT Completed"

           print(f"Task identification is: {identification}, Your Task is: {task_name}, {TaskStatus}")
        print("")
        print("---------------------")

        

    elif UserInput == '3':
        # Updating a task
        pass  # Placeholder for future code
    elif UserInput == '4':
        # Deleting a task
        pass  # Placeholder for future code
    elif UserInput == '5':
        # Exit program
        print("Now exiting the program, Goodbye!")
        break
    else:
        print("Invalid input, please try again.")




MainTaskFunction()
