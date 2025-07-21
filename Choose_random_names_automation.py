#!/usr/bin/env python
# coding: utf-8

# In[1]:


import random
import os
from datetime import date
from datetime import datetime


# In[2]:


def ChooseTwice(items):
    a = random.choice(items)
    b = random.choice(items)
    return a, b


# In[3]:


names = ["Ethel", "Mary", "Charlie", "Cora", "Robert", "Violet", "Daisy", "Matthew", "Thomas"]


# In[4]:


today = date.today()
dt = datetime.now()


# In[5]:

"""
(one, two) = ChooseTwice(names)
if one == two:
    print("%s is happy!" % one, dt)
else:
    print("%s likes %s!" % (one, two), dt)
"""

# In[6]:


#Write and append results to a text file
with open('/Users/anitaowens/Documents/GitHub/Python-Programming/file.txt','a') as f:
    (one, two) = ChooseTwice(names)
    if one == two:
        print("%s is happy!" % one, dt, file=f)
    else:
        print("%s likes %s!" % (one, two), dt, file=f)


# In[7]:


currentDirectory = os.getcwd()
print("this script has run successfully at {}".format(dt))

