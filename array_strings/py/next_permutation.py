#!/usr/bin/env python
# coding: utf-8

# ## next_permutation
# Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.
# 
# If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).
# 
# The replacement must be in-place and use only constant extra memory.
# 
# Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.
# 
# <b>1,2,3 → 1,3,2</b><br>
# <b>3,2,1 → 1,2,3</b><br>
# <b>1,1,5 → 1,5,1</b>
# 
# 
# 

# ![](https://leetcode.com/media/original_images/31_Next_Permutation.gif)

# To illustrate the algorithm with an example, consider nums = [2,3,1,5,4,2]. <br>
# It is easy to see that i = 2 is the first i (from the right) such that nums[i] < nums[i+1].<br>
# Then we swap nums[2] = 1 with the smallest number in nums[3:] that is larger than 1, which is nums[5] = 2, after which we get nums = [2,3,2,5,4,1]. <br>
# To get the lexicographically next greater permutation of nums, we just need to sort nums[3:] = [5,4,1] in-place. <br>
# Finally, we reach nums = [2,3,2,1,4,5].

# In[39]:


#SOLUTION WITHOUT COMMENTS
def next_perm(ls):
    n = len(ls)
    for i in range(n-1, 0, -1):
        if ls[i] > ls[i-1]:
            j = i
            while j < n and ls[j] > ls[i-1]:
                idx = j
                j += 1
            ls[idx], ls[i-1] = ls[i-1], ls[idx]
            for k in range((n-i)//2):
                ls[i+k], ls[n-1-k] = ls[n-1-k], ls[i+k]
            break
    else:
        ls.reverse()
    return ls
print(next_perm([2,3,1,5,4,2]))
print(next_perm([3,2,1]))
print(next_perm([1,2,3]))   
print(next_perm([1,1,5]))


# In[30]:


#SOLUTION WITH COMMENTS
def next_perm(ls):
    # Find the length of the list
    n = len(ls)
    print("Length of the list :", len(ls))
    # Decreement from last element to the first
    for i in range(n-1, 0, -1):
        # if last element is greater then last previous. Then  j =i
        # find the first decreasing element .in the above example 4
        if ls[i] > ls[i-1]:
            print("Found the first decreasing element ls[i]",ls[i])
            j = i
            print("Reset both the pointers",ls[i], i,j)
            #Here the pointer has been reset
            #find the number find the next element which is greater than 4 
            # Here we increement j till we ls[j] is greater than 4 in the above example it is 5
            while j < n and ls[j] > ls[i-1]:
                idx = j
                j += 1
            # swap the elements in the list 4 and 5
            ls[idx], ls[i-1] = ls[i-1], ls[idx]
            # double-slash for “floor” division (rounds down to nearest whole number)
            for k in range((n-i)//2):
                ls[i+k], ls[n-1-k] = ls[n-1-k], ls[i+k]
            break
    else:
        ls.reverse()
    return ls
print(next_perm([2,3,1,5,4,2]))
"""print(next_perm([3,2,1]))
print(next_perm([1,1,5]))"""


# 
# ![alt text](image/np.JPG)

# In[47]:


def next_perm(ls):
    # Find the length of the list
    print("ls",ls)
    n = len(ls)
    print("Length of the list :", len(ls))
    # Decreement from last element to the first
    for i in range(n-1, 0, -1):
        # if last element is greater then last previous. Then  j =i
        # find the first decreasing element .in the above example 
        if ls[i] > ls[i-1]:
            print("\nFIND FIRST DECREASING ELEMENT")
            print("First decreasing element ls[i]:i",ls[i-1],i-1)
            j = i
            print("Reset both the pointers",i,j)
            print("ls",ls)
            #Here the pointer has been reset
            #find the number find the next element which is greater than 4 
            # Here we increement j till we ls[j] is greater than 4 in the above example it is 5
            while j < n and ls[j] > ls[i-1]:
                print("\nFIND NEXT GREATEST ELEMENT")
                print("j : {},len n :{},ls[j]:{},ls[i-1] {}".format(j,n,ls[j],ls[i-1]))
                idx = j
                j += 1
            print("idx is the pointer next greater num, idx {}  ls[idx] {}".format(idx,ls[idx]))
            # swap the elements in the list 4 and 5
            ls[idx], ls[i-1] = ls[i-1], ls[idx]
            print("After swap idx and ls[i-1](this was 2)".format(ls[idx],ls[i-1]))
            print("\n",ls)
            # double-slash for “floor” division (rounds down to nearest whole number)
            print("\nfind (n-i)//2) => ({} - {} )// 2 = {}".format(n,i,(n-i)//2))
            for k in range((n-i)//2):
                print("\nREVERSE")
                print("n",n)
                print("i",i)
                print("ls[i]",ls[i])
                print("(n-i)//2",(n-i)//2)
                print("k",k)
                print("ls[i+k]",ls[i+k])
                print("ls[n-1]",ls[n-1])
                print("ls[n-1-k]",ls[n-1-k])
                ls[i+k], ls[n-1-k] = ls[n-1-k], ls[i+k]
                break
        else:
            ls.reverse()
    return ls
print(next_perm([2,3,1,5,4,2]))
"""print(next_perm([3,2,1]))
print(next_perm([1,1,5]))"""


# In[35]:


#BRUTE FORCE. DOES NOT SOLVE ALL CASE
def next_perm(ls):
    # Check the max element in the list
    max_num=max(ls)
    min_num=min(ls)
    head =0
    tail =len(ls)-1
    
    #We know the max for the first element has been reached then swap the max element
    if ls[0] == max_num:
        temp= ls[-1]
        ls[-1]=ls[0]
        ls[0] =temp
        return ls
    while head <=tail:
        if ls[tail] > ls[tail-1]:
            temp= ls[tail]
            ls[tail]=ls[tail-1]
            ls[tail-1] =temp
        return ls
        head +=1
        tail -=1
    return ls
    
print(next_perm([3,2,1]))
print(next_perm([1,2,3]))   
print(next_perm([1,1,5]))

