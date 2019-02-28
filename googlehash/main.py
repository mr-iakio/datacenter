# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 19:03:29 2019

@author: angel
"""
from RepQ import *
import time
import random
import numpy as np

############## INPUT FILE ##############

inputFile = 'a_example.txt' #4 photos
# inputFile = 'b_lovely_landscapes.txt' #80000 photos
# inputFile = 'c_memorable_moments.txt' #1000 photos
# inputFile = 'd_pet_pictures.txt' #90000 photos
# inputFile = 'e_shiny_selfies.txt' #80000 photos

problem = read_file(inputFile)

################ GENETIC ALGORITHM #################

ok = advanced_initial_population(4, problem)
print(ok)

# ok = initial_population(4,problem)

# ok1 = [1,2,3,4,5]
# ok2 = [6,7,8,9,10]
#
# oknew = new_generation(ok1, ok2)

# print(oknew[0])
# print(oknew[1])

