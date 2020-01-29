#!/usr/bin/env python
# coding: utf-8

# ### Multiply Strings
# ![alt text](image/multiply_strings.JPG)

# In[10]:


# BRUTEFORCE METHOD. note this method would work for small numbers
"""The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly."""
def mul(num1,num2):
    result=0
    if len(num1) >110 or len(num2) > 110:
        return "less than 110"
    elif not num1.isdigit() or not num2.isdigit():
        return "not a digit."
    for i in range(0,int(num2)):
        result += int(num1)
    return result
print(mul('20','5'))
        


# #### SOLUTION
# ![alt text](image/mul.JPG)

# In[23]:


#WITH COMMENTS
def multiply(num1, num2):
    ls = [0] * (len(num1) + len(num2))  #placeholder for multiplication ndigit by mdigit result in n+m digits
    n = len(ls)-1 # position within the placeholder
    for n1 in num1[::-1]:
        tempPos = n 
        for n2 in num2[::-1]: 
            ls[tempPos] += int(n1) * int(n2) # ading the results of single multiplication
            ls[tempPos-1] += ls[tempPos]//10   # bring out carry number to the left array
            ls[tempPos] %= 10 # remove the carry out from the current array
            tempPos -= 1  # first shifting the multplication to the end of the first integer
        n -= 1   # then once first integer is exhausted shifting the second integer and starting 
        # once the second integer is exhausted we want to make sure we are not zero padding
        pointer = 0 # pointer moves through the digit array and locate where the zero padding finishes
        while pointer < len(ls)-1 and ls[pointer] == 0: 
            pointer += 1  # if we have zero before the numbers shift the pointer to the right
    return ''.join(map(str, ls[pointer:])) # only report the digits to the right side of the pointer
print(multiply('19','23'))


# In[25]:


#WITHOUT COMMENTS
def multiply(num1, num2):
    ls = [0] * (len(num1) + len(num2)) 
    n = len(ls)-1 
    for n1 in num1[::-1]:
        k=n
        for n2 in num2[::-1]: 
            ls[k] += int(n1) * int(n2) # multiply
            ls[k-1] += ls[k]//10  #carry to the left
            ls[k] %= 10  #remove carry out
            k -= 1 # shift to the end
        n -= 1 
        pointer = 0 
        while pointer < len(ls)-1 and ls[pointer] == 0: 
            pointer += 1
    return ''.join(map(str, ls[pointer:]))   
print(multiply('19','23'))


# In[8]:


#WITH COMMENTS AND PRINT
def multiply(num1, num2):
    ls = [0] * (len(num1) + len(num2)) 
    n = len(ls)-1 
    for n1 in num1[::-1]:
        tempPos = n 
        for n2 in num2[::-1]: 
            print('\nn1 * n2:',n1,"*",n2,"=",int(n1) * int(n2))
            print('b4 ls[tempPos] :',ls[tempPos])
            ls[tempPos] += int(n1) * int(n2) # multiply
            print('after ls[tempPos] += int(n1) * int(n2)  :',ls[tempPos])
            ls[tempPos-1] += ls[tempPos]//10  #carry to the left
            print("ls[tempPos]//10 :",ls[tempPos]//10)
            print("ls[tempPos-1],ls[tempPos] :",ls[tempPos-1],ls[tempPos])
            ls[tempPos] %= 10  #remove carry out
            print("after  %= 10 ls[tempPos] ls[tempPos] %= 10 :",ls[tempPos-1],ls[tempPos])
            tempPos -= 1 # shift to the end
            print("ls",ls)
        n -= 1 
        pointer = 0 
        while pointer < len(ls)-1 and ls[pointer] == 0: 
            pointer += 1
            print('\nls[pointer],ls :',ls[pointer],ls)
    print(ls[pointer:]) 
    return ''.join(map(str, ls[pointer:]))   
print(multiply('12','79'))


# In[ ]:




