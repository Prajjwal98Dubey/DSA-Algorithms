# Quick sort is a partition based algorithm.
# We can first element or the last element or any random element as the pivot.
# After selecting the desired pivot we will place the pivot to its correct position which means the position of the pivot element in the sorted array.


def QuickSort(nums):
    def findPartition(arr,low,high):
        # print(arr[low])
        pivot = low
        i = low
        j = high
        while i < j:
            while arr[i] <= arr[pivot] and i<=high-1:
                i+=1
            while arr[j] > arr[pivot] and j>=low+1:
                j-=1
            if i<j:
                arr[i],arr[j] = arr[j],arr[i]
        arr[j],arr[pivot]  = arr[pivot],arr[j]
        return j
    def qs(arr,low,high):
        if low<high:
            index = findPartition(arr,low,high)
            qs(arr,low,index-1)
            qs(arr,index+1,high)
            return
    qs(nums,0,len(nums)-1)    
    return nums
print(QuickSort([10,1,5,6,2,3,9,8,7,4]))