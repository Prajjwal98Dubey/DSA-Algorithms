'''
concept -> 
'''
def singleNumber(nums):
    cummXOR = 0 
    for n in nums:
        cummXOR = cummXOR ^ n
    #find the right most set bit
    rms = cummXOR & -cummXOR
    x,y=0,0
    for n in nums:
        if x & rms == 0:
            x = x ^ n
        else:
            y = y ^ n
    return [x,y]

print(singleNumber([-1139700704,-1653765433]))