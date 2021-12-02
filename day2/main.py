with open("day2.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x.split(" ") for x in data if x != ""]
    
    return data

def partOne(inp):
    x = 0
    y = 0
    for line in inp:
        if(line[0] == "forward"):
            x += int(line[1])
        if(line[0] == "down"):
            y += int(line[1])
        if(line[0] == "up"):
            y -= int(line[1])
    print(x * y)

def partTwo(inp):
    x = 0
    y = 0
    aim = 0
    for line in inp:
        if(line[0] == "forward"):
            x += int(line[1])
            y += (aim * int(line[1]))
        if(line[0] == "down"):
            aim += int(line[1])
        if(line[0] == "up"):
            aim -= int(line[1])
    print(x * y)

partOne(preProcess(readIn))
partTwo(preProcess(readIn))
