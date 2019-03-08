#!/usr/bin/env python
# coding: utf-8

# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.
# 
# Example:
# 
# Input: [0,1,0,3,12]
# Output: [1,3,12,0,0]
# Note:
# 
# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

# In[34]:


ar =[0,0,4,7,0,10]
def move_zeros(nums):
    last0=0;
    #move the non zero numbers to the left
    for i in range(0,len(nums)):
        if(nums[i]!=0):
            nums[i],nums[last0]=nums[last0],nums[i]
            last0+=1
    return nums
move_zeros(ar)   


# In[1]:


def mov_zeros(ls):
    last0=0
    for i in range(0,len(ls)):
        print("loop",ls[i])
        if ls[i] !=0:
            print(ls[i])
            print(ls[last0])
            print("before",ls)
            ls[i],ls[last0]=ls[last0],ls[i]
            print("after",ls)
            last0 +=1
            print("last0",last0)
    return ls

print(mov_zeros([0,0,10,20]))


# In[ ]:




