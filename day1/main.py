with open("day1.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [int(x) for x in data if x != ""]
    return data

def partOne(inp):
    prev = 0
    incCount = 0
    for x in inp:
        if x > prev:
            incCount += 1
        prev = x
    print(incCount-1)

def partTwo(inp):
    prev = 0
    incCount = 0
    first = 0
    last = 3
    while last <= len(inp):
        toLook = inp[first:last]
        cur = sum(toLook)
        first += 1
        last += 1
        if(cur > prev):
            incCount += 1
        prev = cur
    print(incCount - 1)

partOne(preProcess(readIn))
partTwo(preProcess(readIn))
