def fractionalKnapsack(weight,values,W):
    # DP solution
    # dp={}
    # def dfs(index,W):
    #     if W == 0:
    #         return 0
    #     if index==len(values):
    #         return 0
    #     if (index,W) in dp:
    #         return dp[(index,W)]
    #     nottake = dfs(index+1,W)
    #     take = 0 
    #     if weight[index] <= W:
    #         take =  values[index] + dfs(index+1,W-weight[index])
    #     else:
    #         # W--> 20 weight[index]->30
    #         unit_value = values[index] / weight[index]
    #         take  = unit_value * W + dfs(index+1,W-W) 
    #     dp[(index,W)]=max(take,nottake)
    #     return max(take,nottake)
    # return dfs(0,w)


    # greedy solution
    # sort on the basis of the unit value of the items and be greedy about the maximum value.
    nums=[]
    for i in range(len(values)):
        nums.append([values[i],weight[i]])
    nums.sort(key = lambda x:x[0]/x[1],reverse=True)
    print(nums)
    profit = 0
    for i in range(len(nums)):
        if W ==0:
            break
        if W < nums[i][1]:
            profit+=W * (nums[i][0]/nums[i][1])
            break
        profit+=nums[i][0]
        W-=nums[i][1]
    return profit
print(fractionalKnapsack([10,20],[60,100],50))