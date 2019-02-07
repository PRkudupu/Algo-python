#!/usr/bin/env python
# coding: utf-8

# Given two arrays, write a function to compute their intersection.
# 
# Example 1:
# 
# Input: nums1 = [1,2,2,1], nums2 = [2,2]
# Output: [2]
# Example 2:
# 
# Input: nums1 = [4,9,5], nums2 = [9,4,9,8,4]
# Output: [9,4]

# In[1]:


def intersection(nums1, nums2):
    return list(set(nums1) & set(nums2))
print(intersection([4,9,5],[9,4,9,8,4]))


# In[2]:


def intersection(nums1, nums2):
    stack =[]
    for i in nums1:
        if i not in stack and i in nums2:
            stack.append(i)
    return stack
print(intersection([4,9,5],[9,4,9,8,4]))


# In[ ]:




