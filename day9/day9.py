from aocd import lines, submit
from graph import Node, Edge
with open("sample.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x for x in data if x != ""]
    return data

def partOne(inp):
    fin = [[int(j) for j in i] for i in inp]
    low = 0
    for indi, i in enumerate(fin):
        for indj, j in enumerate(i):
            nUp = fin[indi-1][indj] if indi-1 >= 0 else 10
            nDown = fin[indi+1][indj] if indi+1 < len(fin) else 10
            nLeft = fin[indi][indj-1] if indj-1 >= 0 else 10
            nRight = fin[indi][indj+1] if indj+1 < len(i) else 10
            if(j < nUp and j < nDown and j < nLeft and j < nRight):
                low += (1 + j)
    return low

alreadyChecked = []
def checkNeighbors(indi, indj, fin):
    nUp = fin[indi-1][indj] if indi-1 >= 0 else 9
    nDown = fin[indi+1][indj] if indi+1 < len(fin) else 9
    nLeft = fin[indi][indj-1] if indj-1 >= 0 else 9
    nRight = fin[indi][indj+1] if indj+1 < len(fin[0]) else 9
    alreadyChecked.append((indi, indj))
    total = 0
    if(nUp != 9 and (indi-1, indj) not in alreadyChecked):
        total += checkNeighbors(indi-1, indj, fin) + 1
    if(nDown != 9 and (indi+1, indj) not in alreadyChecked):
        total += checkNeighbors(indi+1, indj, fin) + 1
    if(nLeft != 9 and (indi, indj-1) not in alreadyChecked):
        total += checkNeighbors(indi, indj-1,fin) + 1
    if(nRight != 9 and (indi, indj+1) not in alreadyChecked):
        total += checkNeighbors(indi, indj+1, fin) + 1

    return total

def partTwo(inp):
    fin = [[int(j) for j in i] for i in inp]
    lowPoints = []
    for indi, i in enumerate(fin):
        for indj, j in enumerate(i):
            nUp = fin[indi-1][indj] if indi-1 >= 0 else 10
            nDown = fin[indi+1][indj] if indi+1 < len(fin) else 10
            nLeft = fin[indi][indj-1] if indj-1 >= 0 else 10
            nRight = fin[indi][indj+1] if indj+1 < len(i) else 10
            if(j < nUp and j < nDown and j < nLeft and j < nRight):
                lowPoints.append((indi, indj))

    basins = []
    for indi, indj in lowPoints:
        global alreadyChecked
        alreadyChecked = []
        basins.append(checkNeighbors(indi, indj, fin) + 1)
    returnVal = 1
    for i in sorted(basins)[-3:]:
        returnVal *= i
    return returnVal

#use sample input
partOne(preProcess(readIn))
partTwo(preProcess(lines))
#submit your input
# submit(partOne(preProcess(lines)))
# submit(partTwo(preProcess(lines)))
