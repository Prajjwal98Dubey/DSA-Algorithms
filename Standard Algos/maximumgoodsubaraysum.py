
def maximumSubarraySum(nums,k):
    # create the prefix sum array
    prefix=[]
    for i in range(len(nums)):
        if not prefix:
            prefix.append(nums[i])
        sum = prefix[-1] + nums[i]
        prefix.append(sum)
    print(prefix)
    hash={}
    for i in range(len(nums)):
        if nums[i]-k in hash:
            tmp=0
            if hash[nums[i]-k]-1 >=0:
                tmp =  prefix[hash[nums[i]-k]-1]
            sum  = prefix[i] - tmp
        else:
            hash[nums[i]]=i





print(maximumSubarraySum([-1,3,2,4,5],3))