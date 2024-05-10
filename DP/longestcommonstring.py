#longest common substring
def LCS(s1,s2):
    dp =[[0 for j in range(len(s2)+1)]for i in range(len(s1)+1)]
    for j in range(len(s2)+1):
        dp[0][j]=0
    for i in range(len(s1)+1):
        dp[i][0]=0
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            if s1[i-1]==s2[j-1]:
                dp[i][j] = 1+dp[i-1][j-1]
            else:
                dp[i][j]= 0
    res = ""
    i,j = len(s1),len(s2)
    while i>0 and j>0:
        if s1[i-1]==s2[j-1]:
            res+=s1[i-1]
            i-=1
            j-=1
        elif dp[i-1][j] > dp[i][j-1]:
            i-=1
        else:
            j-=1
    print(res[::-1])
    return dp[len(s1)][len(s2)]

print(LCS("acbce","ace"))
