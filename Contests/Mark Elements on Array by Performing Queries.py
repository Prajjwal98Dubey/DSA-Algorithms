import heapq
# this code will give TLE
# def unmarkedElement(nums,queries):
#     hash = set()
#     ele=  []
#     minHeap=[]
#     ans=[]
#     totalSum = sum(nums)
#     for i in range(len(nums)):
#         heapq.heappush(minHeap,[nums[i],i])
#     for q in queries:
#         index,k = q
#         if index not in hash:
#             hash.add(index)
#             ele.append(nums[index])
#         while k>0 and minHeap:
#                 val,i = heapq.heappop(minHeap)
#                 if i not in hash:
#                     hash.add(i)
#                     ele.append(val)
#                     k-=1
#         ans.append(totalSum - sum(ele))
#     return ans

# instead of using a set for marked indices here i am converting the nums element into 0 if they are marked to avoid extra space of a set.

def unmarkedElement(nums,queries):
    totalSum=0
    minHeap = []
    for i in range(len(nums)):
        totalSum+=nums[i]
        heapq.heappush(minHeap,[nums[i],i])
    ans=[]
    for q in queries:
        index,k = q
        totalSum-=nums[index]
        nums[index]=0
        while minHeap and k:
            val,i = heapq.heappop(minHeap)
            if nums[i]:
                totalSum-=nums[i]
                nums[i]=0
                k-=1
        ans.append(totalSum)
    return ans
print(unmarkedElement([1,12,12,4,14,1,12,1],[[1,2],[5,4],[4,0],[0,1],[0,3]]))