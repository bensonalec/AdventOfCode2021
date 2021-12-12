from aocd import lines, submit
from collections import defaultdict
from copy import deepcopy
with open("sample.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x.split("-") for x in data if x != ""]
    return data

totalPaths = 0
def traverseGraph(node, graph, beenTo, goal, maxVisits):
    global totalPaths
    for i in graph[node]:
        if i == goal:
            totalPaths += 1
        elif(i.islower() and beenTo[i] < maxVisits):
            tempBeenTo = deepcopy(beenTo)
            tempBeenTo[i] += 1
            traverseGraph(i, graph, tempBeenTo, goal, maxVisits)
        elif(i.isupper()):
            tempBeenTo = deepcopy(beenTo)
            tempBeenTo[i] += 1
            traverseGraph(i, graph, tempBeenTo, goal, maxVisits)

def partOne(inp):
    global totalPaths
    totalPaths = 0
    nodes = defaultdict(lambda: set())
    for line in inp:
        parent, child = line
        nodes[parent].add(child)
        nodes[child].add(parent)
    beenTo = defaultdict(lambda: 0)
    beenTo["start"] = 2
    traverseGraph("start", nodes, beenTo, "end", 1)
    return totalPaths

def traverseGraphTwo(node, graph, beenTo, goal):
    global totalPaths
    for i in graph[node]:
        if i == goal:
            totalPaths += 1
        elif(i.islower() and i != "start"):
            if(beenTo[i] == 0):
                tempBeenTo = deepcopy(beenTo)
                tempBeenTo[i] += 1
                traverseGraphTwo(i, graph, tempBeenTo, goal)
            elif(beenTo[i] == 1 and 2 not in beenTo.values()):
                tempBeenTo = deepcopy(beenTo)
                tempBeenTo[i] += 1
                traverseGraphTwo(i, graph, tempBeenTo, goal)
        if(i.isupper()):
            tempBeenTo = deepcopy(beenTo)
            traverseGraphTwo(i, graph, tempBeenTo, goal)

def partTwo(inp):
    global totalPaths
    totalPaths = 0
    nodes = defaultdict(lambda: set())
    for line in inp:
        parent, child = line
        nodes[parent].add(child)
        nodes[child].add(parent)
    beenTo = defaultdict(lambda: 0)
    traverseGraphTwo("start", nodes, beenTo, "end")
    return totalPaths

#use sample input
# print(partOne(preProcess(readIn)))
# print(partTwo(preProcess(readIn)))

#submit your input
# submit(partOne(preProcess(lines)))
# submit(partTwo(preProcess(lines)))
