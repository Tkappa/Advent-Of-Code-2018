# Counter class used in part on
from collections import Counter

with open('input2.txt') as f:
    lines = f.readlines()
    ntwo=0
    nthree=0
    for line in lines:
        #Discovered counters comparing myself to a solution on reddit, wow they are powerful!
        # for each tuple i,j (letter,number) created using counter.most_common, get only the number(j)
        nletters = [j for i,j in Counter(line).most_common()]
        if 3 in nletters:
            nthree+=1
        if 2 in nletters:
            ntwo+=1
        # My old(first) solution
        """
        two=0
        three=0

        for c in line:
            if line.count(c) == 2:
                two = 1
            if line.count(c) ==3:
                three=1
        if two==1:
            ntwo=ntwo+1
        if three==1:
            nthree=nthree+1
        """
    print "Part one: " + str(ntwo*nthree)
    found = 0
    for line in lines:
        for bline in lines:
             diff = 0
             lis = zip(line,bline)
             for c in lis:
                 if (c[0] != c[1]):
                     diff+=1
             """
             Discovered zip on reddit
             index=0
             for c in line:
                 if(line[index] != bline[index]):
                     diff+=1
                 index+=1
             """    
             if(diff == 1):
                common =""
                lis = zip(line,bline)
                for c in lis:
                    if(c[0]==c[1]):
                        common+=c[0]
                """
                index=0
                for c in line:
                    if(line[index] == bline[index]):
                        common+=c
                    index = index + 1
                """
                print "Part two: " + common
                found = 1
                break
        if (found==1):
            break
