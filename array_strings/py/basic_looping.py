#!/usr/bin/env python
# coding: utf-8

# In[1]:


def basic_looping(nums,ans):
    # Loop through till last except the last element in the list
    for i in range(0,len(nums)-1):
        print("first :",nums[i],i) 
     # loop through all the elements in the list without range
    for j in range(0,len(nums)):
        print("second :",nums[j],j) 
     # loop through all the elements in the list without range
    for k in nums:
        print("third :",k) 
    # loop through and increement by 2
    for l in range(0,len(nums),2):
        print("Increement by 2 :",l) 
    # Traverse from the end of the list
    for m in range(len(nums)-1,0,-1):
        print("Traverse from the tail :",nums[m],m) 
    # Traverse from the tail decrement by 2 
    for n in range(len(nums)-1,0,-2):
        print("Traverse from the tail decrement by 2 :",nums[n],n)    
    # Traverse from the head and tail using while loop
    head = 0
    tail =len(nums)-1
    # Note here = to sign is needed as if the no is odd it would miss the mid point
    while head <= tail:
        print("Head :",head, "tail",tail)
        # increement the head
        head +=1
        # Decrement the tail
        tail -=1
    #reverse a list
    print(nums[::-1])
    
print(basic_looping([3,2,2,1,0],7)) 


# In[ ]:




