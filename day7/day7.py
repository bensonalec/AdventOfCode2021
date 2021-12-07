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
    sum = 0
    for i in inp:
        sum += abs(i - target)
    print(sum)
    return sum

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
# print(partTwo(preProcess(readIn)))

#submit your input
# submit(partOne(preProcess(data)))
print(partTwo(preProcess(data)))
