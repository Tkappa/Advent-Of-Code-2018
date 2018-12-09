import time
from collections import deque,defaultdict

"""
# Old solution made before discovering "Deque" and defaultdict
class Node:
    def __init__(self,dataval=None,prevval=None,nextval=None):
        self.dataval= dataval
        self.prevval= prevval
        self.nextval= nextval
    def insertAfter(self,dataval=None):
        nnode = Node(dataval,self,self.nextval)
        self.nextval.prevval=nnode
        self.nextval= nnode
        return nnode
    def deleteSeven(self):
        node = self
        for n in range(7):
            node= node.prevval
        retnode= node.nextval
        node.prevval.nextval= node.nextval
        node.nextval.prevval= node.prevval
        return (retnode,node.dataval)
    
        

def playGame(players,lastmarble):
    currentplayer=1
    playerscores= dict()
    head = Node(0)
    head.nextval= head
    head.prevval= head

    currentmarble=head
    for n in range(1,lastmarble+1):
        if( n>22 and n%23 == 0):
            score = n
            retval = currentmarble.deleteSeven()
            score+= retval[1]
            currentmarble = retval[0]
            if currentplayer in playerscores:
                playerscores[currentplayer]+=score
            else:
                playerscores[currentplayer]=score
        else:
            #print currentmarble.dataval
            currentmarble= currentmarble.nextval.insertAfter(n)
        
        currentplayer = ((currentplayer+1)%(players+1))
        if currentplayer==0:
            currentplayer=1
    return playerscores
"""

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
