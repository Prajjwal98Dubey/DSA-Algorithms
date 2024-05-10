# next try to think in terms of graphs.
# [[0,2,1],[1,3,1],[4,5,1]]
import collections
def findAllPeople(n,meetings,firstPerson):
    meetings.sort(key=lambda x:x[2])
    

print(findAllPeople(5,[[3,4,2],[1,2,1],[2,3,1]],1))

