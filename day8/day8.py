from typing import final
from aocd import lines, submit
# from graph import Node, Edge, aStar
with open("sample.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x.split(" | ") for x in data if x != ""]
    return data

def partOne(inp):
    inp = [x[1] for x in inp]
    su = 0
    for i in inp:
        for x in i.split():
            if(len(x) in [2,4,3,7]):
                su += 1
    return su


def partTwo(inp):
    correctDict = {"abcefg": 0, "cf": 1, "acdeg": 2, "acdfg": 3, "bcdf": 4, "abdfg": 5, "abdefg": 6, "acf": 7, "abcdefg": 8, "abcdfg": 9}
    alph = ['a','b','c','d','e','f','g']
    finalSum = 0
    for r in inp:
        firstHalf, secondHalf = r
        firstHalf = firstHalf.split()
        secondHalf = secondHalf.split()
        
        #Set up the data structure to hold the possibilities, the first item in the value is a boolean representing whether this value has been 'locked' and can no longer be modified 
        finalDict = {'a': [False, []], 'b': [False, []], 'c': [False, []], 'd': [False, []], 'e': [False, []], 'f': [False, []], 'g': [False, []]}
        
        oneInd = [x for x in firstHalf if len(x) == 2][0]
        fourInd = [x for x in firstHalf if len(x) == 4][0]
        sevenInd = [x for x in firstHalf if len(x) == 3][0]
        eightInd = [x for x in firstHalf if len(x) == 7][0]
        alreadyCounted = []
        #go through the display that has two characters (must be 1) and set the possibilities and mark it as locked
        for i in ["c", "f"]:
            for o in oneInd:
                if o not in finalDict[i] and not finalDict[i][0]:
                    finalDict[i][1].append(o)
            finalDict[i][0] = True
            alreadyCounted.extend(finalDict[i][1])


        #go through the display that has four characters (must be 7) and set the possibilities and mark it as locked
        for i in ["a", "c", "f"]:
            for o in sevenInd:
                if o not in finalDict[i] and not finalDict[i][0] and not o in alreadyCounted:
                    finalDict[i][1].append(o)
            finalDict[i][0] = True
            alreadyCounted.extend(finalDict[i][1])

        #go through the display that has four characters (must be 4) and set the possibilities and mark it as locked

        for i in ["b", "c", "d", "f"]:
            for o in fourInd:
                if o not in finalDict[i] and not finalDict[i][0] and not o in alreadyCounted:
                    finalDict[i][1].append(o)
            finalDict[i][0] = True

        #go through the display that has four characters (must be 8) and set the possibilities and mark it as locked
        alreadyCounted = []
        for x in finalDict.values():
            alreadyCounted.extend(x[1])
        alreadyCounted = list(set(alreadyCounted))
        for i in ["a", "b", "c", "d", "e", "f", "g"]:
            for o in eightInd:
                if o not in finalDict[i] and not finalDict[i][0] and not o in alreadyCounted:
                    finalDict[i][1].append(o)
            finalDict[i][0] = True

        #now we know a for sure, and have two options for every other one (and each letter has a 'match' with the same values)
        #build all possible translations from this (up to 8)
        possibleTranslations = []
        #go through possible translations for b
        bPos = finalDict['b'][1]
        for iind, b in enumerate(bPos):
            #in this instance, d is whatever b is not
            d = finalDict['d'][1][abs(iind -1)]
            #go through possible translations for c
            cPos = finalDict['c'][1]
            for jind, c in enumerate(cPos):
                #in this instance, f is whatever c is not
                f = finalDict['f'][1][abs(jind -1)]
                #go through possible translations for e
                ePos = finalDict['e'][1]
                for kind, e in enumerate(ePos):
                    #in this instance, g is whatever e is not
                    g = finalDict['g'][1][abs(kind -1)]
                    #append this to a list of possible translations
                    possibleTranslations.append(f"{finalDict['a'][1][0]}{b}{c}{d}{e}{f}{g}")

        #now, check these full translations against our input set, make sure that each digit in our input set is represented (the ten displays to the left of the pipe)
        for trans in possibleTranslations:
            correct = 0
            trans = {val: alph[ind] for ind, val in enumerate(trans)}
            for display in firstHalf:
                translated = "".join(sorted([trans[x] for x in display]))
                if(translated in correctDict.keys()):
                    correct += 1
            if(correct == 10):
                translation = trans
                break

        output = ""
        for i in r[1].split():
            translated = "".join(sorted([trans[x] for x in i]))
            output += str(correctDict[translated])

        finalSum += int(output)

    return finalSum

#use sample input
# partOne(preProcess(readIn))
# partTwo(preProcess(readIn))

#submit your input
# submit(partOne(preProcess(lines)))
# submit(partTwo(preProcess(lines)))
