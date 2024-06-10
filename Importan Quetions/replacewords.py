import collections
def replaceWords(dictionary,sentence):
    hash = collections.defaultdict(list)
    dictionary.sort(key=lambda x:len(x))
    for d in dictionary:
        s=""
        for i in range(len(d)):
            s+=d[i]
            hash[s].append(d)
    index = 0
    i = 0
    # "abnormal"
    def check(word):
        s=""
        res = word
        for i in range(len(word)):
            s+=word[i]
            if s in hash and len(hash[s][0]) < len(word):
                res=hash[s][0]
        if res==word:
            return word
        t = ""
        for i in range(len(res)):
            t+=res[i]
            if t in hash and t in dictionary:
                return t
        ret
        
    while i<len(sentence):
        if sentence[i]==" ":
            tmp = sentence[index:i]
            if sentence[index] in hash:
                s = check(sentence[index:i])
                sentence = sentence[:index] + s + sentence[i:]
                i=i+1-(len(tmp)-len(s))
                index = i
            else:
                i+=1
                index = i
            continue
        i+=1
    
    if sentence[index] in hash:
        s = check(sentence[index:])
        sentence = sentence[:index] + s
    return sentence

# print(replaceWords(["ac","ab","a"],"it is abnormal that this solution is accepted"))
print(replaceWords(["cat","bat","rat"],"the cattle was rattled by the battery"))


#["ac","ab"] "it is abnormal that this solution is accepted"