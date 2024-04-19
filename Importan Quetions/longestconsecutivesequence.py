'''
Consider each of the element as the start of the sequence if it is not then move to the other element and check the same.
'''
def longestConsecutive(nums):
    hash = set(nums)
    maxi = 0
    for n in nums:
        if not n-1 in hash:       #checking if n is the start of a sequence
            length = 0
            while n in hash:
                length+=1
                n+=1
            maxi = max(maxi,length)
    return maxi

print(longestConsecutive([0,3,7,2,5,8,4,6,0,1]))