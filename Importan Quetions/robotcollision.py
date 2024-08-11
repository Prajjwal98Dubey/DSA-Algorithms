def survivedRobotsHealth(positions,health,directions):
    hash ={} 
    for pos in positions:
        hash[pos] = -1
    combine = []
    for i in range(len(positions)):
        combine.append([positions[i],health[i],directions[i]])   #[2, 15, 'R'], [3, 10, 'R'], [5, 10, 'L'], [6, 12, 'L']]
    combine.sort(key=lambda x:x[0])
    stack = []
    r =  0
    while r < len(combine):    # [1,10,"R"] , [40,11,"L"]
        if not stack or (stack and stack[-1][1]==combine[r][2]):
            stack.append([combine[r][1],combine[r][2],combine[r][0]])
            r+=1
            continue
        if stack and stack[-1][1]=="L" and stack[-1][1] != combine[r][2] and stack[-1][2] < combine[r][0]:
            stack.append([combine[r][1],combine[r][2],combine[r][0]])
            r+=1
            continue
        if stack and stack[-1][1]=="R" and stack[-1][1] != combine[r][2] and stack[-1][2] > combine[r][0]:
            stack.append([combine[r][1],combine[r][2],combine[r][0]])
            r+=1
            continue
        else:
            if stack[-1][0] == combine[r][1]:
                stack.pop()
                r+=1
                continue
            if stack[-1][0] > combine[r][1]:
                tmp = stack.pop()
                tmp[0]-=1
                stack.append(tmp)
                r+=1
                continue
            power = combine[r][1]
            while stack and stack[-1][0] < power and ((stack and stack[-1][1]=="L" and stack[-1][1] != combine[r][2] and stack[-1][2] > combine[r][0]) or (stack and stack[-1][1]=="R" and stack[-1][1] != combine[r][2] and stack[-1][2] < combine[r][0])):
                stack.pop()
                power-=1
            if stack and power and ((stack and stack[-1][1]=="L" and stack[-1][1] != combine[r][2] and stack[-1][2] > combine[r][0]) or (stack and stack[-1][1]=="R" and stack[-1][1] != combine[r][2] and stack[-1][2] < combine[r][0])):
                if stack[-1][0] > power:
                    stack[-1][0]-=1
                    r+=1
                    continue
                if stack[-1][0] == power:
                    stack.pop()
                    r+=1
                    continue
            else:
                if power:
                    stack.append([power,combine[r][2],combine[r][0]])
                    r+=1
                    continue  

    for h,_,p in stack:     #[17,1,"L"] [18,30,"R"] [24,39,"L"]
        hash[p] = h
    ans =[]
    for key in hash:
        if hash[key]!=-1:
            ans.append(hash[key])
    return ans
print(survivedRobotsHealth([3,5,2,6],[10,10,15,12],"RLRL"))
print(survivedRobotsHealth([1,2,5,6],[10,10,11,11],"RLRL"))
print(survivedRobotsHealth( [5,4,3,2,1],[2,17,9,15,10],"RRRRR"))
print(survivedRobotsHealth([1,40],[10,11],"RL"))
print(survivedRobotsHealth([3,47],[46,26],"LR"))
# print(survivedRobotsHealth([47,3],[46,26],"RL"))
print(survivedRobotsHealth([17,24,18],[1,39,30],"LLR"))
print(survivedRobotsHealth([34,50,42,2],[6,27,17,38],"LLRR"))




'''
[2,38,R] [34,6,L] [42,17,R] [50,27,L]

[2,37,R] [50,26,L]






'''