# XOR represented by "^",if two things are same then 0 and if two things are different then 1.
# left shift "<<"  right shift ">>"
# in left shift we gain bits whereas in the right shift we are losing bits.

# tricks for bit manipulation:-
# do a bitwise & with the number and 1, if the result comes out to be 1 then the number is odd otherwise the number is even. for eg:- 9 & 1 = 1 -> odd


# swap two numbers without using the third variable using bit manipulation.
# it will be done with the help of XOR operation.

# x = 5 
# y = 7
# print("Before Swap:- " + "X: ", + x ,"Y: ",y)
# x= x^y
# y=x^y
# x=x^y
# print("After Swap:- " + "X: ", + x ,"Y: ",y)

# sum of the bit differences of all pairs in O(n) time complexity.
def sumOfBitsDifference(nums):
    sum = 0
    for i in range(32):
        cnt=0
        for n in nums:
            tmp = 1<<i
            if tmp & n !=0:
                cnt+=1
        sum+=2*cnt*(len(nums)-cnt)
    return sum
print(sumOfBitsDifference([1,3,5]))