import collections
def minimumWindow(s,t):
    if len(t) > len(s):
        return ""
    tHash= collections.defaultdict(int)
    tCount= len(t)
    for i in t:
        tHash[i]+=1
    l=0
    res=""
    resLen = len(s)+1
    sHash = collections.defaultdict(int)
    print(tHash)
    for r in range(len(s)):
        if s[r] in tHash:
            sHash[s[r]]+=1
        if sHash==tHash:
            i=r
            sCount=0
            while i>=l:
                if s[i] in tHash:
                    sCount+=1
                if sCount==tCount:
                    if resLen > r-i+1:
                        resLen=r-i+1
                        res=s[i:r+1]
                        break
                i-=1
            for key in sHash:
                sHash[key]=0
            l+=1
            r=l
    return res
print(minimumWindow('ADOBECODEBANC','ABC'))