# LC 3223

#"abaacbcbb"
import collections
def minimumLength(s):
    hash = collections.defaultdict(int)
    for c in s:
        hash[c]+=1
    minLength = len(s)
    for key in hash:
        while hash[key] > 2:
            hash[key]-=2
            minLength-=2
    return minLength
