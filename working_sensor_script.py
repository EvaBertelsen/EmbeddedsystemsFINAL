import serial
import time
import os



ser = serial.Serial('/dev/ttyACM0',9600)
s = [0]
afk_counter = 0
stream = open("michalgui.py")
read_file= stream.read()
os.system('sudo vcgencmd display_power 0')
while True:
    dist=ser.readline()
    print(dist)
    time.sleep(1)
    if dist != dist:
        ori_dist = dist
        os.system('sudo vcgencmd display_power 1')
        exec(read_file)
        if dist == ori_dist:
            while True:
                afk_counter += 1
                print(afk_counter)
                if afk_counter == 10:
                    os.system('sudo vcgencmd display_power 0')