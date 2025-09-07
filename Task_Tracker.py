from json import *
from datetime import *
Task_file = open("Tasks.json").read()
py_tasks = {}
Tasks = loads(Task_file)
print(Tasks)
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
date = f"{day}-{month}-{year}"
taskDate = f"{time}:{date}"
enter_tasks = True
while enter_tasks == True:
    user_task = input("Please enter task")
    task_description = input("Please enter task description")
    task_status = "todo"
    numTasks += 1
    py_tasks['name of task'] = user_task
    py_tasks['task description'] = task_description
    py_tasks['time task was created'] = taskDate
    py_tasks['task id'] = "task" + str(numTasks)
    py_tasks['status of task'] = task_status
    Tasks["tasks"].append(py_tasks)
    print(Tasks['tasks'])
    Task_file = open("Tasks.json","a")
    dump(Tasks,Task_file,indent=2)
    Task_file.close()
    create_tasks = input("Do you want to enter more tasks in? (y/n)")
    list_tasks = input("Do you want to list all current tasks (y/n)")
    if create_tasks == "n":
        Task_file.close()
        enter_tasks = False
    if list_tasks == "y":
        Task_file = open("Tasks.json")
