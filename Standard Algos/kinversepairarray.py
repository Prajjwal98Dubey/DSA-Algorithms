#[1,2,3]
def kInversePairs(n,k):
    # find pairs
    #[2,1,3]
    def findPairs(arr):
        c=0
        for i in range(len(arr)):
            for j in range(i+1,len(arr)):
                if arr[i] > arr[j]:
                    c+=1
        return c
    nums = []
    for i in range(1,n+1):
        nums.append(i)
    # create the permutation list
    curr=[]
    perm=[]
    hash=set()
    def backTrack():
        if len(curr.copy())==len(nums):
            perm.append(curr.copy())
            return
        for i in nums:
            if i not in hash:
                curr.append(i)
                hash.add(i)
                backTrack()
                curr.pop()
                hash.remove(i)
        return 
    backTrack()
    # find the inverse pairs
    total=0
    for arr in perm:
        if findPairs(arr)==k:
            total+=1
    return total



print(kInversePairs(10,0))