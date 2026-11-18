import time 

def task(name):
    print(f"{name} started")
    time.sleep(2)
    print(f"{name} completed")

task("Task 1")
task("Task 2")
task("Task 3")