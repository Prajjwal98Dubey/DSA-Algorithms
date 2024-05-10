# "aabbbbbbbbbbbbba"
def minimumOperationToRemoveBothEnds(s):
    l,r = 0,len(s)-1
    while l<r:
        if s[l] == s[r]:
            simi = s[l]
            while s[l]==simi:
                if l+1<r:
                    l+=1
                else:
                    break
            while s[r]==simi:
                if r+1>l:
                    r-=1
                else:
                    break
        else:
            break
    return r-l+1

print(minimumOperationToRemoveBothEnds("a"))





