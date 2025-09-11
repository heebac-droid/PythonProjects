from json import *
py = """
{
  "name of task": "clean house",
  "task description": "should I",
  "time task was created": "6:22:10-9-2025",
  "task id": "task1",
  "status of task": "todo"
}

"""
task = open("example.json").read()
py = loads(task)
tasks = py['tasks']
task.close()
task = open("example.json","a")
dump(py,tasks,indent=2)
task.close()
task = open("example.json").read()
print(task)
