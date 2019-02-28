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
        self.nRows = 0
        self.nSlots = 0
        self.nUnav = 0
        self.nPools = 0
        self.nServers = 0
        self.uSlotList = []
        self.serverList = []


class server:
    def __init__(self, s, c):
        self.size = s
        self.capacity = c


class allocatedServer:
    def __init__(self, svr, r, s, p):
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
        newLine = line.strip()
        newLine = newLine.split(' ')
        if lineN == 1:
            rows = int(newLine[0])
            slots = int(newLine[1])
            uslots = int(newLine[2])
            pools = int(newLine[3])
            servers = int(newLine[4])
            stackUS = []
            stackServer = []
        elif (lineN >= 2 and lineN < uslots + 2):
            stackUS.append([int(newLine[0]), int(newLine[1])])
        else:
            stackServer.append([int(newLine[0]), int(newLine[1])])

    output.nPools = pools
    output.nRows = rows
    output.nServers = servers
    output.nSlots = slots
    output.nUnav = uslots
    for i in range(0, output.nServers):
        output.serverList.append(server(stackServer[i][0], stackServer[i][1]))
    output.uSlotList = stackUS

    return output

def new_generation_mutation(pop1,pop2):
    new_rand = []
    values = random.sample(range(0, len(pop1)), len(pop1))

    for i in range(len(pop1)):
        randN = int(round(random.random()))
        randNM = int(round(random.random()))
        log1 = pop1[i] in new_rand
        log2 = pop2[i] in new_rand

        if randNM:
            nLeft = len(values)
            randIndex = random.randint(0,nLeft)
            new_rand.append(values[randIndex])
            values.remove(randIndex)
            if randN and not log1:
                new_rand.append(pop1[i])
                values.remove(pop1[i])
            elif randN and not log2:
                new_rand.append(pop2[i])
                values.remove(pop2[i])
            elif not randN and not log2:
                new_rand.append(pop2[i])
                values.remove(pop2[i])
            elif not randN and not log1:
                new_rand.append(pop1[i])
                values.remove(pop1[i])
    new_rand.extend(values)
    return new_rand

def new_generation(pop1,pop2):
    new_rand = []
    values = random.sample(range(0, len(pop1)), len(pop1))

    for i in range(len(pop1)):
        randN = int(round(random.random()))
        log1 = pop1[i] in new_rand
        log2 = pop2[i] in new_rand

        if randN and not log1:
            new_rand.append(pop1[i])
            values.remove(pop1[i])
        elif randN and not log2:
            new_rand.append(pop2[i])
            values.remove(pop2[i])
        elif not randN and not log2:
            new_rand.append(pop2[i])
            values.remove(pop2[i])
        elif not randN and not log1:
            new_rand.append(pop1[i])
            values.remove(pop1[i])
    new_rand.extend(values)
    return new_rand

def genInitialPopulation(problem,nPopulation):
    output = []
    [output.append(random.sample(range(0, problem.nServers), problem.nServers)) for i in range(nPopulation)]
    return output

def costFunction(problem,orderServers):
    dataCenter = problem.uSlotList[:]
    rndSol = collocateServers(dataCenter, problem,orderServers)
    return get_minguaranteedcapacity(problem, rndSol)

def collocateServers(dataCenter, problem,orderServers):
    # orderServers = [0,3,1,2,4]
    # rndndPool   = [0,1,0,1,0]
    rndndPool = range(0, problem.nPools)
    sol = []
    count = -1
    for nS in orderServers:
        output = tryCollocate(dataCenter, problem, problem.serverList[nS].size)
        dataCenter = output[0]
        if output[1]:
            if count < len(rndndPool) - 1:
                count += 1
            else:
                count = 0
            sol.append(
                allocatedServer(problem.serverList[nS], output[2], output[3], rndndPool[count]))
        else:
            sol.append([])
    return sol


def tryCollocate(dataCenter, problem, serverSize):
    state = 0
    for cR in list(range(problem.nRows)):
        for cS in list(range(problem.nSlots)):
            output = tryPosition(dataCenter, problem, serverSize, cR, cS)
            if output[1]:
                state = 1
                break
        if output[1]:
            break
    return output[0], state, cR, cS


def tryPosition(dataCenter, problem, serverSize, row, col):
    MaxColumn = problem.nSlots
    state = 0
    if serverSize + col > MaxColumn:
        state = 0
    elif checkNextSlots(dataCenter, serverSize, row, col):
        state = 1
        for nSe in list(range(0, serverSize)):
            dataCenter.append([row, col + nSe])

    return dataCenter, state


def checkNextSlots(dataCenter, ServerSize, row, col):
    state = 1
    for cS in list(range(0, ServerSize)):
        occ = [row, col + cS] in dataCenter
        if occ:
            state = 0
            break

    return state


# def tryCollocate(DataCenter, ServerSize):
#     MaxRow   = np.size(DataCenter,0)
#     MaxColumn   = np.size(DataCenter,1)
#     whileState   = 1
#     row0    = 0
#     col0    = 0
#
#     while whileState:
#         if (row0<MaxRow and col0 < MaxColumn):
#                DataCenter,ctry = tryPosition(DataCenter,ServerSize, row0, col0)
#
#         if ctry:
#             whileState = 0
#             state = 1
#             return DataCenter, state, row0, col0
#         elif col0<MaxColumn:
#             col0 += 1
#         elif row0<MaxRow:
#             col0 = 0
#             row0 += 1
#         else:
#             state = 0
#             return DataCenter, state, row0, col0
#
# def collocateServers(DataCenter,stackServer):
#     output = []
#     for server in stackServer:
#         DataCenter, success, row0, col0= tryCollocate(DataCenter, int(server[0]))
#         if success:
#             output.append([row0,col0])
#         else:
#            output.append('x')
#     return output
#
# def definePools(stackServer, Npools):
#     pools = []
#     nServers = len(stackServer)
#     vecServers = np.linspace(0,nServers-1,nServers)
#     random.shuffle(vecServers)
#     nSerPool = math.floor(nServers/Npools)
#     for i in range(Npools):
#         if i == Npools-1:
#             pools.append(vecServers[i*nSerPool:])
#         else:
#             pools.append(vecServers[i*nSerPool:(i+1)*nSerPool])
#
#     return pools

def getRowCapacity(problem, row, pool, solution):
    output = 0;
    count = -1;
    for allocserver in solution:
        count += 1
        if allocserver and allocserver.pool == pool and allocserver.row == row:
            output = output + allocserver.server.capacity

    return output


def get_poolRows(solution, pool):
    rows = [alloc.row for alloc in solution if alloc and alloc.pool == pool]
    return set(rows)


def get_poolguaranteedcapacity(problem, pool, solution):
    capacities = [getRowCapacity(problem, row, pool, solution) for row in list(range(0, problem.nRows))]
    return sum(capacities) - max(capacities)


def get_minguaranteedcapacity(problem, solution):
    guaranteedcapacities = [get_poolguaranteedcapacity(problem, pool, solution) for pool in
                            list(range(0, problem.nPools))]
    return min(guaranteedcapacities)
