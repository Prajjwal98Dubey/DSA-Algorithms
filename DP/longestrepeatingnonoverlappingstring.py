# Pure Tabulation question
def longestSubstring(s):
    dp=[[0 for j in range(len(s))]for i in range(len(s))]
    maxi=-1
    indexes = [-1,-1]
    for i in range(len(s)):
        for j in range(i+1,len(s)):
            if s[i]==s[j]:
                dp[i][j] = 1+dp[i-1][j-1] if i-1>=0 else 1
                if dp[i][j] > j-i:       # IMP- edge case 
                    dp[i][j] = 0
                if dp[i][j] > maxi:
                    maxi = dp[i][j]
                    indexes[0] = i
                    indexes[1] = j
            else:
                dp[i][j]=0
    i,j = indexes[0],indexes[1]
    res =""
    while maxi:
        res+=s[i]
        i-=1
        j-=1
        maxi-=1
    res = res[::-1]
    print(maxi)
    print(dp)
    return res
print(longestSubstring("heheheh"))
