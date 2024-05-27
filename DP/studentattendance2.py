'''
Another approach is written at the bottom.

def studentAttendence(n):
    MOD = (10**9) + 7
    # dp={}
    dp =[[[-1 for _ in range(3)]for _ in range(2)]for _ in range(n+1)]
    def dfs(index,absent,late):
        if index == n:
            return 1
        # reports = 0
        if dp[index][absent][late] !=-1:
            return dp[index][absent][late]
        A,P,L = 0,0,0
        if absent < 1 :
            A = dfs(index+1,absent+1,0)
        else:
            A = 0
        if late < 2:
            L = dfs(index+1,absent,late+1)
        else:
            L = 0 
        P = dfs(index+1,absent,0)
        # dp[(index,absent,late)] = reports
        dp[index][absent][late] = A+P+L
        return  A+P+L
    return dfs(0,0,0) % MOD
print(studentAttendence(100000))
'''
def studentAttendance(n):
    MOD = (10**9) + 7
    dp =[[[-1 for _ in range(3)]for _ in range(2)]for _ in range(n+1)]
    def dfs(index,absent,late):
        if absent > 1 or late > 2:
            return 0
        if index == n:
            return 1
        if dp[index][absent][late] !=-1:
            return dp[index][absent][late]
        reports = 0
        reports += dfs(index+1,absent+1,0) % MOD
        reports+=dfs(index+1,absent,late+1) % MOD
        reports+=dfs(index+1,absent,0)% MOD
        dp[index][absent][late] = reports
        return reports
    return dfs(0,0,0)
    
print(studentAttendance(10000))