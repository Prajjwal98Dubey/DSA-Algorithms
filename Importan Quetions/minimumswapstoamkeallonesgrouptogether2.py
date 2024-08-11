#LC 2134

'''
[1,1,0,1,1,1 0,1]
[0,1,1,1,0,0,1,1,0]

[0,0,0]
[1,1,1]
'''
def minSwaps(nums):
    '''
    arr = nums + nums
    l,r=0,0
    totalOnes = nums.count(1)
    currOnes = 0
    swaps = float("inf")
    while r < len(arr):
        if arr[r]==1:
            currOnes+=1
        if r-l+1 ==totalOnes:
            swaps=min(swaps,totalOnes-currOnes)
            if arr[l]==1:
                currOnes-=1
            l+=1
        r+=1
    return swaps if swaps!=float("inf") else 0
    '''
    l,r=0,0
    totalOnes = nums.count(1)
    currOnes = 0
    swaps = float("inf")
    N = 2*len(nums)
    while r < N:
        if nums[r%N]==1:
            currOnes+=1
        if (r%N)-(l%N)+1 ==totalOnes:
            swaps=min(swaps,totalOnes-currOnes)
            if nums[(l%N)]==1:
                currOnes-=1
            l+=1
        r+=1
    return swaps if swaps!=float("inf") else 0

print(minSwaps([1,1,1]))
print(minSwaps([0,0,0]))        
print(minSwaps([0,1,1,1,0,0,1,1,0]))
        

