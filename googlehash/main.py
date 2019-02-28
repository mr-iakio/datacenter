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
population = 10
popTop = 7
popLow = 3
nIterations = 500
initPop = ODC.genInitialPopulation(problem,population)



for nIt in range(nIterations):

    cost = []
    t0 = time.time()
    [cost.append(ODC.costFunction(problem,initPop[i])) for i in range(population)]
    # print cost

    bestPopulation = sorted(range(len(cost)),key=cost.__getitem__)
    bestPopulation.reverse()

    new_generation = []
    # new_generation.append(initPop[bestPopulation[0]])
    # new_generation.append(initPop[bestPopulation[1]])
    nNewGenerated = 3
    nMuted        = 3
    mutation = ODC.genInitialPopulation(problem, nNewGenerated)
    new_generation = new_generation+mutation
    [new_generation.append(ODC.new_generation(initPop[bestPopulation[0]],initPop[bestPopulation[1]])) for i in range(nMuted)]
    [new_generation.append(ODC.new_generation(initPop[bestPopulation[0]],initPop[bestPopulation[1]])) for i in range(population-nNewGenerated-nMuted)]
    initPop = new_generation[:]

    print 'Iteration Number', nIt, '/', nIterations, ' ', round((float(nIt) / float(nIterations)) * 100, 3), '%','  Elapsed time: ', round(time.time() - t0,3), '[s]','  The Minimum guaranteed capacity is: ', max(cost)
    print
# print initPop
# print new_generation









# rndSol = ODC.collocateServers(dataCenter, problem)
# # print(ok)
#
#
# print(ODC.get_minguaranteedcapacity(problem, rndSol))
# do stuff



#
# # TEST MINGUARANTEED CAPACITY
#
# alloc1 = ODC.allocatedServer(problem.serverList[0], 0, 1, 0)
# alloc2 = ODC.allocatedServer(problem.serverList[1], 1, 0, 1)
# alloc3 = ODC.allocatedServer(problem.serverList[2], 1, 3, 0)
# alloc4 = ODC.allocatedServer(problem.serverList[3], 0, 4, 1)
# alloc5 = []
# basicSolution = [alloc1, alloc2, alloc3, alloc4, alloc5]
# # basicSolution = [alloc5, alloc3, alloc2, alloc4, alloc1]
# val = ODC.getRowCapacity(problem,1,1,basicSolution)
# print(val)
#
# print(ODC.get_poolRows(basicSolution, 0))
# print(ODC.get_poolRows(basicSolution, 1))
#
# print(ODC.get_poolguaranteedcapacity(problem, 0, basicSolution))
# print(ODC.get_poolguaranteedcapacity(problem, 1, basicSolution))
#
# ok = ODC.tryPosition(dataCenter,problem, 3, 0,0)
# ok = ODC.tryCollocate(dataCenter,problem,3)