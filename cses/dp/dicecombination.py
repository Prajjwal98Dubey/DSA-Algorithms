# solve the smaller problems or the sub problem to solve the larger problem

# def diceCombination(n):
    # dp = [0]*(n+1)
    # MOD = (10**9) + 7
    # dp[0] = 1
    # for i in range(1,n+1):
    #     for j in range(1,7):
    #         if (i-j >=0):
    #             dp[i]+=dp[i-j]%MOD
    # return dp[n]%MOD
import collections
def diceCombination(n):
    q = collections.deque()   # [1,2,3,4,5,6]
    dp = [0] * (7)
    dp[0] = 1
    MOD = (10**9) + 7
    for i in range(1,7):
        for j in range(1,7):
            if (i-j>=0):
                dp[i]+=dp[i-j]
        q.append(dp[i])
    if n < 7:
        return dp[n]
    index = 7
    while index < n:
        t = sum(q)%MOD
        q.append(t)
        q.popleft()
        index+=1
    return sum(q)%MOD
n = int(input())
ans = diceCombination(n)
print(ans)
