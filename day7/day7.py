from aocd import data, submit
import statistics

with open("sample.txt") as fi:
    readIn = fi.read()

def preProcess(inp):
    data = [int(x) for x in inp.split(",") if x != ""]
    return data

def partOne(inp):
    target = int(statistics.median(inp))
    return sum((i - target) for i in inp)

def partTwo(inp):
    su = float('inf')
    for z in inp:
        tSu = sum([(abs(i - 1 - z) * (abs(i - 1 - z) + 1) / 2) for i in inp])
        if(tSu < su):
            su = tSu
    return int(su)

#use sample input
# partOne(preProcess(readIn))
# partTwo(preProcess(readIn))

#submit your input
# submit(partOne(preProcess(data)))
# submit(partTwo(preProcess(data)))
