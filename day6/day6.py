from collections import defaultdict
from aocd import data, submit

with open("sample.txt") as fi:
    readIn = fi.read()

def preProcess(inp):
    data = [int(x) for x in inp.split(",") if x != ""]
    return data

def determineGrowth(fish):
    zeroCount = tuple(6 if x == 0 else x-1 for x in fish)
    newCount = tuple(8 for x in fish if x == 0)
    return zeroCount + newCount

def partOne(inp):
    cur = tuple(x for x in inp)
    for i in range(0, 256):
        cur = determineGrowth(cur)
    return len(cur)

def determineGrowthPTwo(fish):
    newDic = defaultdict(lambda: 0)
    for x,y in fish.items():
        if(x != 0):
            newDic[x-1] += y
        else:
            newDic[6] += y
            newDic[8] += y
    return newDic

def partTwo(inp):
    cur = inp
    curDic = defaultdict(lambda : 0)
    for x in cur:
        curDic[x] += 1
    for _ in range(0, 256):
        curDic = determineGrowthPTwo(curDic)
    total = 0
    for x,y in curDic.items():
        total += y
    return total

#use sample input
# partOne(preProcess(readIn))
# partTwo(preProcess(readIn))

#submit your input
# submit(partOne(preProcess(data)))
# submit(partTwo(preProcess(data)))
