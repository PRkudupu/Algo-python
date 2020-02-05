#!/usr/bin/env python
# coding: utf-8

# In[ ]:


However, graphs are easily built out of lists and dictionaries. For instance, here's a simple graph (I can't use drawings in these columns, so I write down the graph's arcs):

    A -> B
    A -> C
    B -> C
    B -> D
    C -> D
    D -> C
    E -> F
    F -> C
This graph has six nodes (A-F) and eight arcs. It can be represented by the following Python data structure:
    graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}


# In[1]:


def graph_node_count(ls):
    count =0
    for i in ls:
        count +=1
    return count
graph = graph = {'A': ['B', 'C'],
             'B': ['C', 'D'],
             'C': ['D'],
             'D': ['C'],
             'E': ['F'],
             'F': ['C']}
print(graph_node_count(graph))
        

