# -*- coding: utf-8 -*-
"""
Created on Tue Jul 26 14:13:39 2022

@author: mabou
"""

import numpy as np
from monitorNoFigaroV2 import figaroMonitor
from keithleyPotentiometricR import keithleyPotentiometric
from threading import Thread



    



def func1():
    figaroMonitor('equil-humidity-run4.csv', np.inf, port = 'COM6', bme = 680)

def func2():
    keithleyPotentiometric('equil-dual-resistance-A-D-run4.csv',v=5)

if __name__ == '__main__':
    Thread(target = func1).start()
    Thread(target = func2).start()