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

# <!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">Approach <span style="color: #0000DD; font-weight: bold">1</span>:<b> Bit<span style="color: #333333">-</span>by<span style="color: #333333">-</span>Bit Computation</b>
# Algorithm
# 
# That<span style="background-color: #fff0f0">&#39;s a good old classical algorithm, and there is no conversion from binary string to decimal and back here. Let&#39;</span>s consider the numbers bit by bit starting <span style="color: #008800; font-weight: bold">from</span> <span style="color: #0e84b5; font-weight: bold">the</span> <span style="color: #0e84b5; font-weight: bold">lowest</span> <span style="color: #0e84b5; font-weight: bold">one</span> <span style="color: #0e84b5; font-weight: bold">and</span> <span style="color: #0e84b5; font-weight: bold">compute</span> <span style="color: #0e84b5; font-weight: bold">the</span> <span style="color: #0e84b5; font-weight: bold">carry</span> <span style="color: #0e84b5; font-weight: bold">this</span> <span style="color: #0e84b5; font-weight: bold">bit</span> <span style="color: #0e84b5; font-weight: bold">will</span> <span style="color: #0e84b5; font-weight: bold">add.</span>
# 
# Start <span style="color: #008800; font-weight: bold">from</span> <span style="color: #0e84b5; font-weight: bold">carry</span> <span style="color: #333333">=</span> <span style="color: #6600EE; font-weight: bold">0.</span> If number a has <span style="color: #0000DD; font-weight: bold">1</span><span style="color: #333333">-</span>bit <span style="color: #000000; font-weight: bold">in</span> this lowest bit, add <span style="color: #0000DD; font-weight: bold">1</span> to the carry<span style="color: #333333">.</span> The same <span style="color: #008800; font-weight: bold">for</span> number b: <span style="color: #008800; font-weight: bold">if</span> number b has <span style="color: #0000DD; font-weight: bold">1</span><span style="color: #333333">-</span>bit <span style="color: #000000; font-weight: bold">in</span> the lowest bit, add <span style="color: #0000DD; font-weight: bold">1</span> to the carry<span style="color: #333333">.</span> 
# The same for number b: if number b has 1-bit in the lowest bit, add 1 to the carry. At this point the carry for the lowest bit could be equal to (00)2,(01)2 or (10)2
# 
# Now append the lowest bit of the carry to the answer, <span style="color: #000000; font-weight: bold">and</span> move the highest bit of the carry to the <span style="color: #007020">next</span> order bit<span style="color: #333333">.</span>
# 
# Repeat the same steps again, <span style="color: #000000; font-weight: bold">and</span> again, till <span style="color: #007020">all</span> bits <span style="color: #000000; font-weight: bold">in</span> a <span style="color: #000000; font-weight: bold">and</span> b are used up<span style="color: #333333">.</span> If there <span style="color: #000000; font-weight: bold">is</span> still nonzero carry to add, add it<span style="color: #333333">.</span> Now reverse the answer string <span style="color: #000000; font-weight: bold">and</span> the job <span style="color: #000000; font-weight: bold">is</span> done<span style="color: #333333">.</span>
# </pre></div>
# 

#    ### Logic
#    ![title](image/add_binary.png)

# In[6]:


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
        print('carry',carry)
        print('carry % 2',carry % 2)
        print('answer',result)
        #carry =cary//2
        print("Carry //= 2", carry)
        carry //= 2
        print("After division", carry)
    if carry == 1:
        result.append('1')
    result.reverse()

    return ''.join(result)
print(add_binary('10','110'))


# In[7]:


# Program with comments
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




