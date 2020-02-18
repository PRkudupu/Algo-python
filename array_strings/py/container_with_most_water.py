#!/usr/bin/env python
# coding: utf-8

# ### Container with most water
# Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai). n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0). Find two lines, which together with x-axis forms a container, such that the container contains the most water.
# 
# Note: You may not slant the container and n is at least 2.
# 
# ![](image/containerWithMostWater.jpg)
#  
#  Example:
# 
# <b>Input: [1,8,6,2,5,4,8,3,7]</b><br>
# Output: 49

# <b>hint 1</b>The aim is to maximize the area formed between the vertical lines. The area of any container is calculated using the shorter line as length and the distance between the lines as the width of the rectangle.
# Area = length of shorter vertical line * distance between lines
# 
# We can definitely get the maximum width container as the outermost lines have the maximum distance between them. However, this container might not be the maximum in size as one of the vertical lines of this container could be really short.
# <b>hint 2</b>
# Start with the maximum width container and go to a shorter width container if there is a vertical line longer than the current containers shorter line. This way we are compromising on the width but we are looking forward to a longer length container.

# #### Solution
# 
# ![](image/area_cont.jpg)
# 
# We have to maximize the Area that can be formed between the vertical lines using the shorter line as length and the distance between the lines as the width of the rectangle forming the area.
# 
# Initially we consider the area constituting the exterior most lines. Now, to maximize the area, we need to consider the area between the lines of larger lengths. If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited by the shorter line. But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, despite the reduction in the width. This is done since a relatively longer line obtained by moving the shorter line's pointer might overcome the reduction in area caused by the width reduction.
# 
# <b>Complexity Analysis</b>
# 
# Time complexity : O(n)O(n). Single pass.
# 
# Space complexity : O(1)O(1). Constant space is used.

# In[3]:


def maxArea(height):
    L, R, width, res = 0, len(height) - 1, len(height) - 1, 0
    for w in range(width, 0, -1):
        if height[L] < height[R]:
            res, L = max(res, height[L] * w), L + 1
        else:
            res, R = max(res, height[R] * w), R - 1
    return res


# In[2]:


ls=[1,8,6,2,5,4,8,3,7]
print(maxArea(ls))

