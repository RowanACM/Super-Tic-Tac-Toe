import sys

#set variables for players
mePlayer = 2;
noPlayer = 1;
opPlayer = 0;

lowestH = 3;
highestH = 100;

#setup array for state of the board
boardState = [[]];
localState = [];

def main(args):
    print "Test"
    pass

def readBoardState():
    
    #read the state into the state variables declared above
    
    pass

#currently, this only works with a local board (for testing purposes)
def h(): #return an array of ints representing the score of each space to hit
    #notes: 3 is the lowest heuristic value to be assigned (it is higher than 2, which is the value for the current player
    
    hValues = []; #the values of each free space will be stored here
    
    #setup vars for two-in-a-row cases
    meTwo = [[]]; #this is the matrix of places in the board the current player has two in a row
    meTwoAmount = 0;
    opTwo = [[]];
    opTwoAmount = 0;
    
    #scan for two-in-a-row cases
    it = [0,1];
    
    while it[0]>-1:
        if localState[it[0]] == localState[it[1]]:
            if localState[it[0]] == mePlayer:
                meTwo[meTwoAmount] = it;
                meTwoAmount = meTwoAmount+1;
            elif localState[it[0]] == opPlayer:
                opTwo[opTwoAmount] = it;
                opTwoAmount = opTwoAmount+1;
        
        it = cIterate(it);
    #reach this point when iteration is done
    
    #save the state of the four corners in corner array
    corners = [];
    corners[0] = localState[0];
    corners[1] = localState[2];
    corners[2] = localState[6];
    corners[3] = localState[8];
    
    meCorners = [];
    meCornersAmount = 0;
    opCorners = [];
    opCornersAmount = 0;
    
    for i in range(0,3):
        if corners[i] == mePlayer:
            meCorners[meCornersAmount] = i;
            meCornersAmount = meCornersAmount + 1;
        elif corners[i] == opPlayer:
            opCorners[opCornerAmount] = i;
            opCornersAmount = opCornersAmount + 1;
    
    #now, handle cases in order
    if meTwoAmount > 0:
        #find all spaces that would complete the chain
        spaces = findAdjacent(mePlayer,meTwo,meTwoAmount);
        size = len(spaces);
        #set heuristic values
        for i in range(0,size):
            hValues[spaces[i]] = highestH;
            
    if opTwoAmount > 0:
        #find all spaces that would complete the chain
        spaces = findAdjacent(opPlayer,opTwo,opTwoAmount);
        size = len(spaces);
        for i in range(0,size):
            hValues[spaces[i]] = highestH-1;
            
    if meCornerAmount > 1:
        #case reached: current has two corners
        if opCornerAmount < 2:
            #case reached: at least one other corner is free
    elif meCornerAmount == 1:
        #case reached: current has one corner
        #check if the opposite corner is empty
        opIndex; #store the index of opposite corner
        if meCorners[0] == 0:
            opIndex = 3;
        elif meCorners[0] == 1:
            opIndex = 2;
        elif meCorners[0] == 2;
            opIndex = 1;
        else
            opIndex = 0;
            
        if corners[opIndex] == noPlayer:
            #case reached: opposite corner is empty
            if opCornersAmount < 2:
                #case reached: at least one other corner is empty
                #find the adjacent corners and check those
                adJOne;
                adJTwo;
                
                if opIndex == 0:
                    adJOne = 1;
                    adJTwo = 3;
                elif opIndex == 1:
                    adJOne = 1;
                    adJTwo = 5;
                elif opIndex == 2:
                    adJOne = 3;
                    adJTwo = 7;
                else:
                    adJOne = 5;
                    adJTwo = 7;
                
    
    
    pass

def findAdjacent(p,pTwo,pTwoAmount): #player, array of places where there are two in a row
    spaces = [];
    it = [0,1];
    
    for i in range(0,pTwoAmount):
        cTwo = pTwo[i]; #get the row corresponding to the pair we want to analyze
        if cTwo[0] == 0:
            if cTwo[1] == 1:
                spaces[i] = 2;
            elif cTwo[1] == 3:
                spaces[i] = 6;
            else
                spaces[i] = 8;
        elif cTwo[0] == 1;
            if cTwo[1] == 2:
                spaces[i] = 0;
            else:
                spaces[i] = 7;
        elif cTwo[0] == 2;
            if cTwo[1] == 4:
                spaces[i] = 6;
            else:
                spaces[i] = 8;
        elif cTwo[0] == 3:
            if cTwo[1] == 4:
                spaces[i] = 5;
            elif cTwo[1] == 6:
                spaces[i] = 0;
        elif cTwo[0] == 4:
            if cTwo[1] == 5:
                spaces[i] = 3;
            elif cTwo[1] == 6:
                spaces[i] = 2;
            elif cTwo[1] == 7:
                spaces[i] = 1;
            else:
                spaces[i]= 0;
        elif cTwo[0] == 5:
            spaces[0] = 2;
        elif cTwo[0] == 6:
            spaces[i] = 8;
        else:
            spaces[i] = 6;
    #end of loop
    
    return spaces;
    

def cIterate(n): #this is a custom iterator used to interpret the state of the board; this function handles the iteration itself
    
    if n[0] == 0:
        if n[1] == 1:
            n[1] = 3;
        elif n[1] == 3:
            n[1] = 4;
        else:
            n[0] = 1;
            n[1] = 2;
    elif n[0] == 1:
        if n[1] == 2:
            n[1] = 4;
        else:
            n[0] = 2;
            n[1] = 5;
    elif n[0] == 2:
        if n[1] == 4:
            n[1] = 5;
        else:
            n[0] == 3;
            n[1] == 4;
    elif n[0] == 3:
        if n[1] == 4:
            n[1] = 6;
        else:
            n[0] = 4;
            n[1] = 5;
    elif n[0] == 4:
        if n[1] == 5:
            n[1] = 6
        elif n[1] == 6:
            n[1] = 7;
        elif n[1] == 7:
            n[1] = 8;
        else:
            n[0] = 5;
            n[1] = 8;
    elif n[0] == 5:
        n[0] = 6;
        n[1] = 7;
    elif n[0] == 6:
        n[0] = 7;
        n[1] = 8;
    else:
        n[0] = -1; #case that we are done iterating
    
    return n

if __name__=="__main__":
    main(sys.argv)