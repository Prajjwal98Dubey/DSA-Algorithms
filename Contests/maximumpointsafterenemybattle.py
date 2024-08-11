'''
'''
def maximumPoints(enemyEnergies,currentEnergy):
    enemyEnergies.sort()
    points = 0 
    for i in range(len(enemyEnergies)):
        if currentEnergy >= enemyEnergies[i]:
            currentEnergy-=enemyEnergies[i]
            points+=1
            break
    if points == 0:
        return 0
    hash = set() # all the marked indices
    l,r=0,len(enemyEnergies)-1
    while l < len(enemyEnergies):
        if currentEnergy  >= enemyEnergies[l]:
            if l not in hash:
                tmp = currentEnergy // enemyEnergies[l]
                rem = currentEnergy % enemyEnergies[l]
                points+=tmp
                currentEnergy = rem
            else:
                l+=1
        else:
            currentEnergy+=enemyEnergies[r]
            hash.add(r)
            r-=1
    return points
print(maximumPoints([2],10))

'''  
[2,2,3]      p-> 3    curr = 0 - 3 - 1 - 3 - 1 - 3
'''
    
