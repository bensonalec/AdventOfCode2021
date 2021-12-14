from aocd import lines, submit
from functools import lru_cache
from collections import defaultdict

with open("sample.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x for x in data if x != ""]
    return data

rules = None

@lru_cache
def convertPair(pair):
    return rules[pair]

def solve(inp, steps):
    template = inp[0]
    global rules
    rules = inp[1:]
    rules = [x.split(" -> ") for x in rules]
    rules = {x: y for x,y in rules}
    tempDic = {}
    for ind,_ in enumerate(template[:-1]):
        pair = template[ind] + template[ind+1]
        tempDic[pair] = 1 if pair not in tempDic else tempDic[pair] + 1 

    for _ in range(steps):
        temp = {}
        for x,y in tempDic.items():
            converted = convertPair(x)
            pOne = x[0] + converted
            pTwo = converted + x[1]
            temp[pOne] = y if pOne not in temp else temp[pOne] + y 
            temp[pTwo] = y if pTwo not in temp else temp[pTwo] + y 
        tempDic = temp

    counts = defaultdict(lambda: 0)
    for x,y in tempDic.items():
        counts[x[0]] += y
        counts[x[1]] += y

    counts[template[0]] += 1
    counts[template[-1]] += 1
    #account for doubles
    counts = {x: y // 2 for x,y in counts.items()}
    print(counts)
    mostCommon = (None, 0)
    leastCommon = (None, float('inf'))
    for x,y in counts.items():
        if(y > mostCommon[1]):
            mostCommon = (x, y)
        if(y < leastCommon[1]):
            leastCommon = (x, y)
    return mostCommon[1] - leastCommon[1]

# print(solve(preProcess(lines), 40))
