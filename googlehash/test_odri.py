from googlehash.odri import *
from googlehash.RepQ import *

ind = Individual([0, 1, 3, 0])
ind.gen_output("pruebaout.txt")

inputFile = 'a_example.txt'
problem = read_file(inputFile)
a=ind.fit(problem)


1+1