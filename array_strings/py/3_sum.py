#!/usr/bin/env python
# coding: utf-8

# Given an array nums of n integers, are there elements a, b, c in nums such that a + b + c = target 
# 
# Note:
# 
# <b>Example:</b>
# 
# Given array nums = [-8, -7, 5, 2], target=0
# 
# return (-7,5,2)

# In[6]:


#O(n3) . Here the time complexity is O n3


# In[7]:


def three_sum(arr,target):
    for i in range(len(arr)):
        for j in range(i+1,len(arr)):
            for k in range(j+1,len(arr)):
                if arr[i]+arr[j]+arr[k] == target:
                    return arr[i],arr[j],arr[k]
print(three_sum([-8,-7,5,2],0))


# Here the time complexity is <b> O (n2) </b>

# In[16]:


def three_sum_sort(arr,target):
    #sort
    arr.sort
    for i in range(len(arr)-2):
        partial_target=target-arr[i]
        j=i+1
        k=len(arr)-1
        while j < k:
            partial_sum=arr[j]+arr[k]
            if partial_sum == partial_target:
                return (arr[i],arr[j],arr[k])
            elif partial_sum > target:
                k-=1
            else:
                j+=1
    return None
print(three_sum_sort([-8,-7,5,2],0))           


# Here the time complexity is <b> O (n2)

# In[24]:


# Python3 program to find a triplet using Hashing 
# returns true if there is triplet with sum equal 
# to 'sum' present in A[]. Also, prints the triplet 
def three_sum_hash(A,sum): 
    for i in range(0,len(A)-1): 
        #Find pair in subarray A[i+1..n-1]  
        # with sum equal to sum - A[i] 
        s = set() 
        curr_sum = sum - A[i] 
        for j in range(i+1,len(A)): 
            if (curr_sum - A[j]) in s: 
                print("Triplet is", A[i],  
                        ", ", A[j], ", ", curr_sum-A[j]) 
                return True
            s.add(A[j]) 
    return False
print(three_sum_hash([-8,-7,5,2],0))  


# In[9]:


def three_sum(num,target):
    for i in range(0,len(num)-1):
        s=set()
        curr_sum = target - num[i]
        for j in range(i+1,len(num)):
            if(curr_sum- num[j]) in s:
                return(num[i],num[j],curr_sum-num[j])
            s.add(num[j])
    return False

print(three_sum([-8,-7,5,2],0)) 


# In[2]:


def three_sum_n(arr,target):
    #sort the array
    arr.sort
    for i in range(len(arr)-2):
        print("i {}".format(i))
        print("target {}".format(target))
        print("arr[i] {}".format(arr[i]))
        partial_target =target-arr[i]
        print("partial_target {}".format(partial_target))
        j=i+1
        k=len(arr) - 1
        print ("k {}".format(k))
        while j < k:
            partial_sum = arr[j]+arr[k]
            print("arr[j] {}".format(arr[j]))
            print("arr[k] {}".format(arr[k]))
            print("partial_sum {}".format(partial_sum))
            print("arr[i] {}".format(arr[i]))
            if partial_sum == partial_target:
                return (arr[i],arr[j],arr[k])
            elif partial_sum > partial_target: # Make sum smaller
                k-=1
            else:
                j+=1
    return None

print(three_sum_n([-8,-7,5,2],0))


# In[1]:


def three_sum(nums,ans):
    for i in range(0,len(nums)-1):
        s=set()
        cur_sum= ans-nums[i]
        print("nums[i]",nums[i])
        for j in range(i+1,len(nums)):
            if (cur_sum - nums[j]) in s:
                print("ans",ans)
                print("nums[j]",nums[j])
                print("cur_sum",cur_sum)
                print("cur_sum - nums[j]",cur_sum - nums[j])
                return (nums[i],nums[j],cur_sum-nums[j])
            s.add(nums[j])
            print(s)
    return False              
print(three_sum([3,2,2,1],7))


# In[ ]:




