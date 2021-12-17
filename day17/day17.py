# from aocd import data, submit
# from tqdm import tqdm
with open("sample.txt") as fi:
    readIn = fi.read()

def preProcess(inp):
    return inp.split(": ")[1]

def partOne(inp):
    x, y = [x[2:].split("..") for x in inp.split(", ")]
    x = [int(x) for x in x]
    y = [int(y) for y in y]
    highestY = 0
    highestCombo = [0,0]
    for initX in range(-max([abs(x) for x in x]), max([abs(x) for x in x])):
        for initY in range(-max([abs(y) for y in y]), max([abs(y) for y in y])):
            step = 1
            current = [0,0]
            conditionOne = current[0] <= x[1] if x[1] > 0 else current[0] >= x[0]
            conditionTwo = current[1] <= y[1] if y[1] > 0 else current[1] >= y[0]
            xVel = initX
            yVel = initY
            localHighgestY = 0
            while(conditionOne and conditionTwo):
                # The probe's x position increases by its x velocity.
                current[0] += xVel
                # The probe's y position increases by its y velocity.
                current[1] += yVel
                # Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
                if(xVel != 0):
                    xVel = xVel -1 if xVel > 0 else xVel + 1
                # Due to gravity, the probe's y velocity decreases by 1.
                yVel -= 1
                if(current[1] > localHighgestY):
                    localHighgestY = current[1]
                if((x[0] <= current[0] <= x[1]) and (y[0] <= current[1] <= y[1])):
                    if(localHighgestY > highestY):
                        highestCombo = [initX, initY]
                        highestY = localHighgestY
                    break
                step += 1
                conditionOne = current[0] <= x[1] if x[1] > 0 else current[0] >= x[0]
                conditionTwo = current[1] <= y[1] if y[1] > 0 else current[1] >= y[0]
    print(highestY)
    print(highestCombo)
    return highestY

def partTwo(inp):
    x, y = [x[2:].split("..") for x in inp.split(", ")]
    x = [int(x) for x in x]
    y = [int(y) for y in y]
    highestY = 0
    highestCombo = [0,0]
    numberOfHits = 0
    for initX in range(-1000, 1000):
        for initY in range(-1000, 1000):
            step = 1
            current = [0,0]
            conditionOne = current[0] <= x[1] if x[1] > 0 else current[0] >= x[0]
            conditionTwo = current[1] <= y[1] if y[1] > 0 else current[1] >= y[0]
            xVel = initX
            yVel = initY
            localHighgestY = 0
            while(conditionOne and conditionTwo):
                # The probe's x position increases by its x velocity.
                current[0] += xVel
                # The probe's y position increases by its y velocity.
                current[1] += yVel
                # Due to drag, the probe's x velocity changes by 1 toward the value 0; that is, it decreases by 1 if it is greater than 0, increases by 1 if it is less than 0, or does not change if it is already 0.
                if(xVel != 0):
                    xVel = xVel -1 if xVel > 0 else xVel + 1
                # Due to gravity, the probe's y velocity decreases by 1.
                yVel -= 1
                if(current[1] > localHighgestY):
                    localHighgestY = current[1]
                if((x[0] <= current[0] <= x[1]) and (y[0] <= current[1] <= y[1])):
                    if(localHighgestY > highestY):
                        highestCombo = [initX, initY]
                        highestY = localHighgestY
                    numberOfHits += 1
                    break
                step += 1
                conditionOne = current[0] <= x[1] if x[1] > 0 else current[0] >= x[0]
                conditionTwo = current[1] <= y[1] if y[1] > 0 else current[1] >= y[0]
    print(highestY)
    print(highestCombo)
    print(numberOfHits)
    return highestY

#use sample input
# partOne(preProcess(readIn))
# partTwo(preProcess(readIn))

#submit your input
# submit(partOne(preProcess(data)))
# submit(partTwo(preProcess(data)))
