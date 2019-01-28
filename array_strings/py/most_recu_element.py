#!/usr/bin/env python
# coding: utf-8

# Print the most recurring element in a list 
# 
# <b>Ex for the input : "sssaa" </b>
# 
# Expected output : <b>"s"</b>
# 

# In[3]:


#Store the max count in a varible
#when max count changes add the character to the dictionary
def n_repeat(s):
    dic   ={}
    m_max = 0 
    m_elem = ""
    for ch in s:
        if ch in dic.keys():
            continue
        else:
            if m_max < s.count(ch):
                m_max = s.count(ch)
                dic['max']=ch
    return dic['max']      
print(n_repeat("geekgeeks"))


# In[ ]:




