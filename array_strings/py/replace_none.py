#!/usr/bin/env python
# coding: utf-8

# Given an array containing None values fill in the None values <br>
#     with most recent non None value in the array<br>
#     For example:<br>
#     <b>- input array: </b>[1,None,2,3,None,None,5,None] <br>
#      <b> - output array: </b> [1,1,2,3,3,3,5,5]<br> 
#     Ensure you take care of case input[None] which means None object.<br>

# In[1]:


def repalce_none(ls):
    prev =0
    if len(ls) ==1 and ls[0]==None:
        return None
    for i in  range(len(ls)):
        if i > 0:
            prev=ls[i-1]
        if ls[i]== None:
            ls[i]=prev
    return ls

ls_1=[1,None,2,3,None,None,5,None]
ls_2=[None]
print(repalce_none(ls_1))


# In[ ]:




