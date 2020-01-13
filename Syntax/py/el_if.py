#!/usr/bin/env python
# coding: utf-8

# In[3]:


def if_else(val):
    if val == "1":
        print("one")
    else:
        if val == "2":
            print("two")
        else:
            print("three")
print(if_else("4"))
    


# In[4]:


def el_if(val):
    if val == "1":
        print("one")
    #Eliminatest the need for nested else
    elif val == "2":
        print("two")
    else:
        print("three")
print(el_if("4")) 


# In[ ]:




