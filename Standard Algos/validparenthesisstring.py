#LC 678
def checkValidString(s):
    hash  = {
        '(':')'
    }
    cnt = 0
    stack = []
    for i in range(len(s)):
        if s[i]=="(":
            stack.append(s[i])
