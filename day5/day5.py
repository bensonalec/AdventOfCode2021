from aocd import lines, submit
import copy
with open("sample.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x.split(" -> ") for x in data if x != ""]
    return data

def partOne(inp):
    maxX = 0
    minX = 0
    maxY = 0
    minY = 0
    for pOne, pTwo in inp:
        pOne = pOne.split(",")
        pTwo = pTwo.split(",")
        xVals = [int(pOne[0]), int(pTwo[0])]
        yVals = [int(pOne[1]), int(pTwo[1])]
        curMaxX = max(xVals)
        curMaxY = max(yVals)
        curMinX = min(xVals)
        curMinY = min(yVals)
        if(curMaxX > maxX):
            maxX = curMaxX
        if(curMaxY > maxY):
            maxY = curMaxY
        if(curMinX < minX):
            minX = curMinX
        if(curMinY < minY):
            minY = curMinY
    row = copy.deepcopy([0]) * (maxX + 1)
    grid = [copy.deepcopy(row) for i in range(0,maxY+1)]

    for pOne, pTwo in inp:
        pOne = pOne.split(",")
        pTwo = pTwo.split(",")
        if(pOne[0] == pTwo[0]):
            x = int(pOne[0])
            vals = [int(pOne[1]), int(pTwo[1])]
            yOne = min(vals)
            yTwo = max(vals)
            for i in range(yOne, yTwo+1):
                if(grid[i][x] == 0):
                    grid[i][x] = 1
                else:
                    grid[i][x] = grid[i][x] + 1
        elif(pOne[1] == pTwo[1]):
            y = int(pOne[1])
            vals = [int(pOne[0]), int(pTwo[0])]
            xOne = min(vals)
            xTwo = max(vals)

            for i in range(xOne, xTwo+1):
                if(grid[y][i] == 0):
                    grid[y][i] = 1
                else:
                    grid[y][i] = grid[y][i] + 1
    overlapCount = 0
    for row in grid:
        for char in row:
            if(char >= 2):
                overlapCount += 1
    return overlapCount

def partTwo(inp):
    maxX = 0
    minX = 0
    maxY = 0
    minY = 0
    for pOne, pTwo in inp:
        pOne = pOne.split(",")
        pTwo = pTwo.split(",")
        xVals = [int(pOne[0]), int(pTwo[0])]
        yVals = [int(pOne[1]), int(pTwo[1])]
        curMaxX = max(xVals)
        curMaxY = max(yVals)
        curMinX = min(xVals)
        curMinY = min(yVals)
        if(curMaxX > maxX):
            maxX = curMaxX
        if(curMaxY > maxY):
            maxY = curMaxY
        if(curMinX < minX):
            minX = curMinX
        if(curMinY < minY):
            minY = curMinY
    row = copy.deepcopy([0]) * (maxX + 1)
    grid = [copy.deepcopy(row) for i in range(0,maxY+1)]
    
    for pOne, pTwo in inp:
        pOne = pOne.split(",")
        pTwo = pTwo.split(",")
        if(pOne[0] == pTwo[0]):
            x = int(pOne[0])
            vals = [int(pOne[1]), int(pTwo[1])]
            yOne = min(vals)
            yTwo = max(vals)
            for i in range(yOne, yTwo+1):
                if(grid[i][x] == 0):
                    grid[i][x] = 1
                else:
                    grid[i][x] = grid[i][x] + 1
        elif(pOne[1] == pTwo[1]):
            y = int(pOne[1])
            vals = [int(pOne[0]), int(pTwo[0])]
            xOne = min(vals)
            xTwo = max(vals)

            for i in range(xOne, xTwo+1):
                if(grid[y][i] == 0):
                    grid[y][i] = 1
                else:
                    grid[y][i] = grid[y][i] + 1
        else:
            xOne = int(pOne[0])
            xTwo = int(pTwo[0])
            yOne = int(pOne[1])
            yTwo = int(pTwo[1])
            if(xOne > xTwo):
                direction = "-"
            else:
                direction = "+"
            xRange = []
            yRange = []
            if(yOne > yTwo):
                if(direction == "-"):
                    xRange = [x for x in range(xOne, xTwo-1, -1)]
                    yRange = [y for y in range(yOne, yTwo-1, -1)]
                else:
                    xRange = [x for x in range(xOne, xTwo+1, 1)]
                    yRange = [y for y in range(yOne, yTwo-1, -1)]
            else:
                if(direction == "-"):
                    xRange = [x for x in range(xOne, xTwo-1, -1)]
                    yRange = [y for y in range(yOne, yTwo+1, 1)]
                else:
                    xRange = [x for x in range(xOne, xTwo+1, 1)]
                    yRange = [y for y in range(yOne, yTwo+1, 1)]
            for i in range(0,len(xRange)):
                grid[yRange[i]][xRange[i]] += 1
    overlapCount = 0
    for row in grid:
        for char in row:
            if(char >= 2):
                overlapCount += 1
    return overlapCount

#use sample input
# partOne(preProcess(readIn))
# partTwo(preProcess(readIn))

#submit your input
# submit(partOne(preProcess(lines)))
# submit(partTwo(preProcess(lines)))
