import socket
import time
import timeit
import matplotlib.pyplot as plt
from threading import Thread
from pymavlink import mavutil


startTime = timeit.default_timer()
x_vals = []
y_vals = []
fig, ax = plt.subplots()
plt.style.use('fivethirtyeight')
flag = True

def workerThread(threadname):
    global startTime, x_vals, y_vals, flag
    mav = mavutil.mavudp("0.0.0.0:14550", input=True)
    while flag:
        status = mav.recv_msg()
        if (status != None and status.get_type() == "GLOBAL_POSITION_INT"):
            y_vals.append(status.alt)
            x_vals.append(timeit.default_timer()-startTime)

plt.tight_layout()

print("How long do you want data to be collected? (s): ")
cTime = input()

thread1 = Thread(target=workerThread, args=("Thread-1", ))
thread1.start()

time.sleep(int(cTime))
flag = False

plt.plot(x_vals, y_vals)
plt.show()

thread1.join()
