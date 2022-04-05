#!/usr/bin/env python
# coding: utf-8

# Given an array containing None values fill in the None values <br>
#     with most recent non None value in the array<br>
#     For example:<br>
#     <b>- input array: </b>[1,None,2,3,None,None,5,None] <br>
#      <b> - output array: </b> [1,1,2,3,3,3,5,5]<br> 
#     Ensure you take care of case input[None] which means None object.<br>

# In[43]:


def replace_none(ls):
    prev = None
    # if input parameter is none return none
    if ls is None:
        return None
    #If array is empty return None
    if not ls:
        return []
    for i in range(len(ls)):
        if ls[0] is None:
            ls[0] = None
        #condition is true when ch is not none
        if ls[i]:
            prev = ls[i]
        #condition is true when ch is none
        else:
            ls[i] = prev
    return ls


# In[44]:


assert replace_none(None) == None
assert replace_none([]) == []
assert replace_none([None,8,None]) == [None,8,8]
assert replace_none([1,None,2]) == [1,1,2]
assert replace_none([5,None,None]) == [5,5,5]
assert replace_none([1,None,2,3,None,None,5,None]) == [1,1,2,3,3,3,5,5]


# In[ ]:




