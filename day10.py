import os
import time

def negStep(points):
    for p in points:
        p[0][0]-=p[1][0]
        p[0][1]-=p[1][1] 

def step(points):
    maxx = 0
    maxy = 0
    minx = 1000000
    miny = 1000000
    sumx = 0
    for p in points:
        p[0][0]+=p[1][0]
        p[0][1]+=p[1][1]
        sumx+=p[0][0]
        if p[0][1]<miny:
            miny=p[0][1]
        if p[0][1]>maxy:
            maxy=p[0][1]
        if p[0][0]>maxx:
            maxx=p[0][0]
        if p[0][0]<minx:
            minx=p[0][0]
    area = (abs(maxx)-abs(minx))*(abs(maxy)-abs(miny))
    return (maxx,maxy,area,minx,miny)

def contains(points,point):
    for p in points:
        if p[0]==point:
            return True
    return False


with open('./inputs/input10.txt') as f:
    start_time= time.time()
    clear = lambda: os.system('clear')
    lines = f.readlines()
    points = []

    # Get the points
    for line in lines:
        posx= int(line.split("<")[1].split(",")[0])
        posy= int(line.split("<")[1].split(",")[1].split(">")[0])
        velx = int(line.split(">")[1].split("<")[1].split(",")[0])
        vely = int(line.split(">")[1].split("<")[1].split(",")[1].replace(">","").strip())
        points.append([[posx,posy],(velx,vely)])

    near = False
    seconds = 0
    minarea = 1000000 
    minx = 1000000
    miny = 1000000
    while not(near):
        retval= step(points)
        maxx= retval[0]
        maxy= retval[1]
        minx= retval[3]
        miny= retval[4]
        if (retval[2]<=minarea):
            minarea=retval[2]
            seconds +=1    
        # If the current area is greater than the minarea then the points reached the nearest they can be and are beginning to drift apart
        # So we need to restore le last second in order to get the right anwser
        else:
            negStep(points)
            near=True
    print "Part one: "
    for i in range(miny,maxy+1):
        for j in range(minx,maxx+1):
            if contains(points, [j,i]):
                print "#",
            else:
                print".",
        print "" 
    print "Part two: " + str(seconds)
    print "Time: "+ str(time.time()-start_time)
