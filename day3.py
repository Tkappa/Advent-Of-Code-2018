with open('./inputs/input3.txt') as f:
  lines= f.readlines()
  D = dict()

  # Part one
  for line in lines:
    # A input string il like this #1 @ 287,428: 27x20
    # So coord is 287,428 and amount 27x20
    coord = line.split("@")[1].split(":")[0].split(",")
    amount = line.split("@")[1].split(":")[1].split("x")

    coord= (int(coord[0].strip()), int(coord[1].strip() ))
    amount= (int(amount[0].strip()),int(amount[1].strip()))

    indexx = 0
    while(indexx<amount[0]):
      indexy = 0
      while(indexy<amount[1]):
        newcord = (coord[0]+indexx ,coord[1]+indexy)
        if newcord in D:
            D[newcord]+=1
        else:
          D[newcord]=1
        indexy+=1
      indexx+=1

  total = 0
  for num in D:
    if(D[num]>1):
      total+=1
  print ("Part one: " + str(total))

  #Part two
  for line in lines:
    coord = line.split("@")[1].split(":")[0].split(",")
    amount = line.split("@")[1].split(":")[1].split("x")

    coord= (int(coord[0].strip()), int(coord[1].strip() ))
    amount= (int(amount[0].strip()),int(amount[1].strip()))

    stillone=1 # Checks if the D[coord] value stays 1 while iterating
    entered= 0 # Cheks if it has entered the cycle
    if(D[coord]==1):
        entered=1
        indexx = 0
        while(indexx<amount[0] and stillone==1):
          indexy = 0
          while(indexy<amount[1] and stillone==1):
            newcord = (coord[0]+indexx ,coord[1]+indexy)
            if(D[newcord]!=1):
                stillone = 0
            indexy+=1
          indexx+=1
    # If it has entered the cycle and has ended it without exiting early it means its the one without overlapping
    if(stillone==1 and entered ==1):
        print "Part two: "+ line.split("@")[0].replace('#','')
        break
