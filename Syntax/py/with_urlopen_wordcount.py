#!/usr/bin/env python
# coding: utf-8

# In[12]:


import urllib
#Using URL Open. In this example we are adding the story to the list
with urllib.request.urlopen('http://sixty-north.com/c/t.txt') as story:
    stack =[]
    for line in story:
        line_words=line.split()
        for words in line_words:
            #add words to the list
            stack.append(words)
    for word in stack:
        print(word)


# In[ ]:




