#!/usr/bin/env python
# coding: utf-8

# # Data Cleaning
# You can also create content with Jupyter Notebooks. This means that you can include
# code blocks and their outputs in your book.  
#  

# ```{figure} ./images/test.drawio.png
# :height: 250px
# :name: architecture
# 
# Some architecture
# ```

# In[1]:


import numpy as np
import pandas as pd
from pandas_profiling import ProfileReport

df = pd.DataFrame(np.random.rand(100, 5), columns=["a", "b", "c", "d", "e"])


# In[2]:


profile = ProfileReport(df, title="Pandas Profiling Report")

profile.config.html.navbar_show = False


# In[3]:


from IPython.core.display import display, HTML
display(HTML(profile.to_html()))


# There is a lot more that you can do with outputs (such as including interactive outputs)
# with your book. For more information about this, see [the Jupyter Book documentation](https://jupyterbook.org)
