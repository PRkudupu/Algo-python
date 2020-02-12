#!/usr/bin/env python
# coding: utf-8

# ## Given two binary strings, return their sum (also a binary string).
# 
# The input strings are both non-empty and contains only characters 1 or 0.
# 
# ### Example 1:
# 
# Input: a = "11", b = "1"
# Output: "100"
# ### Example 2:
# 
# Input: a = "1010", b = "1011"
# Output: "10101"
# 

# In[ ]:


def add_binary(a,b):
    return '{0:b}'.format(int(a, 2) + int(b, 2))

print(add_binary('11','11'))


# This method has quite low performance in the case of large input numbers.
# 
# One could use Bit Manipulation approach to speed up the solution.

#    ### Logic
#    ![title](image/add_binary.png)
#    
#    ![title](image/op_addbinary.jpg)

# #### 1.Find the maxlength
# #### 2.Based on the length fill with zero
# #### 3.Create a variable for carry and result
# #### 4.Loop through tail, check if value is "1" .If yes then increment carry
# #### 5.if Carry % 2 == 1 then append 1 else zero
# #### 6. Divide carry by 2 (Keep doing this for all the elements in the array)
# #### 7. Outside the loop if carry is 1 then append 1
# #### 8. Reverse the string and join all the values
# 

# In[15]:


# Program with comments
def add_binary(a,b):
    n = max(len(a), len(b))
    print('\nlength',n)
    a, b = a.zfill(n), b.zfill(n)
    print('zfill a,b',a,b)
    carry = 0
    result = []
    for i in range(n - 1, -1, -1):
        print('\ni',i)
        print('carry on top',carry)
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1

        if carry % 2 == 1:
            result.append('1')
        else:
            result.append('0')
        print('\a[i]',a[i])
        print('\b[i]',b[i])
        print('carry after increement',carry)
        print('carry % 2',carry % 2)
        print('answer',result)
        #carry =cary//2
        print("Carry=carry// 2", carry)
        carry //= 2
        print("After division carry", carry)
    if carry == 1:
        result.append('1')
        print('result',result)
    result.reverse()

    return ''.join(result)
print(add_binary('01','11'))


# In[13]:


# Program without comments
def add_binary(a,b):
    n = max(len(a), len(b))
    a, b = a.zfill(n), b.zfill(n)
    carry = 0
    result = []
    for i in range(n - 1, -1, -1):
        if a[i] == '1':
            carry += 1
        if b[i] == '1':
            carry += 1

        if carry % 2 == 1:
            result.append('1')
        else:
            result.append('0')
        carry //= 2
    if carry == 1:
        result.append('1')
    result.reverse()
    return ''.join(result)    
print(add_binary('10','110'))


# ![title](image/bit_man.jpg)

# In[10]:


def addBinary(a, b) -> str:
        x, y = int(a, 2), int(b, 2)
        while y:
            answer = x ^ y
            carry = (x & y) << 1
            x, y = answer, carry
        return bin(x)[2:]
print(addBinary('001','101'))


#  def addBinary( a, b):
#             if len(a)==0: return b
#             if len(b)==0: return a
#             if a[-1] == '1' and b[-1] == '1':
#                 return addBinary(addBinary(a[0:-1],b[0:-1]),'1')+'0' 
#             if a[-1] == '0' and b[-1] == '0':
#                 return addBinary(a[0:-1],b[0:-1])+'0'
#             else:
#                 return addBinary(a[0:-1],b[0:-1])+'1'

# In[2]:


#  addBinary(addBinary(1,[]),1)+'0' 
#  addBinary(addBinary(1,[]),1) + '0' ==> addBinary(1,[]) return a =1 B
#  addBinary(1,1)+'0' 
#   return {addBinary(addBinary(a[0:-1],b[0:-1]),'1')+'0' } +'0' ==> addBinary(a[0:-1],b[0:-1]) return empty A
# return {addBinary(empty,'1')+'0' } +'0' ===> addBinary(empty,'1') return 1 A
#1 +'0' +'0' 


# In[3]:


addBinary("11","1")


# In[14]:


def add_binary(a,b):
    print("len(a)  {}".format(len(a)))
    print("len(b) {}".format(len(b)))
    print("a[-1] {}".format(a[-1]))  
    print("b[-1] {}".format(b[-1]))
    print("a[0:-1]) {}".format(a[0:-1]))  
    print("b[0:-1]) {}".format(b[0:-1]))
    if len(a)==0:
        print("len a==0")
        return b
    if len(b)==0:
        print("len b==0")
        return a
    if a[-1] == '1' and b[-1] == '1':
        print("First if condition 1,1")
        return addBinary(addBinary(a[0:-1],b[0:-1]),'1')+'0'
    if a[-1] == '0' and b[-1] == '0':
        print("Second if condition 0,0")
        return add_binary(a[0:-1],b[0:-1])+'0'
    else:
        print("Else")
        return add_binary(a[0:-1],b[0:-1])+'1'


# In[17]:


add_binary("1010","1011")


# In[12]:


def add_binary_nums(x, y):
        print((len(x)))
        print((len(x)))
        max_len = max(len(x), len(y)) 
        print("max_len {}".format(max_len))
        
        print()
        #Fill it with zeros
        x = x.zfill(max_len) 
        print("x {}".format(x))
        y = y.zfill(max_len)
        print("y {}".format(y))
        print(y)
          
        # initialize the result 
        result = '' 
          
        # initialize the carry 
        carry = 0
  
        # Traverse the string 
        for i in range(max_len - 1, -1, -1): 
            r = carry 
            r += 1 if x[i] == '1' else 0
            r += 1 if y[i] == '1' else 0
            result = ('1' if r % 2 == 1 else '0') + result 
            carry = 0 if r < 2 else 1     # Compute the carry. 
          
        if carry !=0 : result = '1' + result 
  
        return result.zfill(max_len) 
  


# In[13]:


add_binary_nums('100','10')


# In[ ]:




