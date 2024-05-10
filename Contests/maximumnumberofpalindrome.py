
# Approach ---> We only have to think about forming the palindromes irrespective of how the characeters will be placed to form the palindromes, which means we only have to think about the frequency of the each characters and do the required if the len of a word in even or if the length of the word is odd.
# observe the question write some testcases then we will able to solve this problem.


import collections
def maximumPalindromes(words):
    # create the frequency map
    freq = collections.defaultdict(int)
    for w in words:
        for i in w:
            freq[i]+=1
    # print(freq)
    # count number of even pairs and odd number of elements
    even=0
    odd=0
    for key in freq:
        even+=freq[key]//2
        odd+=1
    print(even,odd)
    # sort the words arrray in terms of len so that the smallest length of word get fills first.
    words.sort(key=lambda x:len(x))
    print(words)
    cnt=0
    for w in words:
        pairs = len(w)//2
        if len(w)%2==0 and even>=pairs:
            cnt+=1
            even-=pairs
        if len(w)%2!=0:
            if not odd:
                even-=1
                odd+=2
            if odd>=1 and even>=pairs:
                cnt+=1
                odd-=1
                even-=pairs
    return cnt

print(maximumPalindromes(["aagha","bc"]))



