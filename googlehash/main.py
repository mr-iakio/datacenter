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

photos = read_file(inputFile)

################ GENETIC ALGORITHM #################
