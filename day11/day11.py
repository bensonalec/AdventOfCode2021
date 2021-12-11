from aocd import lines, submit

with open("sample.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x for x in data if x != ""]
    return data

def partOne(inp, steps):
    grid = [[int(y) for y in x] for x in inp]
    total = 0
    for step in range(steps):
        for indi, i in enumerate(grid):
            for indj, j in enumerate(i):
                grid[indi][indj] += 1
        curGrid = []
        for x in grid:
            curGrid.extend(x)
        alreadyFlashed = []

        while(len([x for x in curGrid if x > 9]) > 0):
            flashed = False
            for indi, i in enumerate(grid):
                for indj, j in enumerate(i):
                    if(j > 9 and (indi, indj) not in alreadyFlashed):
                        total += 1
                        alreadyFlashed.append((indi, indj))
                        grid[indi][indj] = 0

                        if indi-1 >= 0 and (indi-1, indj) not in alreadyFlashed:
                            grid[indi-1][indj] += 1
                        if indi+1 < len(grid) and (indi+1, indj) not in alreadyFlashed:
                            grid[indi+1][indj] += 1
                        if indj-1 >= 0 and (indi, indj-1) not in alreadyFlashed:
                            grid[indi][indj-1] += 1
                        if indj+1 < len(i) and (indi, indj+1) not in alreadyFlashed:
                            grid[indi][indj+1] += 1
                        
                        if indi-1 >= 0 and indj-1 >= 0 and (indi-1, indj-1) not in alreadyFlashed:
                            grid[indi-1][indj-1] += 1
                        if indi-1 >= 0 and indj+1 < len(i) and (indi-1, indj + 1) not in alreadyFlashed:
                            grid[indi-1][indj + 1] += 1
                        if indi+1 < len(grid) and indj-1 >= 0 and (indi+1, indj-1) not in alreadyFlashed:
                            grid[indi+1][indj - 1] += 1
                        if indi+1 < len(grid) and indj+1 < len(i) and (indi+1, indj+1) not in alreadyFlashed:
                            grid[indi+1][indj + 1] += 1
                        flashed = True
                        break
                if(flashed):
                    curGrid = []
                    for x in grid:
                        curGrid.extend(x)
                    break
            curGrid = []
            for x in grid:
                curGrid.extend(x)

    return total

def partTwo(inp):
    grid = [[int(y) for y in x] for x in inp]
    total = 0
    step = 0
    while(True):
        step += 1
        for indi, i in enumerate(grid):
            for indj, j in enumerate(i):
                grid[indi][indj] += 1
        curGrid = []
        for x in grid:
            curGrid.extend(x)
        alreadyFlashed = []

        while(len([x for x in curGrid if x > 9]) > 0):
            flashed = False
            for indi, i in enumerate(grid):
                for indj, j in enumerate(i):
                    if(j > 9 and (indi, indj) not in alreadyFlashed):
                        total += 1
                        alreadyFlashed.append((indi, indj))
                        grid[indi][indj] = 0

                        if indi-1 >= 0 and (indi-1, indj) not in alreadyFlashed:
                            grid[indi-1][indj] += 1
                        if indi+1 < len(grid) and (indi+1, indj) not in alreadyFlashed:
                            grid[indi+1][indj] += 1
                        if indj-1 >= 0 and (indi, indj-1) not in alreadyFlashed:
                            grid[indi][indj-1] += 1
                        if indj+1 < len(i) and (indi, indj+1) not in alreadyFlashed:
                            grid[indi][indj+1] += 1
                        
                        if indi-1 >= 0 and indj-1 >= 0 and (indi-1, indj-1) not in alreadyFlashed:
                            grid[indi-1][indj-1] += 1
                        if indi-1 >= 0 and indj+1 < len(i) and (indi-1, indj + 1) not in alreadyFlashed:
                            grid[indi-1][indj + 1] += 1
                        if indi+1 < len(grid) and indj-1 >= 0 and (indi+1, indj-1) not in alreadyFlashed:
                            grid[indi+1][indj - 1] += 1
                        if indi+1 < len(grid) and indj+1 < len(i) and (indi+1, indj+1) not in alreadyFlashed:
                            grid[indi+1][indj + 1] += 1
                        flashed = True
                        break
                if(flashed):
                    curGrid = []
                    for x in grid:
                        curGrid.extend(x)
                    break
            curGrid = []
            for x in grid:
                curGrid.extend(x)
        if(curGrid.count(0) == len(curGrid)):
            return step


#use sample input
print(partOne(preProcess(readIn), 100))
print(partTwo(preProcess(readIn)))
#submit your input
# submit(partOne(preProcess(lines), 100))
# submit(partTwo(preProcess(lines)))
