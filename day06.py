import time

# Find the nearest "home" point in the list, and the total sum of all distances
def findNearest(currentpoint,pointlist):
    nearestD = 500000
    nearestIndex = -1
    howmany = 0
    totalsum= 0
    for n in range(0,len(pointlist)):
        point = pointlist[n][0]
        dist = abs(currentpoint[0]-point[0])+abs(currentpoint[1]-point[1])
        totalsum += dist
        if dist == nearestD:
            howmany+=1
        if dist < nearestD:
            howmany = 1
            nearestD = dist
            nearestIndex=n
    if howmany>1:
        return (-1,totalsum)
    else:
        return (nearestIndex,totalsum)

# Checks if any point in the list touches a edge, because if it does the area is infinite
def isCursed(pointslist,cursedMin,cursedMax):
    smallestx = min(pointslist[0])
    smallesty = min(pointslist[1])
    biggestx = max(pointslist[0])
    biggesty= max(pointslist[1])

    if (biggestx ==cursedMax or biggesty == cursedMax):
        return True
    if (smallestx == cursedMin or smallesty == cursedMin):
        return True
    return False


with open('./inputs/input6.txt') as f:
    start_time = time.time()
    lines = f.readlines()
    points=[]
    for line in lines:
        #Creates an array of arrays build like this: [(pos X,pos Y),[Array of points that are "mine"]]
        point = [(int(line.split(",")[0]),int(line.split(",")[1])),[]]
        points.append(point)    

    # I need the actual edges of the input
    # The output of max will by a tuple, so it gets the element [0][0] so the x coordinate of the set of coordinates
    maxVar = max(points, key=lambda x: x[0][0])[0][0]
    maxVarY = max(points, key=lambda x: x[0][1])[0][1]
    if (maxVarY>maxVar):
        maxVar=maxVarY
    minVar = min(points, key=lambda x: x[0][0])[0][0]
    minVarY = min(points, key=lambda x: x[0][1])[0][1]
    if (minVarY<minVar):
        minVar=minVarY
    
    # For each point in the area, associate it with the nearest "home" point(Part 1). 
    # If the total distance is <10000 increase the "safe" area (Part 2)
    area = 0
    for i in range(minVar,maxVar+1):
        for j in range(minVar,maxVar+1):
            index = findNearest((i,j),points)
            if index[0] != -1:
                points[index[0]][1].append((i,j))
            if index[1] < 10000:
                area+=1

    # Checks for the largest finite area.
    # I know an area is finite because no point in it touches an edge of the total area (checks it in isCursed)
    largest = 0 
    for p in points:
        if(not(isCursed(p[1],minVar,maxVar))):
            if(len(p[1])> largest):
                largest = len(p[1])

    print "Part one: "+ str(largest)
    print "Part two: "+ str(area)
    print "Time: " + str(time.time()-start_time)
