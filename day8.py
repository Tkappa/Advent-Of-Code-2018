import time

def readNode(currentnode,index,numbers,maxsum):
    # Gets the headers and sets it to the current node
    nchildren = int(numbers[index])
    index+=1
    nmetadata = int(numbers[index])
    currentnode[0][0]=nchildren
    currentnode[0][1]=nmetadata
    index+=1

    # if it has children
    if nchildren>0:
        for n in range(nchildren):
            # Create a new node and read it recursevly
            # The node is made by [[headers],[children],node value for part 2
            node = [[-1,-1],[],0]
            currentnode[1].append(node)
            # retval is a tuple made of (index,maxsum for part one)
            retval=readNode(node,index,numbers,maxsum)

            index=retval[0]
            maxsum=retval[1]

    # if it has some metadata values
    currentsum=0
    for n in range(nmetadata):
        # Part two:
        #   If it has children:
        #       If the children in index exists:(is less than the number of children
        #           Sum the child value
        #   Else:
        #       sum the metadata value as an integer
        if(currentnode[0][0]>0):
            if int(numbers[index])<=currentnode[0][0]:
                # Do numbers[index]-1 because the array starts at 0 , while the input starts at 1
                currentsum+=currentnode[1][int(numbers[index])-1][2]
        else:
            currentsum+=int(numbers[index])

        # Part one:
        maxsum += int(numbers[index])
        index+=1
    currentnode[2]=currentsum
    return (index,maxsum)

with open ("./inputs/input8.txt") as f:
    start_time= time.time()
    numbers= f.read().split(" ")

    index = 0
    head = [[-1,-1],[],[],0]
    maxsum=0

    retval=readNode(head,index,numbers,maxsum)

    print "Part one: "+ str(retval[1])
    print "Part two: "+ str(head[2])
    print "Time: "+ str(time.time()-start_time)
