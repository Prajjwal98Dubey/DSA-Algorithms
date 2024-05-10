# partiton array of maximum sum  LC-> 1043

def partitionSum(arr,k):
    dp={}
    def dfs(index):
        if index==len(arr):
            return 0
        if index in dp:
            return dp[index]
        maxi=-1
        res=-1
        for i in range(index,len(arr)):
            if i < index+k:
                maxi=max(maxi,arr[i])
                res=max(res,(i-index+1)*maxi + dfs(i+1))
        dp[index] = res
        return res
    return dfs(0)
print(partitionSum([1],1))