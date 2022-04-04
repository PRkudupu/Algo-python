#!/usr/bin/env python
# coding: utf-8

# <p>Given a dictionary, print the key for nth highest value present in the dict. <br><br></p>
#  <b>   dic ={'a':242,'b':10,'c':500} 
#   k= 2
# <br>
#  RETURN VALUE <br>
#      op = 242

# In[23]:


def nth_highest(dic,k):
    dic ={'a':242,'b':10,'c':500} 
    return sorted(dic.values())[-k]

dic=dic ={'a':242,'b':10,'c':500} 
print(nth_highest(dic,2))


# Given a dictionary, print the key for nth highest value present in the dict. <br><br>
#  <b>   dic ={'a':242,'b':10,'c':500} 
#   k= 2
# <br>
#     op = a <br>
#  RETURN KEY

# In[25]:


# return Keys not values. In the above example we are returning keys
def nth_highest(dic,k):
    kth_value=sorted(dic.values())[-k]
    for k,v in dic.items():
        if v==kth_value:
            return k
dic=dic ={'a':242,'b':10,'c':500} 
print(nth_highest(dic,1))


# Given a dictionary, print the key for nth highest value present in the dict. If there are <b>more than 1 </b>record present for nth highest value then sort the key and print the first one.<br><br>
#  <b>   {'a':500,'b':10,'c':500,'d':500}
#   k= 1
# <br>
#      op = a <br>
#  RETURN KEY

# In[29]:


def nth_highest(dic,k):
    kth_value=sorted(dic.values())[-k]
    for k,v in dic.items():
        if v==kth_value:
            return k
dic=dic ={'a':500,'b':10,'c':500,'d':500} 
print(nth_highest(dic,1))

