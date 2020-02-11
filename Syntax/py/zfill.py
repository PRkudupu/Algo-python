#!/usr/bin/env python
# coding: utf-8

# <!-- HTML generated using hilite.me --><div style="background: #ffffff; overflow:auto;width:auto;border:solid gray;border-width:.1em .1em .1em .8em;padding:.2em .6em;"><pre style="margin: 0; line-height: 125%">Description
# Python string method zfill() pads string on the left <span style="color: #008800; font-weight: bold">with</span> zeros to fill width<span style="color: #333333">.</span>
# 
# Syntax
# Following <span style="color: #000000; font-weight: bold">is</span> the syntax <span style="color: #008800; font-weight: bold">for</span> zfill() method <span style="color: #FF0000; background-color: #FFAAAA">−</span>
# 
# <span style="color: #007020">str</span><span style="color: #333333">.</span>zfill(width)
# Parameters
# width <span style="color: #FF0000; background-color: #FFAAAA">−</span> This <span style="color: #000000; font-weight: bold">is</span> final width of the string<span style="color: #333333">.</span> This <span style="color: #000000; font-weight: bold">is</span> the width which we would get after filling zeros<span style="color: #333333">.</span>
# 
# Return Value
# This method returns padded string<span style="color: #333333">.</span>
# </pre></div>
# 

# In[8]:


def szfill(str,width):
    return str.zfill(width)

print(szfill('11',5))
print(szfill('11',10))
print(szfill('111',1))
print(szfill('my name is prathap',30))

