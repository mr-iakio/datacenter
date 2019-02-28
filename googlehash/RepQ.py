import random

class Photo:
   def __init__(self, orient, tags):
       self.orient = orient
       self.tags = tags

def read_file(inputFile):
    fid = open(inputFile, 'r')
    #    num = fid.read()
    lines = fid.readlines()
    # print('The number of lines is: ',len(lines))
    output = []
    for line in lines[1:]:
        newLine = line.strip()
        newLine = newLine.split(' ')
        cPhoto = Photo(newLine[0], newLine[2:])
        output.append(cPhoto)
    return output
# def repair(solution):
#     currSol = solution[:]
#     max_val = max(currSol)
#     for k in range(max_val):
#         indices = [i for i, x in enumerate(ok) if x == k]
#         if len(indices)>2:
#             randN = random.sample(len(indices),len(indices))
#             [currSol[randN[2:]]

def advanced_initial_population(nPopulation, problem):
    output = []
    for cPop in range(nPopulation):
        cInd = random.sample(range(0, len(problem)), len(problem))
        joint = False
        for cPhoto in range(len(problem)-1):
            if joint:
                joint = False
                continue

            status = problem[cInd.index(cPhoto)].orient == 'V' and problem[cInd.index(cPhoto+1)].orient =='V'
            if status:
                cInd[cInd.index(cPhoto+1)] = cInd[cInd.index(cPhoto)]
                joint = True
        output.append(cInd)
    return output

def initial_population(nPopulation, problem):
    output = []
    [output.append(random.sample(range(0, len(problem)), len(problem))) for i in range(nPopulation)]
    return output

def new_generation(ind1,ind2):
    new_ind1 = []
    new_ind2 = []
    randN = random.randint(0,len(ind1))
    new_ind1 = ind1[0:randN]+ind2[randN:]
    new_ind2 = ind2[0:randN]+ind1[randN:]
    # values = random.sample(range(0, len(ind1)), len(ind1))
    # for i in range(len(ind1)):
        # randN = int(round(random.random()))
        # if randN :
        #     new_ind1.append(ind1[i])
        #     new_ind2.append(ind2[i])
        # else:
        #     new_ind1.append(ind2[i])
        #     new_ind2.append(ind1[i])

    return new_ind1,new_ind2

# def checkSolution(solution,problem):
