#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
IV sweep on channel B of Keithley 2600

Isaac Zakaria
Jihoon Chung
10 December 2021

Rev: 22 February 2022
Documentation:
    https://keithley2600.readthedocs.io/en/latest/api/keithley_driver.html#keithley_driver.Keithley2600.voltage_sweep_single_smu
Also requires pyusb module!
On Windows, install NI-VISA and use IVI backend instead of pyvisa
VISA library: C:\Windows\System32\visa64.dll
"""

from keithley2600 import Keithley2600, ResultTable
import pyvisa
import numpy as np
import csv

# auto-detect IVI backend and fallback to pyvisa '@py' otherwise
rm = pyvisa.ResourceManager()
rmList = rm.list_resources()
print(rmList)

# default for usbAddr is first entry of rmList
def keithleyIV(fileName, vRange, vStep=0.1, tInt=0.12, delay=-1, usbAddr=rmList[0], channel="b"):
    # initialize keithley object
    # visa_library defaults to pyvisa unless empty string '' is passed!
    k = Keithley2600(usbAddr,visa_library='')
    
    vMin = vRange[0]
    vMax = vRange[1]
    sweepList = np.arange(vMin,vMax+vStep,vStep)

    # voltage sweep from vmin to vmax with step size vstep
    # delay=-1 means no delay
    if channel == "b":
        data = k.voltage_sweep_single_smu(
            k.smub, sweepList, t_int=tInt, delay=delay, pulsed=False
        )
    elif channel == "a":
        data = k.voltage_sweep_single_smu(
            k.smua, sweepList, t_int=tInt, delay=delay, pulsed=False
        )
    elif channel == "both":
        data = k.voltage_sweep_dual_smu(
            k.smua, k.smub, sweepList, sweepList, t_int=tInt, delay=delay, pulsed=False
        )
    else:
        k.reset()
        return
    
    with open(fileName, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(np.transpose(np.array(data)))
    
    k.reset()
    
def multiSweep(fileName, vRangeList, vStepList, tInt=0.12, delay=-1, usbAddr=rmList[0], channel="b"):
    j = 0
    n = len(vRangeList)
    
    for j in range(0, n):
        vRange = vRangeList[j]
        vStep = vStepList[j]
        keithleyIV(fileName + "_" + str(vRange[0]) + "_" + str(vRange[1]) + ".csv",
                   vRange, vStep=vStep, tInt=tInt, delay=delay, usbAddr=usbAddr, channel=channel)