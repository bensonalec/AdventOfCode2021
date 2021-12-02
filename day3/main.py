with open("day3.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x for x in data if x != ""]
    return data

def partOne(inp):
    pass

def partTwo(inp):
    pass

partOne(preProcess(readIn))
partTwo(preProcess(readIn))
