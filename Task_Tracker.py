from json import *
from datetime import *
Task_file = open("Tasks.json")
Task_array = []
Tasks = {}
num = 12
current_time = datetime.now()
day = current_time.day
month = current_time.month
year = current_time.year
hour = current_time.hour
minute = current_time.minute
numTasks = 0
if minute < 10:
    minute = f"0{minute}"
time = f"{hour}:{minute}"
date = f"{day},{month},{year}"
taskDate = f"{time} {date}"
enter_tasks = True
while enter_tasks == True:
    user_task = input("Please enter task")
    task_description = input("Please enter task description")
    task_status = "todo"
    numTasks += 1
    Tasks['name of task'] = user_task
    Tasks['task description'] = task_description
    Tasks['time task was created'] = taskDate
    Tasks['task id'] = "task" + str(numTasks)
    Tasks['status of task'] = task_status
    print(Task_array)
    Task_file = open("Tasks.json","a")
    dump(Tasks,Task_file,indent=2)
    create_tasks = input("Do you want to enter more tasks in? (y/n)")
    list_tasks = input("Do you want to list all current tasks (y/n)")
    if create_tasks == "n":
        Task_file.close()
        enter_tasks = False
    if list_tasks == "y":
        Task_file = open("Tasks.json")
        print(Task_file['name of task'])
