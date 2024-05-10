# TC -> O(len(line)*len(line)) SC->O(len(line)) + O(len(line))
def wordBreak(line,dictionary):
    hash = set(dictionary)
    dp={}
    def dfs(index):
        if index==len(line):
            return True
        if index in dp:
            return dp[index]
        res = False
        for i in range(index,len(line)):
            if line[index:i+1] in hash:
                res = res or dfs(i+1)
        dp[index] = res
        return res
    return dfs(0)


print(wordBreak("ilikesamsunge",["i", "like", "sam", "sung", "samsung", "mobile"]))