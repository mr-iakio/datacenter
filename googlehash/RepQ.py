class problem:
    def __init__(self):
        self.nRows = 0
        self.nSlots = 0
        self.nUnav = 0
        self.nPools = 0
        self.nServers = 0
        self.uSlotList = []
        self.serverList = []


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

def dummy():
    print('The repository is loaded')