'''
Approach-> if we consider one of the freq as "x" then till "x+k" the condition will follow if the frequency becomes greater than x+k then we have to remove the extra frequecy and so on.
'''
import collections
def minimumDeletions(word,k):
    def check(curr,index):
        ops=0
        for i in range(len(freq)):
            if i!=index:
                if freq[i] < curr:
                    ops+=freq[i]
                if freq[i] > curr+k:
                    ops+=freq[i] - (curr+k)
        return ops
    hash = collections.defaultdict(int)
    for w in word:
        hash[w]+=1
    freq = []
    for val in hash.values():
        freq.append(val)
    freq.sort()
    mini = len(word)+1
    for i in range(len(freq)):
        mini = min(mini,check(freq[i],i))
    return mini


print(minimumDeletions("aabcaba",0))