from keithley2600 import Keithley2600, ResultTable
import time
import pyvisa
import numpy as np
import csv

# auto-detect IVI backend and fallback to pyvisa '@py' otherwise
rm = pyvisa.ResourceManager()
rmList = rm.list_resources()
print(rmList)

usbAddr=rmList[0]

k = Keithley2600(usbAddr,visa_library='')

# create ResultTable with two columns
rt = ResultTable(
    column_titles=['Voltage', 'Current'],
    units=['V', 'A'],
    params={'recorded': time.asctime(), 'sweep_type': 'iv'},
)

# create live plot which updates as data is added
rt.plot(live=True)

# measure some currents
v = 5
k.apply_voltage(k.smua, v)
i = k.smua.measure.i()
rt.append_row([v, i])

# save the data
rt.save('iv_curve.txt')