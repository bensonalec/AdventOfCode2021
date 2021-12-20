from aocd import lines, submit

with open("sample.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x for x in data if x != ""]
    return data

def partOne(inp):
    enchancementAlgo = inp[0]
    grid = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]
    
    rest = inp[1:]
    rest = [list(x) for x in rest]
    steps = 2
    for i in range(steps):
        #need to expand rest by 2 on each side
        charToAdd = "."
        if(i % 2 != 0):
            charToAdd = "#"
        rest = [x + [charToAdd] for x in rest]
        rest = [x + [charToAdd] for x in rest]
        rest = [[charToAdd] + x for x in rest]
        rest = [[charToAdd] + x for x in rest]

        rest.insert(0, [charToAdd for x in rest[0]])
        rest.insert(0, [charToAdd for x in rest[0]])
        rest.append([charToAdd for x in rest[0]])
        rest.append([charToAdd for x in rest[0]])

        boundI = (0, len(rest))
        boundJ = (0, len(rest[0]))
        
        newImage = []
        for indi, i in enumerate(rest):
            newRow = []
            for indj, j in enumerate(i):
                num = []
                for gr in grid:
                    #check (indi, indj) + (gr[0], gr[1]) to determine pixel
                    toCheckI = indi + gr[0]
                    toCheckJ = indj + gr[1]
                    #within the 9 by 9 grid
                    if((boundI[0] <= toCheckI < boundI[1]) and (boundJ[0] <= toCheckJ < boundJ[1])):
                        num.append(rest[toCheckI][toCheckJ])
                    else:
                        num.append(charToAdd)
                newRow.append(enchancementAlgo[int("".join(num).replace(".", "0").replace("#","1"),2)])
            newImage.append(newRow)
        rest = newImage
    count = 0
    for i in rest:
        for j in i:
            if(j == "#"):
                count += 1
    return count
def partTwo(inp):
    enchancementAlgo = inp[0]
    grid = [
        (-1, -1),
        (-1, 0),
        (-1, 1),
        (0, -1),
        (0, 0),
        (0, 1),
        (1, -1),
        (1, 0),
        (1, 1)
    ]
    
    rest = inp[1:]
    rest = [list(x) for x in rest]
    steps = 50
    for i in range(steps):
        #need to expand rest by 2 on each side
        charToAdd = "."
        if(i % 2 != 0):
            charToAdd = "#"
        rest = [x + [charToAdd] for x in rest]
        rest = [x + [charToAdd] for x in rest]
        rest = [[charToAdd] + x for x in rest]
        rest = [[charToAdd] + x for x in rest]

        rest.insert(0, [charToAdd for x in rest[0]])
        rest.insert(0, [charToAdd for x in rest[0]])
        rest.append([charToAdd for x in rest[0]])
        rest.append([charToAdd for x in rest[0]])

        boundI = (0, len(rest))
        boundJ = (0, len(rest[0]))
        
        newImage = []
        for indi, i in enumerate(rest):
            newRow = []
            for indj, j in enumerate(i):
                num = []
                for gr in grid:
                    #check (indi, indj) + (gr[0], gr[1]) to determine pixel
                    toCheckI = indi + gr[0]
                    toCheckJ = indj + gr[1]
                    #within the 9 by 9 grid
                    if((boundI[0] <= toCheckI < boundI[1]) and (boundJ[0] <= toCheckJ < boundJ[1])):
                        num.append(rest[toCheckI][toCheckJ])
                    else:
                        num.append(charToAdd)
                newRow.append(enchancementAlgo[int("".join(num).replace(".", "0").replace("#","1"),2)])
            newImage.append(newRow)
        rest = newImage
    count = 0
    for i in rest:
        for j in i:
            if(j == "#"):
                count += 1
    return count
#use sample input
# print(partOne(preProcess(readIn)))
print(partTwo(preProcess(readIn)))

#submit your input
# submit(partOne(preProcess(lines)))
# submit(partTwo(preProcess(lines)))
