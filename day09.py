import time
from collections import deque,defaultdict

def playGame(players,lastmarble):
    playerscores= defaultdict(int)
    circle = deque([0])
    for n in range(1,lastmarble+1):
        if n%23 == 0:
            circle.rotate(7)
            playerscores[n%players]+= n + circle.pop()
            circle.rotate(-1)
        else:
            circle.rotate(-1)
            circle.append(n)
    return playerscores
    

with open('./inputs/input9.txt') as f: 
    start_time= time.time()
    line = f.readlines()[0].strip().split(" ")
    players = int(line[0])
    lastmarble = int(line[6])

    playerscores = playGame(players,lastmarble)

    print "Part one: "+str(playerscores[max(playerscores,key=playerscores.get)])

    lastmarble= lastmarble*100

    playerscoress = playGame(players,lastmarble)
    print "Part two: "+str(playerscoress[max(playerscoress,key=playerscoress.get)])
    print "Time: "+str(time.time()-start_time)
