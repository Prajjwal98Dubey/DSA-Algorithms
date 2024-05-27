import collections
def sumOfDigitDifference(nums):
    hash = collections.defaultdict(list)
    for n in nums:
        index=0
        while n:
            v = n%10
            hash[index].append(v)
            n = n//10
            index+=1
    total = 0
    for key in hash:
        vals = hash[key]
        mp = collections.defaultdict(int)
        for v in vals:
            mp[v]+=1
        for k in mp:
            count = mp[k]
            '''
            [4,3,2,2]
            {4:1,3:1,2:2}
            '''
            total+= count*(len(vals) - count)   #important line of code to understand.
    return total//2

print(sumOfDigitDifference([13,24,12,22]))
            