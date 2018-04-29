from random import *
def simNumOfGames(numOfSim, probA, probB):
    winsA = 0
    winsB = 0
    for gameNum in range(numOfSim):
        print(numOfSim)
        scoreA, scoreB = simGame(probA,probB)
        if scoreA == 15:
            winsA = winsA + 1
            print('A team Wins')
        else:
            winsB = winsB + 1
            print('B team Wins')
    return winsA, winsB


def gameOver( scoreA, scoreB):
    return scoreA == 15 or scoreB == 15


def serveStart(server, probA , probB):
    scoreA = 0
    scoreB = 0
    r = random()
    print(r)
    while not gameOver(scoreA, scoreB):
        if server == "A":
            if random() < probA:
                scoreA = scoreA + 1
            else:
                server = "B"
        else:
            
            if random() < probB:
                scoreB = scoreB + 1
            else:
                server = "A"
    if scoreA == 15:
        print('A team Wins')
    else:
        
        print('B team Wins')
    return scoreA, scoreB


