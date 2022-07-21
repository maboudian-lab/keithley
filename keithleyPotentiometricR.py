from keithley2600 import Keithley2600, ResultTable
import time
import pyvisa
import numpy as np
import csv

import matplotlib.pyplot as plt
import matplotlib.animation as animation

# auto-detect IVI backend and fallback to pyvisa '@py' otherwise
rm = pyvisa.ResourceManager()
rmList = rm.list_resources()
print(rmList)

usbAddr=rmList[0]

k = Keithley2600(usbAddr,visa_library='')
v = 5
tEnd = 3
channel = "both"

tInt = 0.12
delay = -1

t0 = time.time()
dt = 0

fileName = "test.csv"


with open(fileName, 'a', newline='') as csvFile:
    while dt <= tEnd:
        # voltage sweep from vmin to vmax with step size vstep
        # delay=-1 means no delay
        sweepList = [v]
        data = k.voltage_sweep_dual_smu(
            k.smua, k.smub, sweepList, sweepList, t_int=tInt, delay=delay, pulsed=False
        )
        t = time.time()
        dt = t - t0
        
        data = np.transpose(np.array(data))
        np.insert(data,1,t)
        
        writer = csv.writer(csvFile)
        writer.writerows(data)
    
    # print(dt)
    # print(data)

k.reset()

# print(dt)