# GFG -> count digits grouping of a number.
# this code will give TLE
# def countGroups(s):
#     ans=[]
#     curr= []
#     def backTrack(index):
#         if index==len(s):
#             ans.append(curr.copy())
#             return
#         for i in range(index,len(s)):
#             curr.append(s[index:i+1])
#             backTrack(i+1)
#             curr.pop()
#     backTrack(0)
#     def sumOfDigits(s1):
#         sum=0
#         for i in s1:
#             sum+=int(i)
#         return sum
#     groups=0
#     for i in range(len(ans)):
#         if len(ans[i])==1:
#             groups+=1
#             continue
#         flag =1
#         for j in range(1,len(ans[i])):
#             if sumOfDigits(ans[i][j-1]) > sumOfDigits(ans[i][j]):
#                 flag=0
#                 break
#         if flag:
#             groups+=1
#     print(ans)
#     return groups

# index , prevSum ,length

# Memoization
# memoise the sum of digits as well to pass the large testcases.
def TotalCount(s):
    memo={}
    def sumOfDigits(s1):
        if s1 in memo:
            return memo[s1]
        sum=0
        for i in s1:
            sum+=int(i)
        memo[s1]=sum
        return sum
    # ans=[0]
    dp={}
    def dfs(index,prev):
        if index==len(s):
            return 1
        if (index,prev) in dp:
            return dp[(index,prev)]
        ans=0
        for i in range(index,len(s)):
            if prev==0 or prev<=sumOfDigits(s[index:i+1]):
                ans+=dfs(i+1,sumOfDigits(s[index:i+1]))
        dp[(index,prev)]=ans
        return ans
    return dfs(0,0)

# Tabulation:
def TotalCount(self, s):
    n = len(s)
    dp = [[0] * (n + 1) for _ in range(n + 1)]
    
    for i in range(n + 1):
        dp[i][n] = 1

    for i in range(n - 1, -1, -1):
        for j in range(n, 0, -1):
            dp[i][j-1] = dp[i][j]
            if j <= sum(int(c) for c in s[i:]):
                dp[i][j-1] += dp[i+1][j]

    return dp[0][0]
    
print(TotalCount("1119"))