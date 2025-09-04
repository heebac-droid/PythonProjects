from json import *
from datetime import *
Task_file = open("Tasks.json").read()
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
date = f"{day} {month} {year}"
taskDate = f"{time} {date}"
enter_tasks = True
while enter_tasks == True:
    user_task = input("Please enter task")
    task_description = input("Please enter task description")
    task_status = "todo"
    numTasks += 1
    task_description = input("Please enter task description")
    tasks['name of task'] = user_task
    tasks['task description'] = task_description
    tasks['time task was created'] = taskDate
    tasks['task id'] = "task" + str(numTasks)
    tasks['status of task'] = task_status
    print(tasks)
    print(numTasks)
    task_file = open("Tasks.json","a")
    dump(tasks,task_file,indent=2)
    create_tasks = input("Do you want to enter more tasks in? (y/n)")
    if create_tasks == "n":
        task_file.close()
        enter_tasks = False
