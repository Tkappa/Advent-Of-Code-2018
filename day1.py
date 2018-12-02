with open('input1.txt') as f:
    lines = f.readlines()
    amount = 0
    D = dict()
    D[0]= 1
    breakcycle =1
    firsttime = 0 
    while breakcycle==1:
        for f in lines:
            amount += int(f)
            if amount in D:
                print "Part two:" + str(amount)
                breakcycle = 2
                break
            else:
                D[amount]= 1
        if firsttime == 0:
            print "Part one:"+ str(amount)
            firsttime= 1
