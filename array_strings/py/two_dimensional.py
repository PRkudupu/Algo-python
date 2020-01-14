#!/usr/bin/env python
# coding: utf-8

# ### Processing and printing

# In[36]:


#Processing and printing
a =[[1,2,3,],[4,5,6]]

print('a:',a,'\na[0]:',a[0],'\na[1]:',a[1])


# In[15]:


#Print specific element in an list
print('a[0][1] :',a[0][1])


# In[24]:


# Process 2 dimensional array
for i in range(len(a)):
    for j in range(len(a[i])):
        print('a[i],[j]',a[i][j])
   


# In[41]:


### Handy feature to print
for i in a:
    for elem in i:
        print(elem)


# ### Sum of all elements in an array

# In[27]:


# sum of all the elements in the list
sum=0
for i in a:
    for elem in i:
        sum += elem
print('sum',sum)
        


# ### Create new 2 dimensional array 

# In[35]:


# Create 2 dimensional list based on m *n with 0
# Create an empty list and append new elements
n =3
m =4
a =[]
for i in range(n):
    print('[0]',[0])
    print('m',m)
    a.append([0] * m )
print(a)


# ### Using generators
# #### Python provides generator functions as a convenient shortcut to building iterators

# In[43]:


n=3
m=4
a =[[0]* m for i in range(n)]
print(a)


# ### Find max in 2 dimensional aray

# In[40]:


m=0
a= [[10,20,40],[20,400,200]]
for i in a:
    for elem in i:
        if elem > m:
            m=elem
        print(elem)
print('maximum',m)


# 
