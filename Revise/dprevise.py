# minimum number of jumps ->
# https://www.geeksforgeeks.org/problems/minimum-number-of-jumps-1587115620/1?page=1&company=Google&difficulty=Medium,Hard&sortBy=submissions
def minimumJumps(arr):
    l=r=0
    res=0
    while r < len(arr)-1:
        fartest = 0
        for i in range(l,r+1):
            fartest=max(fartest,i+arr[i])
        l=r+1
        r=fartest
        res+=1
    return res