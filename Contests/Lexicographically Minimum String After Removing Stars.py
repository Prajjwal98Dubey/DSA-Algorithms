
'''
"dk*adad*yy*"
"dk**"
'''

import collections
def clearStars(s):
    hash = {}
    for i in range(ord('a'),ord('z')+1):
        hash[chr(i)]=[]
    hashset = set()
    for i in range(len(s)):
        if s[i]=="*":
            for key in hash:
                if len(hash[key])!=0:
                    index = hash[key].pop()
                    hashset.add(index)
                    break
            continue
        hash[s[i]].append(i)
    ans = ""
    for i in range(len(s)):
        if i not in hashset and s[i]!="*":
            ans+=s[i]
    return ans
    


print(clearStars("dk*adad*yy*"))
'''
kddyy
'''