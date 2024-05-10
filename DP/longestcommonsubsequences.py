# Recursion + Memoization

# def LCS(s1,s2):
#     dp={}
#     def dfs(index1,index2):
#         if index1<0 or index2<0:
#             return 0
#         if (index1,index2) in dp:
#             return dp[(index1,index2)]
#         match,notmatch = 0,0
#         if s1[index1] == s2[index2]:
#             match  = 1 + dfs(index1-1,index2-1)
#         else:
#             notmatch = max(dfs(index1-1,index2),dfs(index1,index2-1))
#         dp[(index1,index2)] = max(match,notmatch)
#         return max(match,notmatch)
#     return dfs(len(s1)-1,len(s2)-1)

# Tabulation

def LCS(s1,s2):
    dp=[[0 for j in range(len(s2)+1)]for i in range(len(s1)+1)]
    for j in range(len(s2)+1):
        dp[0][j]=0
    for i in range(len(s1)+1):
        dp[i][0]=0
    for i in range(1,len(s1)+1):
        for j in range(1,len(s2)+1):
            match,notmatch = 0,0
            if s1[i-1] == s2[j-1]:
                match  = 1+dp[i-1][j-1]
            else:
                notmatch = max(dp[i-1][j],dp[i][j-1])
            dp[i][j] = max(match,notmatch)
    # printing the longest common subsequence
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
    return res[::-1]
    # return dp[len(s1)][len(s2)]

print(LCS("aksjdsdk","eorieow"))