
def waterThePlants(nums):
    # create the ranges
    intervals=[]
    for i in range(len(nums)):
        if nums[i]==-1:
            continue
        s = i-nums[i]
        e = i+nums[i]
        intervals.append([max(s,0),min(e,len(nums)-1)])
    # sort the intervals on the basis of the start of the range.
    intervals.sort()
    print(intervals)
    # find the minimum number of the sprinklrs.
    def dfs(index,prev,c):
        if prev[0]==0 and prev[1]==len(nums)-1:
            return c
        if index==len(intervals):
            return float("inf")
        # if prev[1]==
        nottake = dfs(index+1,prev,c)
        take = float("inf")
        if prev[0]==float("inf") or intervals[index][0]<prev[1]<intervals[index][1] :
            take =  dfs(index+1,[min(prev[0],intervals[index][0]),max(prev[1],intervals[index][1])],c+1)
        return min(nottake,take)
    res= dfs(0,[float("inf"),-1],0)  # [-1,-1]
    return res
print(waterThePlants([-1, 2, 2, -1, 0, 0]))