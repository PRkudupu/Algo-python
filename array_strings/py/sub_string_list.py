#!/usr/bin/env python
# coding: utf-8

# ### Check if a string is substring of another
# Given two strings s1 and s2, find if s1 is substring of s2. If yes, return true of first occurrence, else return false.
# 
# #### Examples :
# 
# #### Input : s1 = "sam", s2 = "I am sam"
# Output : True
# String "for" is present as a substring
# of s2.
# 
# #### Input : s1 = "prathap", s2 = "I am sam"
# Output : False.

# In[ ]:


def sub(s1,s2):
    if s1 in s2:
        return True
    else:
        return False
print(sub("sam","I am sam")) 
    


# In[13]:


def sub(s1,s2):
    if s2.find(s1) != -1:
        return True
    else:
        return False
print(sub("sam","I am sam"))


# In[25]:


def sub(s1,s2):
    sub_str=len(s1)
    main_str=len(s2)
    out_loop=main_str-sub_str+1
    
    for i in range(out_loop):
        for j in range(sub_str):
            if s2[i+j] != s1[j]:
                break;
            if j+1 == sub_str:
                return True
    return False
print(sub("sam","I am sam"))            


# In[ ]:





# In[ ]:




