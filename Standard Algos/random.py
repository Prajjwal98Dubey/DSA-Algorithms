def countMatchingSubarrays(nums,pattern):
        if len(nums) < len(pattern):
            return 0
    
        count = 0
        
        for r in range(len(nums) - len(pattern) + 1):
            flag = True
            for k in range(len(pattern)):
                if pattern[k] == 0:
                    if nums[r+k] != nums[r]:
                        flag = False
                        break
                elif pattern[k] == 1:
                    if nums[r+k] <= nums[r+k-1]:
                        flag = False
                        break
                elif pattern[k] == -1:
                    if nums[r+k] >= nums[r+k-1]:
                        flag = False
                        break
            if flag:
                count += 1
        
        return count

print(countMatchingSubarrays([1,2,3,4,5,6],[1,1]))



# sub=[]
#         # [1,4,4,1,3,5,5,3]
#         n = len(nums)
#         # Generate all possible subarrays
#         for i in range(n):
#             for j in range(i, n):
#                 subarray = nums[i:j + 1]
#                 sub.append(subarray)
#         count=0
#         print(sub)
#         for s in sub:
#             if len(s) == len(pattern)+1:
#                 index=1
#                 flag=1
#                 for k in range(len(pattern)):
#                     if pattern[k]==0:
#                         if s[index-1]!=s[index]:
#                             flag=0
#                             break
#                         else:
#                             index+=1
#                     if pattern[k]==1:
#                         if s[index-1]>=s[index]:
#                             flag=0
#                             break
#                         else:
#                             index+=1
#                     if pattern[k]==-1:
#                         if s[index-1]<=s[index]:
#                             flag=0
#                             break
#                         else:
#                             index+=1
#                 if flag:
#                     count+=1
#         return count

