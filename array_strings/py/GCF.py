#!/usr/bin/env python
# coding: utf-8

# Write a function to which would return the greatest common of factor.
# 
# <b> Input : 18, 27</b>
# 
# <b> return: 9 </b>
# 
#         

# #### Loops

# In[5]:


def gcd(x,y):
    if x > y:
        small=y
    else:
        small=x
    for i in range(1,small+1):
        if(x % i == 0) and (y % i ==0):
            gcd=i
    return gcd
print(gcd(18,27))


# In[6]:


def gcd(x,y):
    small=min(x,y)
    print("x",x)
    print("y",y)
    print("small",small)
    for i in range(1,small+1):
        if x % i == 0 and y % i == 0:
            print("i",i)
            gcd=i
    return gcd
print(gcd(18,27))


# <b>Euclidean Algorithm</b>

# In[13]:


def gcd(x,y):
    while(y):
        x , y = y,x % y
    return x
print(gcd(18,27))


# #### Recursion

# In[17]:


def gcd(a,b):
    if(b == 0):
        return a
    else:
        return gcd(b,a%b)
print(gcd(18,27))


# In[ ]:




