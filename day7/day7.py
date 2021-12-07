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
    target = math.floor(statistics.mean(inp))
    return int(sum([(abs(i - target) * (abs(i - target) + 1) / 2) for i in inp]))

#use sample input
# partOne(preProcess(readIn))
# partTwo(preProcess(readIn))

#submit your input
# submit(partOne(preProcess(data)))
partTwo(preProcess(data))