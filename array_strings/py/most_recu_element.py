#!/usr/bin/env python
# coding: utf-8

# Print the most recurring element in a list 
# 
# <b>Ex for the input : "sssaa" </b>
# 
# Expected output : <b>"s"</b>
# 

# In[ ]:


def max_oc(s):
    dic = {}
    max_oc=0
    for i in range(len(s)):
        if s[i] in dic:
            continue
        else:
            count =s.count(s[i])
            dic[s[i]] =count
            if count > max_oc:
                max_oc=count
    return max_oc
print(max_oc("sssaa"))


# In[11]:


def max_oc(s):
    dic = {}
    max_oc=0
    for i in range(len(s)):
        print("dic",dic)
        if s[i] in dic:
            continue
        else:
            count =s.count(s[i])
            dic[s[i]] =count
            if count > max_oc:
                max_oc=count
                dic['max'] =s[i]
    return dic['max']
print(max_oc("sssaa"))

