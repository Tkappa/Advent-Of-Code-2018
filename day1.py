with open('input.txt') as f:
    lines = f.readlines()
    amount = 0
    D = dict()
    D[0]= 1
    hehe =1
    firsttime = 0 
    while hehe==1:
        for f in lines:
            amount += int(f)
            if amount in D:
                print "Part two:" + str(amount)
                hehe = 2
                break
            else:
                D[amount]= 1
        if firsttime == 0:
            print "Part one:"+ str(amount)
            firsttime= 1
