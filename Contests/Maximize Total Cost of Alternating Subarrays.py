'''
 there are three changing states -> index,start,sign
'''

def maximiseTotalCost(nums):
    def dfs(index,start,sign):
        if index == len(nums):
            return 0
        res = -float("inf")
        if start:
            res = max(res,nums[index]+dfs(index+1,False,not sign))
        else:
            if sign:
                res = max(res,-nums[index] + dfs(index+1,False,not sign))
                res = max(res,nums[index] + dfs(index+1,False,False))
            else:
                res = max(res,nums[index] + dfs(index+1,False,not sign))
                res = max(res,nums[index] + dfs(index+1,False,False))
        return res
    return dfs(0,0,0)
    
print(maximiseTotalCost([0]))
