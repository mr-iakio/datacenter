# -*- coding: utf-8 -*-
"""
Created on Thu Feb  7 19:05:04 2019

@author: angel
"""
import numpy as np
import random
import math

class problem:
    def __init__(self):
        self.nRows   = 0
        self.nSlots  = 0
        self.nUnav   = 0
        self.nPools  = 0
        self.nServers = 0
        self.uSlotList = []
        self.serverList = []

class server:
    def __init__(self, s, c):
        self.size = s
        self.capacity = c
        
class allocatedServer:
        def __init__(self,svr,r,s,p):
            self.server = svr
            self.row = r
            self.slot = s
            self.pool = p
            
class solution:
        def __init__(self):
            self.allocatedServerList = []
            
        
def readFile(inputFile):
    
    fid = open(inputFile, 'r')
    #    num = fid.read()
    lines = fid.readlines()
    lineN = 0
    output = problem()
    for line in lines:
        lineN += 1
        newLine = line.split(' ')
        if lineN == 1:
            rows    = int(newLine[0])
            slots   = int(newLine[1])
            uslots  = int(newLine[2])
            pools   = int(newLine[3])
            servers = int(newLine[4])
            stackUS = np.zeros((uslots,2))
            stackServer = np.zeros((servers,2))
        elif (lineN >= 2 and lineN<uslots+2):
            stackUS[lineN-2][:] =  newLine
        else:
            stackServer[lineN-2-uslots][:] =  newLine  
        
    output.nPools = pools
    output.nRows = rows
    output.nServers = servers
    output.nSlots = slots
    output.nUnav = uslots
    for i in range(0, output.nServers):
        output.serverList.append(server(stackServer[i][0], stackServer[i][1]))
    output.uSlotList = stackUS

    return output

def tryPosition(DataCenter,ServerSize, row, col):
    MaxColumn   = np.size(DataCenter,1)
    state = 0
    if ServerSize+col>MaxColumn:
        state = 0
    elif not all(item == 0 for item in DataCenter[row,col:col+ServerSize]):
        state = 0
    else:
        DataCenter[row,col:col+ServerSize]=1
        state = 1
    
    return DataCenter,state
            
def tryCollocate(DataCenter, ServerSize):
    MaxRow   = np.size(DataCenter,0)
    MaxColumn   = np.size(DataCenter,1)
    whileState   = 1
    row0    = 0
    col0    = 0
    
    while whileState:
        if (row0<MaxRow and col0 < MaxColumn):
               DataCenter,ctry = tryPosition(DataCenter,ServerSize, row0, col0)
               
        if ctry:
            whileState = 0
            state = 1
            return DataCenter, state, row0, col0
        elif col0<MaxColumn:
            col0 += 1
        elif row0<MaxRow:
            col0 = 0
            row0 += 1
        else:
            state = 0
            return DataCenter, state, row0, col0
        
def collocateServers(DataCenter,stackServer):
    output = []
    for server in stackServer:
        DataCenter, success, row0, col0= tryCollocate(DataCenter, int(server[0]))
        if success:
            output.append([row0,col0])
        else:
           output.append('x')
    return output

def definePools(stackServer, Npools):
    pools = []
    nServers = len(stackServer)
    vecServers = np.linspace(0,nServers-1,nServers)
    random.shuffle(vecServers)
    nSerPool = math.floor(nServers/Npools)
    for i in range(Npools):
        if i == Npools-1:
            pools.append(vecServers[i*nSerPool:])
        else:
            pools.append(vecServers[i*nSerPool:(i+1)*nSerPool])
    
    return pools

def getRowCapacity(problem,row,pool,solution):

    output = 0;
    count = -1;
    for allocserver in solution:
        count += 1
        if allocserver and allocserver.pool==pool and allocserver.row==row:
            output = output+allocserver.server.capacity

    return output

    
    
    
def get_poolRows(solution, pool):
    rows = [alloc.row for alloc in solution if alloc and alloc.pool == pool]
    return set(rows)


def get_poolguaranteedcapacity(problem, pool, solution):
    capacities = [getRowCapacity(problem, row, pool, solution) for row in list(range(0, problem.nRows))]
    return sum(capacities) - max(capacities)

def get_minguaranteedcapacity(problem, solution):
    guaranteedcapacities = [get_poolguaranteedcapacity(problem, pool, solution) for pool in list(range(0, problem.nPools))]
    return min(guaranteedcapacities)
