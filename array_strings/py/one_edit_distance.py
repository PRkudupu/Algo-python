#!/usr/bin/env python
# coding: utf-8

# #### Given two strings s and t, determine if they are both one edit distance apart.
# 
# Note: 
# 
# There are 3 possiblities to satisify one edit distance apart:
# 
# Insert a character into s to get t
# Delete a character from s to get t
# Replace a character of s to get t
# Example 1:
# <code>
# <b>Input: s = "ab", t = "acb"
# Output: true</b>
# Explanation: We can insert 'c' into s to get t.
# Example 2:
# </code>
# 
# <code>
# <b>Input: s = "cab", t = "ad"
# Output: false</b>
# Explanation: We cannot get t from s by only one step.
# Example 3:
# </code>
# 
# <code>
# <b>Input: s = "1203", t = "1213"
# Output: true</b>
# Explanation: We can replace '0' with '1' to get t.
# </code>

# #### Approach 1: One pass algorithm
# Intuition
# 
# First of all, let's ensure that the string lengths are not too far from each other. If the length difference is 2 or more characters, then s and t couldn't be one edit away strings.
# 
# ![](image/OneEditDistance.jpg)
# 
# For the next let's assume that s is always shorter or the same length as t. If not, one could always call isOneEditDistance(t, s) to inverse the string order.
# 
# Now it's time to pass along the strings and to look for the first different character.
# 
# If there is no differences between the first len(s) characters, only two situations are possible :
# 
# <i>1)The strings are equal.
# 
# 2)The strings are one edit away distance.</i>
# 
# 
# 
# Now what if there is a different character so that s[i] != t[i].
# 
# If the strings are of the same length, all next characters should be equal to keep one edit away distance. To verify it, one has to compare the substrings of s and t both starting from the i + 1th character.
# 
# If t is one character longer than s, the additional character t[i] should be the only difference between both strings. To verify it, one has to compare a substring of s starting from the ith character and a substring of t starting from the i + 1th character.

# In[3]:


def one_edit_distance(ls,t):
    ns, nt = len(ls), len(t)
    if ns > nt:
        return False
    if nt - ns > 1:
        return False

    for i in range(ns):
        if ls[i] != t[i]:
            if ns == nt:
                return ls[i + 1:] == t[i + 1:]
            else:
                return ls[i:] == t[i + 1:]
    return ns + 1 == nt

print(one_edit_distance('abc','abhh'))
print(one_edit_distance('ab','acb'))
print(one_edit_distance('cab','ad'))
print(one_edit_distance('1203','1213'))


# In[1]:


#olution with print and commit
def one_edit_distance(ls,t):
    ns, nt = len(ls), len(t)
    print('ns',ns)
    print('nt',nt)
 
    # Ensure that s is shorter than t.
    if ns > nt:
        return False
    
    # The strings are NOT one edit away distance  
    # if the length diff is more than 1.
    if nt - ns > 1:
        return False

    for i in range(ns):
        print('\nls[i]',ls[i])
        print('t[i]',t[i])
        print('ls[i:]',ls[i:] )
        if ls[i] != t[i]:
            # if strings have the same length
            if ns == nt:
                return ls[i + 1:] == t[i + 1:]
            # if strings have different lengths
            else:
                return ls[i:] == t[i + 1:]
        print('ls[i + 1:]',ls[i + 1:])
        print('t[i + 1:]',t[i + 1:])
        

    # If there is no diffs on ns distance
    # the strings are one edit away only if
    # t has one more character. 
    return ns + 1 == nt

print(one_edit_distance('abc','abhh'))


# In[ ]:




