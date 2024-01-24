
def batteryPercentages(battery):
    nums = battery
    index = 0 
    cnt=0
    while index<len(nums):
        if nums[index] ==0:
            index+=1
            continue
        cnt+=1
        for j in range(index+1,len(nums)):
            nums[j] = max(0,nums[j]-1)
        index+=1
    return cnt
print(batteryPercentages([0,1,2]))