
# using dp on partitions will give TLE

'''
import collections
def sample(target,words,costs):
    hash = {}
    dp = {}
    for i in range(len(words)):
        hash[words[i]] = float("inf")
    for i in range(len(words)):
        hash[words[i]] = min(hash[words[i]],costs[i])
    def dfs(index):   # O(10^4)
        if index == len(target):
            return 0
        if index in dp:
            return dp[index]
        res = float("inf")
        s=""
        for i in range(index,len(target)):   # O(10^4)
            s+=target[i]
            if s in hash:  
                tmp = hash[s] + dfs(i+1)
                res = min(res,tmp)
        dp[index] = res
        return res
    ans = dfs(0)
    return ans if ans!=float("inf") else -1

    '''


def minimumCost(target,words,costs):
    pass


# print(minimumCost("r",["r","r","r","r"],[6,3,1,3]))
# print(minimumCost("abcdef",["abdef","abc","d","def","ef"],[100,1,1,10,5]))
