#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random


# In[2]:


def ChooseTwice(items):
    a = random.choice(items)
    b = random.choice(items)
    return a, b


# In[3]:


names = ["Alice", "Bob", "Charlie", "Debra", "Peter", "Cora"]


# In[5]:


(one, two) = ChooseTwice(names)
if one == two:
    print("%s is happy!" % one)
else:
    print("%s likes %s!" % (one, two))

