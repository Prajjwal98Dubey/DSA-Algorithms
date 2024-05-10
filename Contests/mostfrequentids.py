#brute force  --> this will give TLE.
'''
import heapq
def mostFrequentIds(nums,freq):
    maxHeap = []
    seen = set()
    ans = [0]*len(nums)
    for i in range(len(nums)):
        if nums[i] not in seen:
            heapq.heappush(maxHeap,[-1*freq[i],-1*nums[i]])
            seen.add(nums[i])
            ans[i] = -maxHeap[0][0]
        else:
            popped = []
            while maxHeap:
                f,v = heapq.heappop(maxHeap)
                if -v == nums[i]:
                    newF = -f + freq[i]
                    if newF == 0:
                        seen.remove(-v)
                    if newF:
                        popped.append([-1*newF,v])
                    break
                popped.append([f,v])
            for f,v in popped:
                heapq.heappush(maxHeap,[f,v])
            if maxHeap:
                ans[i] = -maxHeap[0][0]
    return ans
                
'''

'''
 nums = [5,5,3], freq = [2,-2,1]
'''
import heapq,collections
def mostFrequentIds(nums,freq):
    hash = collections.defaultdict(int)
    maxHeap = []
    ans = []
    for i in range(len(nums)):
        hash[nums[i]]+=freq[i]
        heapq.heappush(maxHeap,[-hash[nums[i]],-nums[i]])
        if (hash[-maxHeap[0][1]]==-maxHeap[0][0]):
            ans.append(-maxHeap[0][0])
        else:
            while maxHeap:
                if (hash[-maxHeap[0][1]]!=-maxHeap[0][0]):
                    heapq.heappop(maxHeap)
                else:
                    ans.append(-maxHeap[0][0])
                    break
    return ans
print(mostFrequentIds([2,5,1,5,4,5,9,1,8],[3,1,2,-1,2,5,1,-1,3]))

