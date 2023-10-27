#!/usr/bin/env python
# coding: utf-8

# In[25]:


#Sunburst Charts in Python
import plotly.express as pex


# In[26]:


#Sample data
data= {
    'id': ["A", "B", "C", "D", "E", "F", "G"],
    'parent': ["", "A", "A", "B", "B", "C", "D"],
    'value': [10, 15, 7, 8, 12, 6, 5],
}


# In[27]:


# Create a sunburst chart
fig= pex.sunburst(data, names='id', parents='parent', values='value')


# In[28]:


#Set the chart title
fig.update_layout(title_text="Sunburst Chart")


# In[29]:


#Show the chart
fig.show()


# In[ ]:




