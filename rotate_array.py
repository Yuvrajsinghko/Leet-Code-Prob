"""
Rotate Array

Given an integer array nums, rotate the array to the right by k steps, where k is non-negative.
"""
n=int(input("Enter number of times to rotate:"))
li=[1,2,3,4,5,6,7]
for i in range(0,n):

    a=li.pop()
    li.insert(0,a)
print(li)