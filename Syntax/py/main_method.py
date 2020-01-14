#!/usr/bin/env python
# coding: utf-8

# In[7]:


from urllib.request import urlopen
def fetch_words():
    #Using URL Open. In this example we are adding the story to the list
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        stack =[]
        for line in story:
            line_words=line.split()
            for words in line_words:
                #add words to the list
                stack.append(words)
        return stack

def print_words():
    for word in stack:
        print(word)
print(__name__)
""" IF __name__== __main__
def main():
    words =fetch_words()
    print_words(words)
    if __name__ == '__main__':
    main()
"""    


# In[11]:


#Calling main and its functions
from urllib.request import urlopen
def fetch_words():
    #Using URL Open. In this example we are adding the story to the list
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        stack =[]
        for line in story:
            line_words=line.split()
            for words in line_words:
                #add words to the list
                stack.append(words)
        return stack

def print_words(stack):
    for word in stack:
        print(word)

if __name__ == '__main__':
    words=fetch_words()
    print_words(words)


# In[13]:


# Calling all methods defined in main
from urllib.request import urlopen
def fetch_words():
    #Using URL Open. In this example we are adding the story to the list
    with urlopen('http://sixty-north.com/c/t.txt') as story:
        stack =[]
        for line in story:
            line_words=line.split()
            for words in line_words:
                #add words to the list
                stack.append(words)
        return stack

def print_words(items):
    for word in items:
        print(word)

        #define main method
def main():
    words=fetch_words()
    print_words(words)

#Call main method here.   
if __name__ == '__main__':
    main()
  


# In[18]:


# Calling main methods as arguments
import sys
from urllib.request import urlopen

def fetch_words(url):
    #Using URL Open. In this example we are adding the story to the list
    with urlopen(url) as story:
        stack =[]
        for line in story:
            line_words=line.split()
            for words in line_words:
                #add words to the list
                stack.append(words)
        return stack

def print_words(items):
    for item in items:
        print(item)

#define main method
def main(url):
    words=fetch_words(url)
    print_words(words)

#Call main method here.   
if __name__ == '__main__':
    main('http://sixty-north.com/c/t.txt')
  


# In[ ]:




