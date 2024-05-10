# n = 3, meetings = [[1,20],[2,10],[3,5],[4,9],[6,8]]
import heapq
def mostBooked(n,meetings):
    rooms= [0] * n
    minHeap=[]
    meetings.sort(key=lambda x:(x[0],x[1]))
    for i in range(min(n,len(meetings))):
        start,end = meetings[i]
        rooms[i]+=1
        heapq.heappush(minHeap,[end,i])
    print(rooms)
    for i in range(min(n,len(meetings)),len(meetings)):
        start,end = meetings[i]
        e,r = heapq.heappop(minHeap)
        interval=[start,end]
        if e > start:
            delay= e-start
            interval[0] = e
            interval[1] = end + delay
        rooms[r]+=1
        heapq.heappush(minHeap,[interval[1],r])
    print(rooms)
    maxi = max(rooms)
    index  = rooms.index(maxi)
    return index
print(mostBooked(4,[[18,19],[3,12],[17,19],[2,13],[7,10]]))