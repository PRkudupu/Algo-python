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

# In[1]:


def n_repeat(s):
    dic ={}
    for ch in s:
        if ch in dic.keys():
            continue
        else:
            if s.count(ch) == 1:
                return ch
            else:
                dic[ch]=s.count(ch)
    return -1     
print(n_repeat("geekgeeks"))


# In[3]:


# In this example iteration is done
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
                    dic[s[i]]=s.count(s[i])
            
        return -1

print(firstUniqChar("saspa"))


# In[2]:


def f_dup(st):
    dic = {}
    for i in range(len(st)):
        print("st[i]",st[i])
        print("dic",dic)
        print("count",st.count(st[i]) )
        if st[i] in dic.keys():
            print("inside if")
            continue
        else:
            if st.count(st[i]) == 1:
                return i
            else:
                dic[st[i]]=st.count(st[i])
    return -1
print(f_dup("sapsa"))


# In[ ]:




