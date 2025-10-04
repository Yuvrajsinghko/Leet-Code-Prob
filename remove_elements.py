#Remove Element

"""
Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. The order of the elements may be changed. Then return the number of elements in nums which are not equal to val.

Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things:

Change the array nums such that the first k elements of nums contain the elements which are not equal to val. The remaining elements of nums are not important as well as the size of nums.
Return k.
"""


class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        nums_len = len(nums)
        filtered_list = nums
        while val in filtered_list:
            filtered_list.remove(val)
        k = len(filtered_list)

        for i in range(nums_len):
            if i < len(filtered_list):
                nums.append(filtered_list[i])
            else:
                nums.append('_')
        return k





