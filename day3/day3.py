from aocd import lines, submit

with open("sample.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x for x in data if x != ""]
    return data

def partOne(inp):
    epsilon = ""
    gamma = ""
    for ind, i in enumerate(inp[0]):
        toCheck = [int(x[ind]) for x in inp]
        mostCommon = "0" if sum(toCheck) > (len(toCheck) / 2) else "1"
        leastCommon = "0" if sum(toCheck) < (len(toCheck) / 2) else "1"
        gamma += mostCommon
        epsilon += leastCommon
    return int(gamma,2 ) * int(epsilon, 2)


def partTwo(inp):
    checking = inp
    for ind, _ in enumerate(inp[0]):
        toCheck = [(x[ind], x) for x in checking]
        mostCommon = "0" if [x[0] for x in toCheck].count("0") > [x[0] for x in toCheck].count("1") else "1"
        checking = [x[1] for x in toCheck if x[0] == mostCommon]
        if(len(checking) == 1):
            break
    oxygen = checking[0]

    checking = inp
    for ind, _ in enumerate(inp[0]):
        toCheck = [(x[ind], x) for x in checking]
        mostCommon = "0" if [x[0] for x in toCheck].count("0") <= [x[0] for x in toCheck].count("1") else "1"
        checking = [x[1] for x in toCheck if x[0] == mostCommon]
        if(len(checking) == 1):
            break
    co2 = checking[0]
    return int(oxygen,2) * int(co2,2)

#use sample input
print(partOne(preProcess(readIn)))
# partTwo(preProcess(readIn))

#submit your input
# submit(partOne(preProcess(lines)))
# submit(partTwo(preProcess(lines)))
