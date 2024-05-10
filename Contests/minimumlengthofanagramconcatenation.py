'''
only the factors of the length of s can make an anagram.
'''
import collections
def minAnagramLength(s):
    def isAnagram(index):
        t =  s[:index] 
        print(t)
        hash = collections.defaultdict(int)
        for i in range(len(t)):
            hash[t[i]]+=1
        i = index
        while i < len(s):
            tmp = collections.defaultdict(int)
            j = i
            while j < len(t) + i:
                tmp[s[j]]+=1
                j+=1
            print(tmp)
            if tmp!=hash:
                return False
            i+=index
        return True
    for i in range(len(s)+1):
        if i == 0:
            continue
        if len(s)%i == 0 and isAnagram(i):
            return i
        

print(minAnagramLength("cdef"))