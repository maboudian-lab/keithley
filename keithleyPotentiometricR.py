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

print("Creating CSV...")
with open(fileName, 'w', newline='') as csvFile:
    writer = csv.writer(csvFile)

print("Writing to CSV!")
with open(fileName, 'a', newline='') as csvFile:
    while dt <= tEnd:
        # use dual-smu voltage sweep to measure current at voltage v
        sweepList = [v]
        data = k.voltage_sweep_dual_smu(
            k.smua, k.smub, sweepList, sweepList, t_int=tInt, delay=delay, pulsed=False
        )
        t = time.time()
        dt = t - t0
        
        data = np.transpose(np.array(data))
        data = np.insert(data,0,t,axis=1) # append time as first column
        
        writer = csv.writer(csvFile)
        writer.writerows(data)

k.reset()