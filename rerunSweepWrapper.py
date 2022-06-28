# -*- coding: utf-8 -*-
"""
Created on Tue Jun 28 14:49:13 2022

@author: mabou
"""

from keithleyIvSweep import multiSweep
from time import sleep

n = 3
fileName = 'sensorName'
vRangeList = ((-5,5),(-0.5,0.5))
vStepList = (0.1,0.01)

for j in range(0,3):
    multiSweep(fileName + "_run" + str(j) + "_",vRangeList,vStepList)
    sleep(10)