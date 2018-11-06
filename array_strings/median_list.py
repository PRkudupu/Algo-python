#!/usr/bin/env python
# coding: utf-8

# ### Find the median for an odd set of numbers
# Sample question: Find the median for the following data set:
# 102, 56, 34, 99, 89, 101, 10.
# 
# Step 1: Place the data in ascending order. In other words, sort your data from the smallest number to the highest number. For this sample data set, the order is:
# 10, 34, 56, 89, 99, 101, 102.
# 
# Step 2: Find the number in the middle (where there are an equal number of data points above and below the number):
# 10, 34, 56, <b>89</b>, 99, 101, 102.
# <b>The median is 89.</b>
# 
# Tip: If you have a large data set, divide the number in the set by two. That tells you how many numbers should be above and how many numbers should be below. 
# For example, <b>101/2 = 55.5.</b> Ignore the decimal: 55 numbers should be above and 55 below.
# 
# ### Find the median for an even set of numbers
# Sample question: Find the median for the following data set:
# 102, 56, 34, 99, 89, 101, 10, 54.
# 
# Step 1: Place the data in ascending order (smallest to highest).
# 10, 34, 54, 56, 89, 99, 101, 102.
# 
# Step 2: Find the TWO numbers in the middle (where there are an equal number of data points above and below the two middle numbers).
# 10, 34, 54, 56, 89, 99, 101, 102
# 
# Step 3: Add the two middle numbers and then divide by two, to get the average:
# <b>56 + 89 = 145 </b>
# 145 / 2 = 72.5.
# The median is 72.5.
# Tip: For large data sets, divide the number of items by 2, then subtract 1 to find the number that should be above and the number that should be below. 
# <b>For example, 100/2 = 50. 50 – 1 = 49.</b> The middle two numbers will have 49 

# In[11]:


def med(nums):
    ls=sorted(nums)
    l=len(nums)
    mid=int((l-1)/2)
    mid_plus_one=int((l+1)/2)
    if l % 2 == 0:
        return int((ls[mid] + ls[mid_plus_one])/2)
    else:
        return ls[mid]

print(med([1,2,3,4,5]))


# ### Using in built library

# In[12]:


def med(nums):
    import statistics
    return statistics.median(nums)
print(med([1,2,3,4,5]))

