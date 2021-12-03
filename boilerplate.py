from aocd import lines, submit

with open("sample.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x for x in data if x != ""]
    return data

def partOne(inp):
    pass

def partTwo(inp):
    pass

#use sample input
partOne(preProcess(readIn))
partTwo(preProcess(readIn))

#submit your input
# submit(partOne(preProcess(lines)))
# submit(partTwo(preProcess(lines)))
