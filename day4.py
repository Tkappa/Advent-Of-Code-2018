import time

with open('./inputs/input4.txt') as f:
  start_time = time.time()
  lines = f.readlines()

  # Sort the array by date
  lines.sort()

  Guards = dict()
  for line in lines:
    action = line.split(" ")[3].strip()
    #If it has a hashtag its a guard shift , so it gets the new guard
    if(action[0]=="#"):
      currentguard= action.replace("#","")
    #If the word is asleep , the guard just fell asleep, so i store the time
    if(action=="asleep"):
      timeasleep= int(line.split(" ")[1].split(":")[1].replace("]",""))
    #If the word is up, the guard has woken up, so I increment the times
    if(action=="up"):
      timewakeup = int(line.split(" ")[1].split(":")[1].replace("]",""))
      for t in range(timeasleep,timewakeup):
        if currentguard in Guards:
          if t in Guards[currentguard]:
            Guards[currentguard][t]+=1
          else:
            Guards[currentguard][t]=1
        else:
          Hours= dict()
          Guards[currentguard]= Hours


  mostMinutes= 0
  partOneChecksum=0

  #( which guard , which minute, numberoftimesslept)
  mostminutesleptbyguard=(0,0,0)

  #For all guards
  for currentguard in Guards:
    bestMinuteCycle = 0
    totalMinutesCycle = 0
    mostMinuteAmountCycle =0
    #For all minutes they slept
    for currentminute in Guards[currentguard]:
        if Guards[currentguard][currentminute] > mostminutesleptbyguard[2]:
            mostminutesleptbyguard = (currentguard,currentminute,Guards[currentguard][currentminute])
        totalMinutesCycle+=Guards[currentguard][currentminute]
        if Guards[currentguard][currentminute] > mostMinuteAmountCycle:
          mostMinuteAmountCycle = Guards[currentguard][currentminute]
          bestMinuteCycle = currentminute
    if totalMinutesCycle >mostMinutes:
        mostMinutes=totalMinutesCycle
        partOneChecksum = int(bestMinuteCycle)*int(currentguard)

  print "Part one: "+ str(partOneChecksum)
  print "Part two: "+ str(int(mostminutesleptbyguard[0])*int(mostminutesleptbyguard[1]))
  print "Time: "+ str(time.time()-start_time)
