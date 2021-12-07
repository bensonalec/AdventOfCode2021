from aocd import data, submit
import statistics
import math
with open("sample.txt") as fi:
    readIn = fi.read()

def preProcess(inp):
    data = [int(x) for x in inp.split(",") if x != ""]
    return data

def partOne(inp):
    target = int(statistics.median(inp))
    return sum((i - target) for i in inp)

def partTwo(inp):
    su = 100000000000000000
    for z in inp:
        tSu = 0
        target = z
        for i in inp:
            ans = abs(i - 1 - target)
            tSu += ans * (ans + 1) / 2
        if(tSu < su):
            su = tSu
    return int(su)

#use sample input
# partOne(preProcess(readIn))
# partTwo(preProcess(readIn))

#submit your input
# submit(partOne(preProcess(data)))
# submit(partTwo(preProcess(data)))
