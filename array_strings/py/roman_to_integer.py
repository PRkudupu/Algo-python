#!/usr/bin/env python
# coding: utf-8

# Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.
# 
# Symbol       Value
# I             1 <br>
# V             5 <br>
# X             10 <br>
# L             50 <br>
# C             100 <br>
# D             500 <br>
# M             1000 <br>
# For example, two is written as II in Roman numeral, just two one's added together. Twelve is written as, XII, which is simply X + II. The number twenty seven is written as XXVII, which is XX + V + II.
# 
# Roman numerals are usually written largest to smallest from left to right. However, the numeral for four is not IIII. Instead, the number four is written as IV. Because the one is before the five we subtract it making four. The same principle applies to the number nine, which is written as IX. There are six instances where subtraction is used:
# 
# I can be placed before V (5) and X (10) to make 4 and 9. 
# X can be placed before L (50) and C (100) to make 40 and 90. 
# C can be placed before D (500) and M (1000) to make 400 and 900.
# Given a roman numeral, convert it to an integer. Input is guaranteed to be within the range from 1 to 3999.
# 
# <b>Example 1:</b>
# 
# Input: "III"
# Output: 3
# <br>
# 
# <b>Example 2: </b>
# 
# Input: "IV"
# Output: 4
# <br>
# 
# <b>Example 3:</b>
# 
# Input: "IX"
# Output: 9
# <br>
# 
# <b>Example 4:</b>
# 
# Input: "LVIII"
# Output: 58
# Explanation: L = 50, V= 5, III = 3.
# <br>
# 
# <b>Example 5:</b>
# 
# Input: "MCMXCIV"
# Output: 1994
# Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.
# <br>
#    Hide Hint #1  
# I - 1
# V - 5
# X - 10
# L - 50
# C - 100
# D - 500
# M - 1000
# <br>
#    Hide Hint #2  
# Rules:
# * If I comes before V or X, subtract 1 eg: IV = 4 and IX = 9
# * If X comes before L or C, subtract 10 eg: XL = 40 and XC = 90
# * If C comes before D or M, subtract 100 eg: CD = 400 and CM = 900
# 
# <b>Solution</b>:<br>
# * we store all the roman characters as key value pairs in dictionary
# * The trick is that the last letter is always added. Except the last one, if one letter is less than its latter one, this letter is subtracted

# In[5]:


def rom_to_int(ls):
    dic ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result =0
    ls=ls.upper()
    for i in range(len(ls)-1):
        if dic[ls[i]] < dic[ls[i+1]]:
            result -= dic[ls[i]]
        else:                    
            result += dic[ls[i]]
    return result  +dic[ls[-1]]
print(rom_to_int("V"))
print(rom_to_int("IV"))
print(rom_to_int("IX"))
print(rom_to_int("LVIII"))
print(rom_to_int("MCMXCIV"))


# In[4]:


def rom_to_Integer(ls):
    dic ={'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}
    result =0
    ls=ls.upper()
    for i in range(len(ls)-1):
        if dic[ls[i]] < dic[ls[i+1]]:
            result -= dic[ls[i]]
        else:                    
            result += dic[ls[i]]
        print("result",result)
    print("ls[-1]",ls[-1])
    print(dic[ls[-1]])
    return result +  dic[ls[-1]]     

print(rom_to_Integer("IV"))
#print(rom_to_int("IV"))
"""print(rom_to_int("IX"))
print(rom_to_int("LVIII"))
print(rom_to_int("MCMXCIV"))"""


# In[ ]:




