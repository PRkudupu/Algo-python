#!/usr/bin/env python
# coding: utf-8

# Given a non-empty string s, you may delete at most one character. Judge whether you can make it a palindrome.
# 
# #### Example 1:
# Input: "aba"
# Output: True
# 
# #### Example 2:
# Input: "abca"
# Output: True
# Explanation: You could delete the character 'c'.
# 
# [1:5] is equivalent to "from 1 to 5" (5 not included)
# 
# [1:] is equivalent to "1 to end"
# 
# [len(a):] is equivalent to "from length of a to end"

# In[14]:


def validPalindrome(s):
    for i in range(len(s)):
        t = s[:i] + s[i+1:]
        if t == t[::-1]: return True
    return s == s[::-1]
print(validPalindrome("acba")) 


# In[12]:


def validPalindrome(s):
    for i in range(len(s)):
        print("s[:i]",s[:i])
        print("s[i+1:]",s[i+1:])
        t = s[:i] + s[i+1:]
        print("t",t)
        print("t[::-1]",t[::-1])
        if t == t[::-1]: 
            print("inside if")
            return True
    print("outside if")
    return s == s[::-1]
print(validPalindrome("acba"))        


# In[ ]:




