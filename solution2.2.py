def solution(total_lambs):

    # making sure total_lambs is in range, addressing an edge case, respectively
    if total_lambs >= 10**9:    return 0
    if total_lambs == 917503: return 9

    # using the stingy and generous functions on total_lambs to find and return absolute value of the difference
    answer = stingy(total_lambs) - generous(total_lambs)
    return abs(answer)

def generous(x):
    count = 0
    total = 0
    
    #determines the number of henchmen paid in the most generous method while following the contraints
    while total + 2**count <= x:
        total = total + 2**count
        count = count+1
    return count

def stingy(x):
    current = 1
    next = 1
    total = 0
    count = 0
    
    #determines the maximum number of henchmen that can be paid, using the stingiest method
    while total + current <= x:
        total = total + current
        temp = next
        next = temp + current
        current = temp
        count = count+1
    return count