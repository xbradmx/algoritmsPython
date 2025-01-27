

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



def updating_a_task(tasks_list):
   
  try:
    task_id = int(input("enter the ID of the task:"))
    

  #finding the id of the task 
    task_to_update = None
    for task in tasks_list:
      if task['id'] == task_id:
          task_to_update = task
          break
        
  # task is not in the task list
    if not task_to_update:
      print("Task not found. Please try again.")
      return tasks_list
    

  # change the name of the task
    change_name = input("would you like to change the name? y/n:").lower()
    if change_name == 'y':
      task_to_update["task"] = input("Enter the NEW NAME of the task: ")
    elif change_name == 'n':
      pass
    else:
      print("Invalid input, please try again")


  # change the status of the task 
    change_status = input("would you like to change the completion status? y/n:").lower()

    if change_status == 'y':
      task_to_update['completed'] = not task_to_update['completed'] # toggling the status

    elif change_status == 'n':
        pass
    else:
        print("Invalid input, please try again")

    #tasks_list.append({"id": task_id, "task": task_name, "completed": Completed})


    print("-----------")
    print("")
    print(f"your task {task_to_update['task']} has been updated")
    print("")
    print("-----------")
  except ValueError:
    print("invalid entry, please try again!")
  return tasks_list



def Delete_Task(tasks_list):
  task_id = int(input("enter the ID of the task:"))
  erase_it = None
  for task in tasks_list:
     if task['id'] == task_id:
        erase_it = task 
        break
  if not erase_it:
    print("Task not found. Please try again.")
    return tasks_list
  
  confirm_delete = input(f"Are you sure that you want to delete {erase_it['task']}? y/n: ").lower()
  if confirm_delete == 'y':
    tasks_list.remove(erase_it)
    print("-----------")
    print("")
    print("Task Deleted!")
    print("")
    print("-----------")
  elif confirm_delete == 'n':
    print("-----------")
    print("")
    print(f"{erase_it['task']} was NOT deleted.")
    print("")
    print("-----------")

  return tasks_list




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
        updating_a_task(tasks_list)
      


    elif UserInput == '4':
        # Deleting a task
        Delete_Task(tasks_list)



    elif UserInput == '5':
        # Exit program
        print("-----------")
        print("")
        print("Now exiting the program, Goodbye!")
        print("")
        print("-----------")
        break
    else:
        print("Invalid input, please try again.")




MainTaskFunction()
