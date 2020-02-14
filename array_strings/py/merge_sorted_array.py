#!/usr/bin/env python
# coding: utf-8

# #### Given two sorted integer arrays nums1 and nums2, merge nums2 into nums1 as one sorted array.
# 
# Note:
# <p>
# The number of elements initialized in nums1 and nums2 are m and n respectively.
# <br>Note:
#     You may assume that <i><b>nums1 has enough space (size that is greater or equal to m + n) to hold additional elements from nums2.</b></i>
# </p>
# Example:
# <br><br>
# <b>
# Input:
# nums1 = [1,2,3,0,0,0], m = 3 <br>
# nums2 = [2,5,6],       n = 3 </b>
# 
# Output: [1,2,2,3,5,6]

# #### Hint1
# 
# You can easily solve this problem if you simply think about two elements at a time rather than two arrays. We know that each of the individual arrays is sorted. What we don't know is how they will intertwine. Can we take a local decision and arrive at an optimal solution?
# 
# #### Hint2
# If you simply consider one element each at a time from the two arrays and make a decision and proceed accordingly, you will arrive at the optimal solution.

# #### Approach 1 : Merge and sort
# Intuition
# 
# The naive approach would be to merge both lists into one and then to sort. It's a simple solution with a pretty bad time complexity \mathcal{O}((n + m)\log(n + m))O((n+m)log(n+m)) because here one doesn't profit from the fact that both arrays are already sorted.
# <br><br>
# <b>Time complexity :</b> \mathcal{O}((n + m)\log(n + m))O((n+m)log(n+m)). <br>
# <b> Space complexity :</b> \mathcal{O}(1)O(1).
# 

# In[7]:


def merge_sorted_array(ls1,m,ls2,n):
    ls1[:]=sorted(ls1[:m] + ls2)
    return ls1
print(merge_sorted_array([1,2,3,0,0,0],3,[2,5,6],3))


# #### Approach 2 : Two pointers / Start from the beginning
# Intuition
# 
# Typically, one could achieve <i> \mathcal{O}(n + m)O(n+m) </i> time complexity in a sorted array(s) with the help of two pointers approach.
# 
# The straightforward implementation would be to set get pointer p1 in the beginning of nums1, p2 in the beginning of nums2, and push the smallest value in the output array at each step.
# 
# <b>Since nums1 is an array used for output, one has to keep first m elements of nums1 somewhere aside, that means \mathcal{O}(m)O(m) space complexity for this approach.</b>
# 
# ![](image/merge_sorted.jpg)
# 

# In[11]:


# solution without print
def merge_sorted_array(ls1,m,ls2,n):
    # Make a copy of ls1.
    ls1_copy = ls1[:m] 
    ls1[:] = []
    
    # Two get pointers for ls1_copy and ls2.
    p1 = 0 
    p2 = 0
       
    # Compare elements from ls1_copy and ls2
    # and add the smallest one into ls1.
    while p1 < m and p2 < n: 
        if ls1_copy[p1] < ls2[p2]: 
            ls1.append(ls1_copy[p1])
            p1 += 1
        else:
            ls1.append(ls2[p2])
            p2 += 1
    # if there are still elements to add
    if p1 < m: 
        ls1[p1 + p2:] = ls1_copy[p1:]
    if p2 < n:
        ls1[p1 + p2:] = ls2[p2:]
    return ls1
    print(merge_sorted_array([1,2,3,0,0,0],3,[2,5,6],3))


# In[12]:


#solution with print
def merge_sorted_array(ls1,m,ls2,n):
    # Make a copy of ls1.
    ls1_copy = ls1[:m] 
    ls1[:] = []
    
    # Two get pointers for ls1_copy and ls2.
    p1 = 0 
    p2 = 0
    print('m,n',m,n)
    print('ls1_copy',ls1_copy)
       
    # Compare elements from ls1_copy and ls2
    # and add the smallest one into ls1.
    while p1 < m and p2 < n: 
        print('\np1, p2',p1,p2)
        print('ls1_copy[p1]',ls1_copy[p1])
        print('ls2[p2]',ls2[p2])
        if ls1_copy[p1] < ls2[p2]: 
            print('increement p1')
            ls1.append(ls1_copy[p1])
            p1 += 1
        else:
            print('increement p2')
            ls1.append(ls2[p2])
            p2 += 1
        print('ls1',ls1)
    # if there are still elements to add
    print("\np1,p2",p1,p2)
    print('ls1[p1 + p2:]',ls1[p1 + p2:])
    print('ls1_copy[p1:]',ls1_copy[p1:])
    print('ls2[p2:]',ls2[p2:])
    if p1 < m: 
        print("pointer 1 is greater than m.")
        ls1[p1 + p2:] = ls1_copy[p1:]
    if p2 < n:
        print("pointer2 is greater than n.")
        ls1[p1 + p2:] = ls2[p2:]
    return ls1
print(merge_sorted_array([1,2,3,0,0,0],3,[2,5,6],3))

#nums1[:] = sorted(nums1[:m] + nums2)
                
                


# In[8]:


# Solution with print
def merge_sorted_array(ls1,m,ls2,n):
    # Make a copy of ls1.
    ls1_copy = ls1[:m] 
    ls1[:] = []
    
    # Two get pointers for ls1_copy and ls2.
    p1 = 0 
    p2 = 0
    print('m,n',m,n)
    print('ls1_copy',ls1_copy)
       
    # Compare elements from ls1_copy and ls2
    # and add the smallest one into ls1.
    while p1 < m and p2 < n: 
        print('\np1, p2',p1,p2)
        print('ls1_copy[p1]',ls1_copy[p1])
        print('ls2[p2]',ls2[p2])
        if ls1_copy[p1] < ls2[p2]: 
            print('increement p1')
            ls1.append(ls1_copy[p1])
            p1 += 1
        else:
            print('increement p2')
            ls1.append(ls2[p2])
            p2 += 1
        print('ls1',ls1)
    # if there are still elements to add
    print("\np1,p2",p1,p2)
    print('ls1[p1 + p2:]',ls1[p1 + p2:])
    print('ls1_copy[p1:]',ls1_copy[p1:])
    print('ls2[p2:]',ls2[p2:])
    if p1 < m: 
        print("pointer 1 is greater than m.")
        ls1[p1 + p2:] = ls1_copy[p1:]
    if p2 < n:
        print("pointer2 is greater than n.")
        ls1[p1 + p2:] = ls2[p2:]
    return ls1
print(merge_sorted_array([1,2,3,0,0,0],3,[2,5,6],3))

#nums1[:] = sorted(nums1[:m] + nums2)
                
                


# In[5]:


#brute force solution. 1st solution 
def merge_sorted_array(ls1,m,ls2,n):
    i=0
    for j in range(n) :
        ls1[j+m]=ls2[j]
        i+=1
    return sorted(ls1)
print(merge_sorted_array([1,2,3,0,0,0],3,[2,5,6],3))


# In[6]:


#brute force solution. 1st solution with print
def merge_sorted_array(ls1,m,ls2,n):
    i=0
    for j in range(n) :
        print('\nj',j)
        print('ls2[j]',ls2[j])
        print(ls1[j+m])
        ls1[j+m]=ls2[j]
        i+=1
    return sorted(ls1)
print(merge_sorted_array([1,2,3,0,0,0],3,[2,5,6],3))


# In[ ]:




