with open('input.txt') as f:
  lines = f.readlines()
  tmp = lines[0].split("[")[1].split("]")[0]
  lines.sort(key=lambda r: r.split("[")[1].split("]")[0])
  
  Guards = dict()
  for line in lines:
    gid = line.split(" ")[3].strip()
    if(gid[0]=="#"):
      currentguard= gid.replace("#","")
      print(currentguard)
    if(gid=="asleep"):
      timeasleep= int(line.split(" ")[1].split(":")[1].replace("]",""))
      print (timeasleep)
    if(gid=="up"):
      timewakeup = int(line.split(" ")[1].split(":")[1].replace("]",""))
      while(timeasleep<timewakeup):
        if currentguard in Guards:
          if timeasleep in Guards[currentguard]:
            Guards[currentguard][timeasleep]+=1
          else:
            Guards[currentguard][timeasleep]=1
        else:
          Hours= dict()
          Guards[currentguard]= Hours
        timeasleep+=1
  
  mostHours= 0
  mostMinuteAbs=0
  for g in Guards:
    mostMinute = 0
    totalMinutes = 0
    mostMinuteAmount =0
    for n in Guards[g]:
      totalMinutes+=Guards[g][n]
      if Guards[g][n] > mostMinuteAmount:
        mostMinuteAmount = Guards[g][n]
        mostMinute = n
    if totalMinutes >mostHours:
      mostHours=totalMinutes
      mostMinuteAbs = mostMinute*g
  print(mostMinuteAbs)


