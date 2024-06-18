'''

dp[power] = max(dp[power-1],dp[power-2],dp[power-3]+(occurance of power * power))

dp[power-3] cannot exists which means we have to find out the power in the power array which has the difference of power with the current power >=3 and most closest to the current power --> for this we can use binary search.


'''
def maximumTotalDamage(power):
    power.sort()
    def bs(c):
        possible = -1
        l=0
        r=len(power)-1
        while l<=r:
            m = (l+r)//2
            mid = power[m]
            if c - mid >=3:
                possible = mid
                l = m+1
            else:
                r=m-1
        return possible
    hash = {}
    for p in power:
        if p in hash:
            hash[p]+=1
        else:
            hash[p]=1
    dp={}
    dp[0]=0
    for key in hash:
        dp[key] = 0
    for key in hash:
        x,y=0,0
        if key-1 in hash:
            x = dp[key-1]
        if key-2 in hash:
            y = dp[key-2]
        result = bs(key)
        z=  result if result >= 0 else 0
        dp[key] = max(x,y,hash[key]*key + dp[z])
    res = 0
    for key in dp:
        res = max(res,dp[key])
    return res


print(maximumTotalDamage([4,5,5,6,3,6,5,3,4]))