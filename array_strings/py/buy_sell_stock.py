#!/usr/bin/env python
# coding: utf-8

# ## Time Complexity O(n)^2
# ## Space Complexity 0(1)

# In[6]:


stocks=[7,1,5,2,4]
   
def buy_sell_once(s):
    maxprofit=0
    #first loop
    for i in range(len(s)-1):
        print("i {}".format(i))
        print("s[i] {}".format(s[i]))
        for j in range(i+1,len(s)):
            print("j {}".format(j))
            print("s[j] {}".format(s[j]))
            if s[j] - s[i] > maxprofit:
                maxprofit=s[j] - s[i]
    return maxprofit

m=buy_sell_once(stocks)
print(m)


# ## Time Complexity O(n)
# ## Space Complexity 0(1)

# In[2]:


def buy_sell_once_ef(ls):
    max_profit=0
    min_price=ls[0]
    for price in range(len(ls)-1):
        min_price = min(min_price,ls[price])
        profit    = ls[price]-min_price
        max_profit=max(profit,max_profit)
    return max_profit
m=buy_sell_once_ef([5,10,10])
print(m)


# In[ ]:




