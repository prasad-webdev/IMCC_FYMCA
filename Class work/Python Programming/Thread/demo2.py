from threading import Thread
from time import sleep

def task():
    for i in range(5):
        print(i)
        sleep(1)  # Call sleep directly

def alphabet():
    for ch in ['a', 'b', 'c', 'd', 'e']:
        print(ch)
        sleep(1)  # Call sleep directly

t1 = Thread(target=task)
t2 = Thread(target=alphabet)

t1.start()
t2.start()

t1.join()
t2.join()

print("Both threads have completed execution.")