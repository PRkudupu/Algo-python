#!/usr/bin/env python
# coding: utf-8

# ### PRINT FIZZ BUZZ WHEN NUM IS DIV 3 AND 5
# ### PRINT FIZZ  WHEN NUM IS DIV 3 
# ### PRINT BUZZ WHEN NUM IS DIV 5

# In[4]:


def fizzbizz(num):
    for i in range(1,num):
        if i%3==0 and i%5==0:
            print("FIZZBuzz")
        elif i%3==0:
            print("FIZZ")
        elif i%5 ==0:
            print("BUZZ")
        else:
            print(i)

output=fizzbizz(101)
print(output)


# In[ ]:




