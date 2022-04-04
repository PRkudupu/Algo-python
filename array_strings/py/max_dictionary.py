#!/usr/bin/env python
# coding: utf-8

# Given an dictionary find the max value in a dictionary. Return the key with the max value<br><br>
#  <b>dic ={'a':1,'b':3,'c':2} 
#  
# op=b

# In[4]:


def max_dic(dic):
    return max(dic,key=dic.get)
dic ={'a':1,'b':3,'c':2} 
print(max_dic(dic))


# In[ ]:




