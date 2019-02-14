# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 19:03:29 2019

@author: angel
"""

import ODC
import numpy as np
   

#inputFile = 'dc.in'
inputFile = 'basic.txt'
problem = ODC.readFile(inputFile)
alloc1 = ODC.allocatedServer(problem.serverList[0], 0, 1, 0)
alloc2 = ODC.allocatedServer(problem.serverList[1], 1, 0, 1)
alloc3 = ODC.allocatedServer(problem.serverList[2], 1, 3, 0)
alloc4 = ODC.allocatedServer(problem.serverList[3], 0, 4, 1)
alloc5 = []
basicSolution = [alloc1, alloc2, alloc3, alloc4, alloc5]
val = ODC.getRowCapacity(problem,1,1,basicSolution)
print(val)

print(ODC.get_poolRows(basicSolution, 0))
print(ODC.get_poolRows(basicSolution, 1))

print(ODC.get_poolguaranteedcapacity(problem, 0, basicSolution))
print(ODC.get_poolguaranteedcapacity(problem, 1, basicSolution))

print(ODC.get_minguaranteedcapacity(problem, basicSolution))






#ServerSize = 3
#row = 1
#col = 2
##DataCenter,state, row,col = ODC.tryCollocate(DataCenter, ServerSize)
##ODC.collocateServers(DataCenter,stackServer)
#servers = ODC.collocateServers(DataCenter,stackServer)
#pools = ODC.definePools(stackServer, Npools)
#
#print(pools)

        
