from aocd import data, submit

with open("sample.txt") as fi:
    readIn = fi.read()

def preProcess(inp):

    return inp

def partOne(inp):
    #x increases to the right
    sectionOne, sectionTwo = inp.split("\n\n")
    coordList = [x.split(",") for x in sectionOne.split("\n")]
    xList = [int(x[0]) for x in coordList]
    yList = [int(x[1]) for x in coordList]
    boundOne = max(xList)
    boundTwo = max(yList)
    grid = []
    for i in range(boundTwo+1):
        newRow = []
        for j in range(boundOne+1):
            newRow.append(".")
        grid.append(newRow)

    for var in sectionOne.split("\n"):
        x, y = var.split(",")
        grid[int(y)][int(x)] = "#"


    for line in sectionTwo.split("\n")[:1]:
        instr = line.split(" ")[-1]
        axis, num = instr.split("=")
        if(axis == "y"):
            #fold up on line num
            toFold = grid[int(num)+1:]
            grid = grid[:int(num)]
            for indi, i in enumerate(toFold[::-1]):
                for indj, j in enumerate(i):
                    if(grid[indi][indj] == "." and j != "."):
                        grid[indi][indj] = j

        if(axis == "x"):
            #fold left on line num
            toFold = [x[int(num)+1:] for x in grid]
            toFold = [x[::-1] for x in toFold]
            for i in range(abs(int(num) - len(toFold[0]))):
                for indj, j in enumerate(toFold):
                    toFold[indj].insert(0,".")
            grid = [x[:int(num)] for x in grid]
            for indi, i in enumerate(toFold):
                for indj, j in enumerate(i):
                    if(grid[indi][indj] == "."):
                        grid[indi][indj] = j

    totalCount = 0
    for i in grid:
        for j in i:
            if(j == "#"):
                totalCount += 1
    return totalCount

def partTwo(inp):
    #x increases to the right
    sectionOne, sectionTwo = inp.split("\n\n")
    coordList = [x.split(",") for x in sectionOne.split("\n")]
    xList = [int(x[0]) for x in coordList]
    yList = [int(x[1]) for x in coordList]
    boundOne = max(xList)
    boundTwo = max(yList)
    grid = []
    for i in range(boundTwo+1):
        newRow = []
        for j in range(boundOne+1):
            newRow.append(".")
        grid.append(newRow)

    for var in sectionOne.split("\n"):
        x, y = var.split(",")
        grid[int(y)][int(x)] = "#"


    for line in sectionTwo.split("\n"):
        instr = line.split(" ")[-1]
        axis, num = instr.split("=")
        if(axis == "y"):
            #fold up on line num
            toFold = grid[int(num)+1:]
            grid = grid[:int(num)]
            for indi, i in enumerate(toFold[::-1]):
                for indj, j in enumerate(i):
                    if(grid[indi][indj] == "." and j != "."):
                        grid[indi][indj] = j

        if(axis == "x"):
            #fold left on line num
            toFold = [x[int(num)+1:] for x in grid]
            toFold = [x[::-1] for x in toFold]
            for i in range(abs(int(num) - len(toFold[0]))):
                for indj, j in enumerate(toFold):
                    toFold[indj].insert(0,".")
            grid = [x[:int(num)] for x in grid]
            for indi, i in enumerate(toFold):
                for indj, j in enumerate(i):
                    if(grid[indi][indj] == "."):
                        grid[indi][indj] = j


    string = ""
    for i in grid:
        for j in i:
            string += (j)
        string += ("\n")
    print(string)
    totalCount = 0
    for i in grid:
        for j in i:
            if(j == "#"):
                totalCount += 1
    return totalCount

#use sample input
print(partOne(preProcess(data)))
partTwo(preProcess(data))

#submit your input
# submit(partOne(preProcess(data)))
# submit(partTwo(preProcess(lines)))
