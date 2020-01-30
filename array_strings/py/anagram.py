#!/usr/bin/env python
# coding: utf-8

# Given two strings s1 and s2, check if both the strings are anagrams of each other.

# <pre style="background-color: #e0e0e0;">Input : s1 = "listen"
#         s2 = "silent"
# Output : The strings are anagrams.
# 
# 
# Input : s1 = "dad"
#         s2 = "bad"
# Output : The strings aren't anagrams.
# </pre>

# In[2]:


def anagram(str1,str2):
    if sorted(str1) == sorted(str2):
        return True
    else:
        return False
print(anagram('ate','te'))


# In[ ]:




