import collections
def openLock(deadends,target):
    if "0000" in deadends:
        return -1
    dead = set(deadends)
    visited = set()
    q = collections.deque()
    q.append(("0000",0))
    while q:
        lock,turns = q.popleft()
        if lock == target:
            return turns
        for i in range(4):
            clock = (int(lock[i]) + 1)%10
            anti = (int(lock[i])-1)
            if int(lock[i])==0:
                anti = 9
            newNodeClock = lock[:i] + str(clock) + lock[i+1:]
            newNodeAnti =  lock[:i] + str(anti) + lock[i+1:]
            if newNodeClock not in visited and newNodeClock not in dead:
                visited.add(newNodeClock)
                q.append((newNodeClock,turns+1))
            if newNodeAnti not in visited and newNodeAnti not in dead:
                visited.add(newNodeAnti)
                q.append((newNodeAnti,turns+1))
    return -1

print(openLock(["0201","0101","0102","1212","2002"],"0202"))
