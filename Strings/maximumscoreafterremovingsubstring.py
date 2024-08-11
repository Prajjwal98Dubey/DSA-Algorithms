'''
cdbcbbaaabab
'''
def maximumGain(s,x,y):
    stack =  []
    t="ab"
    z="ba"
    if y > x:
        t = "ba"
        z = "ab"
    hash = {}
    hash["ab"] = x
    hash["ba"] = y
    r = 0
    cnt=0
    while r < len(s):   #cdbcbbaaabab   x => 4 y => 5
        if stack and stack[-1]+s[r]==t:
            cnt+=hash[t]
            stack.pop()
        else:
            stack.append(s[r])
        r+=1
    newS = "".join(stack)
    r = 0
    stack = []
    while r < len(newS):   #cdbcbbaaabab   x => 4 y => 5
        if stack and stack[-1]+newS[r]==z:
            cnt+=hash[z]
            stack.pop()
        else:
            stack.append(newS[r])
        r+=1
    return cnt
print(maximumGain("aabbaaxybbaabb",5,4))


    
