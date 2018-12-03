with open('input3.txt') as f:
  lines= f.readlines()
  D = dict()
  for line in lines:
    spline = line.split("@")
    values = spline[1].split(":")
    coord = values[0].split(",")

    coord[0] = coord[0].strip()
    coord[1] = coord[1].strip()
    amount = values[1].split("x")
    amount[0]= amount[0].strip()
    amount[1]= amount[1].strip()
    indexx = 0
    while(indexx<int(amount[0])):
      indexy = 0
      while(indexy<int(amount[1])):
        newcord =[0,0]
        newcord[0]= int(coord[0])+indexx
        newcord[1]= int(coord[1])+indexy
        scord = str(newcord[0]) + ','+ str(newcord[1])
        if scord in D:
          D[scord]+=1
        else:
          D[scord]=1
        indexy+=1
      indexx+=1
  total = 0
  for num in D:
    if(D[num]>1):
      total+=1
  print ("Part one: " + str(total))
  
  """
  Part 2 work in progress
  single = ""
  for num in D:
    if(D[num]==1):
      single = num
      print (num)
      break
  print (single)
  for line in lines:
    spline = line.split("@")
    values = spline[1].split(":")
    coord = values[0].strip()
    if(coord==single):
      print(spline[0]) 
    """
