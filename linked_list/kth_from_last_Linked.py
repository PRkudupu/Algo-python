#!/usr/bin/env python
# coding: utf-8

# In[1]:


Add a method that returns kth from last element of linked list.
# def kth_from_last(self, k)
# Ex - For list -> 2, 3, 4, 7, 0, 9
# k = 2 would return 0
# k = 1 would return 9


# In[2]:


class Node:
    def __init__(self,data=None):
        self.data=data
        self.next=None
        
class Linked_list:
    def __init__(self):
        self.head=Node()
    
    def append(self,data):
        cur=self.head
        new_node=Node(data)
        while cur.next != None:
            cur=cur.next
        cur.next=new_node
    
    def display(self):
        cur=self.head
        array =[]
        while cur.next != None:
            cur=cur.next
            array.append(cur.data)
        print(array)
    
    def reverse(self):
        cur=self.head
        prev=None
        while cur:
            nxt= cur.next
            cur.next =prev
            prev =cur
            cur =nxt
        self.head = prev
    
    def kth_from_last(self,k):
            self.reverse()
            cur=self.head
            prev=None
            count=1
            while cur:
                cur=cur.next
                if k == count:
                    return cur.data
                count+=1
                                   
            
ll=Linked_list()
ll.append(10)
ll.append(20)
ll.append(30)
ll.display()
print(ll.kth_from_last(1))
ll.display()


# In[ ]:


[10, 20, 30]
20
[20, 10, None]

