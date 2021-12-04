from aocd import lines, submit

with open("sample.txt") as fi:
    readIn = fi.readlines()

def preProcess(inp):
    data = [line.strip() for line in inp]
    data = [x for x in data if x != ""]
    return data

def calculateSum(board):
    finalSum = 0
    for line in board:
        for char in line:
            if(char != "X"):
                finalSum += int(char)
    return finalSum


def checkWon(arr):
    if(arr == ['X','X','X','X','X']):
        return True
    return False

def checkFinished(board):
    for row in board:
        if(checkWon(row)):
            return True
    cols = [[board[j][i] for j in range(0,5)] for i in range(0,5)]
    for col in cols:
        if(checkWon(col)):
            return True

def partOne(inp):
    draws = inp[0].split(",")
    boards = [inp[1:][(x*5):(x+1)*5] for x in range(0,len(inp[1:]) // 5)]
    boards = [[y.split() for y in x] for x in boards]

    for draw in draws:
        for indY, board in enumerate(boards):
            for ind,line in enumerate(board):
                for indX, char in enumerate(line):
                    if(char == draw):
                        boards[indY][ind][indX] = "X"
            if checkFinished(board):
                return int(draw)*calculateSum(board)


def partTwo(inp):
    draws = inp[0].split(",")
    boards = [inp[1:][(x*5):(x+1)*5] for x in range(0,len(inp[1:]) // 5)]
    boards = [[y.split() for y in x] for x in boards]

    winDic = {x: True for x, _ in enumerate(boards)}
    for draw in draws:
        if(list(winDic.values()).count(True) > 1):
            for indY, board in enumerate(boards):
                if(winDic[indY]):
                    for ind,line in enumerate(board):
                        for indX, char in enumerate(line):
                            if(char == draw):
                                boards[indY][ind][indX] = "X"
                    if(checkFinished(board)):
                        winDic[indY] = False

    indY = [x for x,y in winDic.items() if y == True][0]
    board = boards[indY]
    for draw in draws:
        for ind,line in enumerate(board):
            for indX, char in enumerate(line):
                if(char == draw):
                    boards[indY][ind][indX] = "X"
        if(checkFinished(board)):
            return int(draw)*calculateSum(board)

#use sample input
# partOne(preProcess(readIn))
# partTwo(preProcess(readIn))

#submit your input
# submit(partOne(preProcess(lines)))
# submit(partTwo(preProcess(lines)))
