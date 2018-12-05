import string

def calcPolymer(string):
    safe = string[len(string)-1]
    string = string[:len(string)-1]
    rangel = len(string)
    for n in reversed(range(0,rangel)):
        if(string[n].lower()==safe[0].lower() and ((string[n].islower() and safe[0].isupper())or (string[n].isupper() and safe[0].islower()))):
            safe = safe[1:]
        else:
            safe = string[n] + safe
    return len(safe)

with open('./inputs/input5.txt') as f:
    line = f.read().strip()

    print "Part one: " + str(calcPolymer(line))

    minLen = 50000
    for char in string.ascii_lowercase:
        cLine = line.replace(char,"").replace(char.upper(),"")
        amount = calcPolymer(cLine)
        if amount<minLen:
            minLen= amount
    print "Part two: "+str( minLen)
