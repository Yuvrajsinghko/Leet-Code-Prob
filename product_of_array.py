"""
Product of Array Except Self

Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

You must write an algorithm that runs in O(n) time and without using the division operation.
"""
import math

nums = [1,2,3,4]
final_ans=[]
ch=1
n=len(nums)
for i in range(n):
    for j in range(i+1,n):
        ch*=nums[j]
        final_ans.append(ch)

print(final_ans)



