#"abBAcC"
#contains lot of testcases be carefull.

def makeGood(s):
    if not s:
            return ""
    i=0
    while i<len(s):
        if 33<=ord(s[i])<97:
            if i-1 >=0 and ord(s[i-1])!=ord(s[i]):
                i1 = s[i-1].upper()
                if i1==s[i]:
                    s=s[:i-1]+s[i+1:]
                    i=0
                    continue
            if i+1 < len(s) and ord(s[i+1])!=ord(s[i]):
                i1 = s[i+1].upper()
                if i1==s[i]:
                    s=s[:i] + s[i+2:]
                    i=0
                    continue
            i+=1
        else:
            i+=1
    return s

print(makeGood(""))

