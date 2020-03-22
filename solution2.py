from fractions import Fraction  

def solution(pegs):

    #determine if there is an odd or even number of pegs
    pegLen = len(pegs) 
    if (pegLen % 2 == 0):
        isEven = True
        sum = (-pegs[0] + pegs[pegLen -1])
    else:
        isEven = False 
        sum =(-pegs[0] - pegs[pegLen-1])   

    #account for the sum if there are more than 2 pegs
    if (pegLen > 2):
        for i in range(1, pegLen-1):
            sum += 2 * (-1)**(i+1) * pegs[i]
    
    #returns -1,-1 if there are only 0 or 1 pegs, 
    if ((not pegs) or pegLen == 1):
        return [-1,-1]

    #calculate radius, based on whether the peg number is odd or even
    firstRad = Fraction(2 * (float(sum)/3 if isEven else sum)).limit_denominator()
    currentRad = firstRad

    #iterate through list of pegs, calculating center distance, stopping if radius = 1
    for i in range(0, pegLen-2):
        center = pegs[i+1] - pegs[i]
        nextRad = center - currentRad
        if (currentRad < 1 or nextRad < 1):
            return [-1,-1]
        else:
            currentRad = nextRad

    return [firstRad.numerator, firstRad.denominator]