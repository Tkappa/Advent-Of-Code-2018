import time
import string

with open("./inputs/input7.txt") as f:
    start_time = time.time()
    lines = f.readlines()
        
    steps = []
    ptwo_steps = []
    
    # Initialize the arrays with [char,boolean array of n=26]
    # The boolean array will represent the letters that are blocking the current one
    for c in string.ascii_uppercase:
        steps.append([c,[False]*26])
        ptwo_steps.append([c,[False]*26])

    # Read the input and fill the arrays
    for line in lines: 
        blocked = line.split()[7]
        blocking = line.split()[1]
        steps[ord(blocked)-65][1][ord(blocking)-65]=True
        ptwo_steps[ord(blocked)-65][1][ord(blocking)-65]=True


    # Part one
    # Read the array:
    #  If you encounter a index that is not blocked by anything:
    #    Unblock all the letters that are waiting for the current one
    #    Block himself to signal that he finished
    #    ReStart reading from the beginning
    #  Else : continue reading
    order=""
    index = 0
    while index<26:
        if (not(any(steps[index][1]))):
            for n in range(26):
                steps[n][1][index]=False
            order+=steps[index][0]
            steps[index][1][index]=True
            index=0
        else:
            index+=1
    
    # Part two

    # Variable that keeps the current time
    ctime = 0
    # List of active workers
    workers =[]
    # Variable that can break the cycle
    finished=False
    while finished==False:
        bfound=False
        # If there are workers:check which one has finished, unblock all the other letters from the current, and free the worker
        if len(workers)>0:
            bfound=True
            found = [x for x in workers if x[1]==ctime][0]
            for n in range(26):
                ptwo_steps[n][1][found[0]]=False
            ptwo_steps[found[0]][1][found[0]]=True
            workers.remove(found)
        # Search for other letters that can be worked on, checks also if its being worked on and if there are workers free before starting the job
        for n in range(26):
            if (not(any(ptwo_steps[n][1]))):
                found = [x for x in workers if x[0]==n]
                if len(found)==0:
                    if(len(workers)<5):
                        # 61 because n starts from 0, and the time starts from 1
                        workers.append([n,ctime+61+n])
                        bfound=True
        # Skips the time to the next worker that will finish
        if len(workers)>0:
            ctime=min(workers, key=lambda x: x[1])[1]
        if bfound==False:
            finished = True


    print "Part one: "+str(order)
    print "Part two: "+str(ctime)
    print "Time: "+ str(time.time()-start_time)
