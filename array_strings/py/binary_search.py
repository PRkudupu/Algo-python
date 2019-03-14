#!/usr/bin/env python
# coding: utf-8

# Given a sorted (in ascending order) integer array nums of n elements and a target value, write a function to search target in nums. If target exists, then return its index, otherwise return -1.
# 
# 
# Example 1:
# 
# <b>Input: nums = [-1,0,3,5,9,12], target = 9</b>
# 
# Output: 4
# 
# Explanation: 9 exists in nums and its index is 4
# 
# Example 2:
# 
# <b>Input: nums = [-1,0,3,5,9,12], target = 2</b>
# 
# Output: -1
# 
# Explanation: 2 does not exist in nums so return -1
#  

# In[2]:


def search(nums, target):
    l, r = 0, len(nums) - 1
    while l <= r:
        mid = (l + r) // 2
        if nums[mid] < target:
            l = mid + 1
        elif nums[mid] > target:
            r = mid - 1
        else:
            return mid
    return -1
print(search([3,4,5,6],5))


# In[ ]:




