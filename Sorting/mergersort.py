# It is a divide and conquer algorithm.
# split the array until the single element is present in the list.

# There will be two steps 1. is to divide the array such that arr is left with only one element and other is to merge the splitted array.

#[1,3,2,4,5]
# TC -> nlogn   logn for the height of the recursion as everytime the array is being divided into 2 halves so total would be logn height and at every level for conquering we have to iterate over the n elements so "nlogn"

# in merge sort we can take the "extra space" as merger array to merge the array in the ascending order 

def main(nums):
    def conquer(arr,L,MID,R):
        merged = [-1]*(R-L+1)
        i=L
        j=MID+1
        k = 0
        while i<=MID and j<=R:
            if arr[i] < arr[j]:
                merged[k] = arr[i]    # merged[k++] = arr[i++] in some other languages
                i+=1
                k+=1
            else:
                merged[k] = arr[j]   # merged[k++] = arr[j++] in some other languages
                j+=1                   
                k+=1
        while i<=MID:
            merged[k] = arr[i]
            i+=1
            k+=1
        while j<=R:
            merged[k] = arr[j]
            j+=1
            k+=1
        j=0
        for i in range(L,R+1):
            arr[i] = merged[j]
            j+=1
    def divide(arr,l,r):
        if l==r:
            return 
        mid = (l+r)//2
        divide(arr,l,mid)
        divide(arr,mid+1,r)
        conquer(arr,l,mid,r)
    divide(nums,0,len(nums)-1)
    return nums
print(main([5,1,3,2,4]))