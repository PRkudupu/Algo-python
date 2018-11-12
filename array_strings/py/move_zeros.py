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


# In[2]:


# move
def move_zeros(nums):
    last0=0
    for i in range(0,len(nums)):
        if(nums[i]!=0):
            print("i",i)
            print("nums[i]",nums[i])
            print("nums[last0]",nums[last0])
            print("[last0]",last0)
            nums[i],nums[last0]=nums[last0],nums[i]
            print("after nums[i]",nums[i])
            print("after nums[last0]",nums[last0])
            print("nums",nums)
            last0+=1
    return nums
print(move_zeros([0,1,0,10]))


# In[ ]:




