
from typing import final
from aocd import data, submit
import numpy
with open("sample.txt") as fi:
    readIn = fi.read()

map = {
    "0":"0000",
    "1":"0001",
    "2":"0010",
    "3":"0011",
    "4":"0100",
    "5":"0101",
    "6":"0110",
    "7":"0111",
    "8":"1000",
    "9":"1001",
    "A":"1010",
    "B":"1011",
    "C":"1100",
    "D":"1101",
    "E":"1110",
    "F":"1111"
}

versionCount = 0
def preProcess(inp):
    data = [map[x] for x in inp]
    return "".join(data)


def parsePacket(inp):
    if(list(inp).count("0") == len(inp)):
        return 0, 0

    global versionCount
    version = int(inp[0:3],2)
    versionCount += version

    packetType = int(inp[3:6],2)

    if packetType == 4:
        currentIndex = 6
        finalValue = ""
        while(currentIndex < len(inp)):
            group = inp[currentIndex:currentIndex+5]
            lead = group[0]
            block = group[1:]
            finalValue += block
            currentIndex = currentIndex + 5
            if(lead == "0"):
                break
        finalValue = int(finalValue, 2)
        return finalValue, currentIndex
    else:
        lengthTypeId = inp[6]
        if(lengthTypeId == "0"):
            length = int(inp[7: 22], 2)
            currentIndex = 22
        else:
            numberOfPackets = int(inp[7: 18], 2)
            currentIndex = 18

        values = []
        
        while(currentIndex < len(inp)):
            group = inp[currentIndex:]
            parsed, tempIndex = parsePacket(group)
            currentIndex = currentIndex + tempIndex
            if(list(group).count("0") == len(group)):
                break
            values.append(parsed)
            if(lengthTypeId == "1" and len(values) == numberOfPackets):
                break
            if(lengthTypeId == "0" and currentIndex - 22 == length):
                break

        if(packetType == 0):
            return sum(values), currentIndex
        elif(packetType == 1):
            return numpy.prod(values), currentIndex
        elif(packetType == 2):
            return min(values), currentIndex
        elif(packetType == 3):
            return max(values), currentIndex
        elif(packetType == 5):
            return int(values[0] > values[1]), currentIndex
        elif(packetType == 6):
            return int(values[0] < values[1]), currentIndex
        elif(packetType == 7):
            return int(values[0] == values[1]), currentIndex

def partOne(inp):
    answer = parsePacket(inp)
    return versionCount

def partTwo(inp):
    answer = parsePacket(inp)
    return answer[0]

#use sample input
# partOne(preProcess(readIn))
# partTwo(preProcess(readIn))

#submit your input
# submit(partOne(preProcess(data)))
# submit(partTwo(preProcess(data)))