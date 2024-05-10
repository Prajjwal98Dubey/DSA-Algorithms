import collections
def minimumDeletion(word,k):
    hash = collections.defaultdict(int)
    for w in word:
        hash[w]+=1
    res=[]
    for key in hash:
        res.append(hash[key])
    res.sort(reverse=True)
    cnt=0
    for i in range(len(res)):
        maxi = res[i]
        for j in range(i+1,len(res)):
            if res[i]-res[j] > k:
                tmp = (res[i]-res[j]) - k
                if res[j] > maxi:
                    cnt+=tmp
                    res[j]-=tmp
                else:
                    cnt+=tmp
                    res[i]-=tmp
    return cnt
print(minimumDeletion("aabcaba",0))