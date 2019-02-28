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
