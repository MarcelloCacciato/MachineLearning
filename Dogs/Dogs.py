
# coding: utf-8

# In[1]:

import numpy as np


# In[2]:

import matplotlib.pyplot as plt


# In[3]:

greyhounds = 500


# In[4]:

labradors = 500


# In[5]:

grey_h = 100 + 10*np.random.randn(greyhounds)


# In[10]:

lab_h = 90 + 10*np.random.randn(labradors)


# In[11]:

plt.hist([grey_h,lab_h],stacked=True,color=['r','b'])


# In[12]:

plt.show()


# In[ ]:



