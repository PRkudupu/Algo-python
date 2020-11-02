#!/usr/bin/env python
# coding: utf-8

# In[9]:


# Example for break
i=3
j=5

while i:
    i-=1
    print("i",i)
    while j:
        j -=1
        print("j",j)
        if j == 4:
            break
    print("outside j loop")
    print(j,i)

        


# In[ ]:




