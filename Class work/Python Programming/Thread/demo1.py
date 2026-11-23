from threading import Thread

def task():
    print("Task is running in a separate thread.")

#create thread
t = Thread(target=task)

#start thread
t.start()

#waiting for complition of thread
t.join()

print("Thread has completed execution.")