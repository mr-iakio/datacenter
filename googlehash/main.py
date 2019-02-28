# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 19:03:29 2019

@author: angel
"""

import ODC
import time
import random
import numpy as np

############## INPUT FILE ##############
print 'The code is running!'
inputFile = 'dc.in'
# inputFile = 'basic.txt'
problem = ODC.readFile(inputFile)
dataCenterInit = problem.uSlotList[:]

################ GENETIC ALGORITHM #################
