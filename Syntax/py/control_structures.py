#!/usr/bin/env python
# coding: utf-8

# ### Iteration with Loops
# 
# To iterate in Python, there are several options. A for loop can be used to iterate through a list or dictionary. Instead of the traditional for loop where we initialize a value i and increase / decrease it till it reaches an end value, Python's for loops are for-each in nature. This means that when you are iterating using a for loop over a list, you actually iterate over the items of that list.
# 
# If you also need the index values from the list while iterating, another possibility is to use enumerate, which is shown in an example below.
# 
# An additional way to iterate in Python is with a while loop. Just as in other programming languages, the while loop will repeat while some conditional statement is true. You will see more on conditional statements shortly, but first, here are examples of iteration with for and while loops.

# In[9]:


mylist =[0,1,2,3,4,5]

# iterate using for.Here we are printing each value in the list using in
for value in mylist:
    print("The value in the list",value)


# In[10]:


# print value and the index from the list using enumerate
for index,value in enumerate(mylist):
    print(" The index value in the list :"+ str(index) + ".The value at index i is :" +str(value))


# In[11]:


# print number from 0 to 9 using while loop
i=0
while (i<10):
    print(i)
    i+=1


# In[20]:


# Print key and dictionary value
dict ={'1':'first','2':'second','3':'third'}

for key in dict:
    print("The value of key: "+key +":"+ dict[key])


# ### Conditional Statements
# Conditional statements use boolean logic to help guide our decision process: the statement is true or false. These statements are structured using comparison operators: greater than (>), less than (<), and equal to (==).
# 
# Using conditional statements for control flow is accomplished in Python with the keywords: if, else, and elif. When doing multiple comparisons in Python, one after the other, the first comparison always usesif and the last comparison generally uses else. If additional control flow is needed, elif statements can be used; elif stands for "else if".

# In[22]:


num = 12
if num > 10:
    print("Number is greater than 10")
elif num < 10:
    print("Number is lesser than 10")
else:
    print("number is 10")


# In[ ]:




