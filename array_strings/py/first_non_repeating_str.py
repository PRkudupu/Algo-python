#!/usr/bin/env python
# coding: utf-8

# #### Given a string, find the first non-repeating character in it and return it's index. If it doesn't exist, return -1.
# 
# Examples:
# 
# s = "leetcode"
# 
# <b>return 0.</b>
# 
# s = "loveleetcode",
# 
# <b>return 2.</b>
# 

# In[ ]:


def firstUniqChar(s):
        """
        :type s: str
        :rtype: int
        """
        dic ={}
        for i in range(len(s)):
            if s[i] in dic.keys():
                continue
            else:
                if s.count(s[i]) == 1:
                    return i
                else:
                    dic[s[i]]=s[i].count(s[i])
            
        return -1

print(firstUniqChar("saspa"))

