'''
0 < x,y,z <= 10**8

x - 8
y - 5
z - 3


8,9,10,11

8 - selected    operationLeft : 3


19 //2 -> 9 

'''
def maximiseX(x,y,z):
    maxi = x
    l = maxi
    r = x + z
    while l<=r:
        mid = (l+r)//2
        remainingOperations = z - (mid - x)
        if mid - remainingOperations > y:
            r = mid-1 
        else:
            maxi = max(mid,maxi)
            l = mid+1
    return maxi

print(maximiseX(5,5,8))