from aocd import lines, submit
import statistics

with open("sample.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x for x in data if x != ""]
    return data

def checkSyntax(line):
    charStack = []
    for char in line:
        if(char == "("):
            charStack.append(char)
        elif(char == "["):
            charStack.append(char)
        elif(char == "{"):
            charStack.append(char)
        elif(char == "<"):
            charStack.append(char)
        elif(char == ")"):
            popped = charStack.pop()
            if(popped != "("):
                return 3
        elif(char == "]"):
            popped = charStack.pop()
            if(popped != "["):
                return 57
        elif(char == "}"):
            popped = charStack.pop()
            if(popped != "{"):
                return 1197
        elif(char == ">"):
            popped = charStack.pop()
            if(popped != "<"):
                return 25137
    return 0

def partOne(inp):
    total = 0
    for line in inp:
        total += checkSyntax(line)
    return total

def repairSyntax(line):
    charStack = []
    for char in line:
        if(char == "("):
            charStack.append(char)
        elif(char == "["):
            charStack.append(char)
        elif(char == "{"):
            charStack.append(char)
        elif(char == "<"):
            charStack.append(char)
        elif(char == ")"):
            popped = charStack.pop()
        elif(char == "]"):
            popped = charStack.pop()
        elif(char == "}"):
            popped = charStack.pop()
        elif(char == ">"):
            popped = charStack.pop()
    completionStack = []
    for char in charStack[::-1]:
        if(char == "("):
            completionStack.append(")")
        elif(char == "["):
            completionStack.append("]")
        elif(char == "{"):
            completionStack.append("}")
        elif(char == "<"):
            completionStack.append(">")
    charStack = charStack.extend(completionStack)
    total = 0
    for char in completionStack:
        if(char == ")"):
            total *= 5
            total += 1
        elif(char == "]"):
            total *= 5
            total += 2
        elif(char == "}"):
            total *= 5
            total += 3
        elif(char == ">"):
            total *= 5
            total += 4

    return total

def partTwo(inp):
    finalList = []
    for line in inp:
        if(checkSyntax(line) == 0):
            finalList.append(repairSyntax(line))
    return statistics.median(finalList)

#use sample input
# partOne(preProcess(readIn))
print(partTwo(preProcess(readIn)))

#submit your input
# submit(partOne(preProcess(lines)))
submit(partTwo(preProcess(lines)))
