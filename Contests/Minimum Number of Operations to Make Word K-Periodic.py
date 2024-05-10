import collections
def minimumOperations(word,k):
    hash = collections.defaultdict(int)
    i=0
    while i<len(word)-k+1:
        s = word[i:i+k]
        hash[s]+=1
        i+=k
    maxi,s = -1,""
    for key in hash:
        if maxi < hash[key]:
            maxi = hash[key]
            s=key
    print(s,maxi)
    cnt = 0
    for key in hash:
        if key != s:
            cnt+=hash[key]*k
    return cnt//k
    

print(minimumOperations("leetcoleet",4))
    