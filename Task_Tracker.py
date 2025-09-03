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
if minute < 10:
    minute = f"0{minute}"
time = f"{hour}:{minute}"
date = f"{day} {month} {year}"
taskDate = f"{time} {date}"
enter_tasks = True
while enter_tasks == True:
    user_task = input("Please enter task")
    task_description = input("Please enter task description")
    Python_task = loads(Task_file)
    for task_details in Python_task:
        Task_file = open("Tasks.json","w")
        Tasks['Task name'] = user_task
        Tasks['Task Description'] = task_description
        Tasks['Date of task creation'] = taskDate

    create_tasks = input("Do you want to enter more tasks in? (y/n)")
    if create_tasks == "n":
        enter_tasks = False
Task_file = open("Tasks.json","a")
dump(Tasks,Task_file,indent=2)
