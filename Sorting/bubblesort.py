# Bubble sort in O(n*n) TC algo.
def bubbleSort(nums):
    for _ in range(len(nums)):
        j = 0
        k = j+1
        while k < len(nums):
            if nums[k] < nums[j]:
                nums[k],nums[j] = nums[j],nums[k]
            k+=1
            j+=1   
    return nums
print(bubbleSort([5,1,3,2,4]))