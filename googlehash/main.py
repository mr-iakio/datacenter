# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 19:03:29 2019

@author: angel
"""
from googlehash.RepQ import *
from googlehash.odri import *
import time
import random
import numpy as np

############## INPUT FILE ##############

# inputFile = 'a_example.txt' #4 photos
#inputFile = 'b_lovely_landscapes.txt' #80000 photos
# inputFile = 'c_memorable_moments.txt' #1000 photos
inputFile = 'd_pet_pictures.txt' #90000 photos
# inputFile = 'e_shiny_selfies.txt' #80000 photos

problem = read_file(inputFile)

################ GENETIC ALGORITHM #################

# ok = advanced_initial_population(4, problem)
nPopulation = 100
nIterations = 1000
oldPop = initial_population(nPopulation, problem)

for kiki in range(nIterations):
    print('Progress: ',kiki/nIterations,' [%]')
    newPop = []

    for nBr in range(int(nPopulation/2)):
        randFathers = random.randint(0,nPopulation-1)
        randFathers2 = random.randint(0, nPopulation-1)
        cNewPop = new_generation(oldPop[randFathers], oldPop[randFathers2])
        newPop.append(cNewPop[0])
        newPop.append(cNewPop[1])

    totalPop = newPop+oldPop
    cost = [Individual(pop).fit(problem) for pop in totalPop]

    bestPopulation = sorted(range(len(cost)),key=cost.__getitem__)
    bestPopulation.reverse()

    oldPop = [totalPop[ind] for ind in bestPopulation[0:nPopulation]]
    bestInv = Individual(oldPop[0])
    bestInv.gen_output("output_%d.txt" % bestInv.fit(problem))



#
# new_generation = []
# # new_generation.append(initPop[bestPopulation[0]])
# # new_generation.append(initPop[bestPopulation[1]])
# # nNewGenerated = 3
# # nMuted        = 3
# mutation = ODC.genInitialPopulation(problem, nNewGenerated)
# new_generation = new_generation+mutation
# [new_generation.append(ODC.new_generation(initPop[bestPopulation[0]],initPop[bestPopulation[1]])) for i in range(nMuted)]
# [new_generation.append(ODC.new_generation(initPop[bestPopulation[0]],initPop[bestPopulation[1]])) for i in range(population-nNewGenerated-nMuted)]
# initPop = new_generation[:]



# print(ok)

# ok = initial_population(4,problem)

# ok1 = [1,2,3,4,5]
# ok2 = [6,7,8,9,10]
#
# oknew = new_generation(ok1, ok2)

# print(oknew[0])
# print(oknew[1])

