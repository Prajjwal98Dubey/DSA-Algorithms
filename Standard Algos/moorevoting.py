
# In this solution the time Complexity is O(n) but the space Complexity is also O(n) due to the usage of dictionary so to solve this problem in O(1) space, we have to use Moore's Voting Algorithm.


# def majorityElement(nums):
#     dict={}
#     for i in nums:
#         if(i in dict):
#             dict[i]=dict[i]+1
#         else:
#             dict[i]=1
#     for i in dict:
#         if(dict[i]>(len(nums)//2)):
#             return i
#     return -1
#
# print(majorityElement([3,1,3,3,2]))
# Moore's Voting Algoithm:-
def majorityElement(nums):
    count=1
    majority_element=nums[0]
    for i in range(1,len(nums)):
        if(majority_element!=nums[i]):
            count=count-1
        else:
            count=count+1
        if(count==0):
            majority_element=nums[i]
            count=1
    counter=0
    for i in nums:
        if(majority_element==i):
            counter=counter+1
    if(counter > len(nums)//2):
        return majority_element
    else:
        return -1


print(majorityElement([3,1,3,3,2]))



# https://www.studocu.com/in/document/institute-of-management-and-research-pune/bachalor-of-engineering/oracle/68344123