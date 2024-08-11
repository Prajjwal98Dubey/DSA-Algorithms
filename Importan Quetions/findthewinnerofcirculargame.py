
'''
[1,2,3,4,5]   k=2
'''

def findTheWinner(n,k):
    nums = [i for i in range(1,n+1)]
    r = 0
    hash = set()
    while len(hash)!=n-1:
        index = 0
        while index < k-1:
            r+=1
            if r == len(nums):
                r = 0
            if r not in hash:
                index+=1
        hash.add(r)
        r+=1
        if r == len(nums):
            r= 0
        while r in hash:
            r+=1
            if r == len(nums):
                r=0
    return nums[r]


print(findTheWinner(6,5))
        
