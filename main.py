import socket
import time
from pymavlink import mavutil

mav = mavutil.mavudp("0.0.0.0:14550", input=True)
flag = True
while flag:
    status = mav.recv_msg()
    try:
        print(str(status.to_dict()))
    except:
        pass
    time.sleep(0.1)
