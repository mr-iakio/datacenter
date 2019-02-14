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
basicSolution = [[0,1,0],[1,0,1],[1,3,0],[0,4,1],['x']]
val = ODC.getRowCapacity(problem,1,1,basicSolution)
print(val)








#ServerSize = 3
#row = 1
#col = 2
##DataCenter,state, row,col = ODC.tryCollocate(DataCenter, ServerSize)
##ODC.collocateServers(DataCenter,stackServer)
#servers = ODC.collocateServers(DataCenter,stackServer)
#pools = ODC.definePools(stackServer, Npools)
#
#print(pools)

        
