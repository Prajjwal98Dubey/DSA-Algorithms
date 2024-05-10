# Approach:- As the identical character will be only added after the cooldown period so we have to process the most frequent character first,if we dont do this then at the last all the frequent character will be selected with the idle time and the total time will increase and the other hand we have to minimize the time(interval) of the tasks.
# will be using max heap and queue for solving this question
import heapq,collections
def leastInterval(tasks,n):
    hash=collections.defaultdict(int)
    for task in tasks:
        hash[task]+=1
    maxHeap=[]
    for key in hash:
        heapq.heappush(maxHeap,-1*hash[key])
    queue = collections.deque()
    time=0
    while maxHeap or queue:
        time+=1
        if maxHeap:
            task = 1 + heapq.heappop(maxHeap)
            if task:
                queue.append([task,time+n])
        if queue and queue[0][1] == time:
            heapq.heappush(maxHeap,queue.popleft()[0])
    return time

print(leastInterval(["A","A","A","B","B","B"],2))