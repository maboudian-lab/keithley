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
"""

from keithley2600 import Keithley2600, ResultTable
import pyvisa
import numpy as np
import csv

# using pyvisa-py as VISA backend, list connected instruments
# rm = pyvisa.ResourceManager('@py')
rm = pyvisa.ResourceManager('@py')
print(rm.list_resources())

def keithleyIV(fileName, vMin, vMax, vStep=0.1, tInt=0.12, delay=-1, usbAddr='USB0::1510::9730::4062092\x00::0::INSTR'):
    # initialize keithley object
    k = Keithley2600('usbAddr')
    
    # voltage sweep from vmin to vmax with step size vstep
    # delay=-1 means no delay
    data = k.voltage_sweep_single_smu(
        k.smub, np.arange(vMin,vMax+vStep,vStep), t_int=tInt, delay=delay, pulsed=False
    )
    
    with open(fileName, 'w', newline='') as csvFile:
        writer = csv.writer(csvFile)
        writer.writerows(np.transpose(np.array(data)))
    
    k.reset()