#!/usr/bin/env python
# coding: utf-8

# # Univariate,Bivariate,MultiVariate Analysis & Histograms
# 

# In[34]:


import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns


# In[2]:


# The iris dataset that comes with the seaborn library
df=sns.load_dataset('iris')


# In[3]:


# Preview the first ten rows of the iris dataset
df.head(10)


# In[4]:


# Preview the last five rows of the iris dataset (five rows are displayed by default)
df.tail()


# In[5]:


# Preview the structure of the data, (150, 5) represents a total of 150 rows and 5 columns of data
df.shape


# In[6]:


type(df)


# In[7]:


df


# In[8]:


# View the type of each column
df.info()


# In[9]:


# See how many types of plants are included in the "species" column
df['species'].unique()


# ### Data processing (extracting subsets of data for different types of plants)

# In[10]:


# Previewing the dataset of "setosa" type plants
df.loc[df['species']=='setosa']


# In[11]:


# Extract subset data for different plant types
df_setosa=df.loc[df['species']=='setosa']


# In[12]:


df_setosa.info()


# In[13]:


df_virginica=df.loc[df['species']=='virginica']
df_versicolor=df.loc[df['species']=='versicolor']


# In[14]:


df_virginica.info()


# In[15]:


df_versicolor.count()


# ### Univariate Analysis

# In Python, such sequence of characters is included inside single or double quotes. As far as language syntax is concerned, there is no difference in single or double quoted string. Both representations can be used interchangeably. However, if either single or double quote is a part of the string itself, then the string must be placed in double or single quotes respectively.

# In[16]:


# Visual analysis of sepal length according to three plants (setosa, virginica, versicolor)
plt.plot(df_setosa['sepal_length'])
plt.plot(df_virginica['sepal_length'])
plt.plot(df_versicolor['sepal_length'])
plt.ylabel('sepal_length')
plt.show()


# In[17]:


plt.plot(df_setosa["sepal_length"],marker="x")
plt.plot(df_virginica['sepal_length'],marker='*')
plt.plot(df_versicolor['sepal_length'],marker='o')
plt.ylabel('sepal_length')
plt.show()


# In[18]:


# Visual analysis of sepal width according to three plants (setosa, virginica, versicolor)
plt.plot(df_setosa['sepal_width'])
plt.plot(df_virginica['sepal_width'])
plt.plot(df_versicolor['sepal_width'])
plt.ylabel('sepal_width')
plt.show()


# In[19]:


# Visual analysis of petal length according to three plants (setosa, virginica, versicolor)
plt.plot(df_setosa['petal_length'])
plt.plot(df_virginica['petal_length'])
plt.plot(df_versicolor['petal_length'])
plt.ylabel('petal_length')
plt.show()


# In[20]:


# Visual analysis of petal width according to three plants (setosa, virginica, versicolor)
plt.plot(df_setosa['petal_width'])
plt.plot(df_virginica['petal_width'])
plt.plot(df_versicolor['petal_width'])
plt.ylabel('petal_width')
plt.show()


# It can be seen from the above analysis attempt that petal_width or petal_length is ideal for univariate analysis because their features are significant

# We can also put these features in a latitude for feature comparison, such as the following example:

# In[21]:


plt.plot(df_setosa['species'],df_setosa['sepal_length'],marker='o')
plt.plot(df_virginica['species'],df_virginica['sepal_length'],marker='o')
plt.plot(df_versicolor['species'],df_versicolor['sepal_length'],marker='o')
plt.ylabel('sepal_length')
plt.show()


# In[22]:


plt.plot(df_setosa['petal_width'],df_setosa['species'],marker='o')
plt.plot(df_virginica['petal_width'],df_virginica['species'],marker='x')
plt.plot(df_versicolor['petal_width'],df_versicolor['species'],marker='*')
plt.xlabel('petal_width')
plt.show()


# In[23]:


plt.plot(df_setosa['petal_length'],np.zeros_like(df_setosa['petal_length']),'o')
plt.plot(df_virginica['petal_length'],np.zeros_like(df_virginica['petal_length']),'x')
plt.plot(df_versicolor['petal_length'],np.zeros_like(df_versicolor['petal_length']),'*')
#plt.plot(df_setosa['sepal_length'],np.ones_like(df_setosa['sepal_length']),'o')
#plt.plot(df_virginica['sepal_length'],np.ones_like(df_virginica['sepal_length']),'x')
#plt.plot(df_versicolor['sepal_length'],np.ones_like(df_versicolor['sepal_length']),'*')
plt.xlabel('Petal length')
plt.show()


# In[24]:


plt.plot(df_setosa['petal_length'],np.ones_like(df_setosa['petal_length']),'o')
plt.plot(df_virginica['petal_length'],np.ones_like(df_virginica['petal_length']),'x')
plt.plot(df_versicolor['petal_length'],np.ones_like(df_versicolor['petal_length']),'*')
#plt.plot(df_setosa['sepal_length'],np.ones_like(df_setosa['sepal_length']),'o')
#plt.plot(df_virginica['sepal_length'],np.ones_like(df_virginica['sepal_length']),'x')
#plt.plot(df_versicolor['sepal_length'],np.ones_like(df_versicolor['sepal_length']),'*')
plt.xlabel('Petal length')
plt.show()


# ### Bivariate Analysis

# In[25]:


# Bivariate analysis of petal_length and petal_width of the three types of plants (these two variables have significant characteristics from the univariate analysis)
plt.plot(df_setosa['petal_length'],df_setosa["petal_width"],'o')
plt.plot(df_virginica['petal_length'],df_virginica["petal_width"],'x')
plt.plot(df_versicolor['petal_length'],df_versicolor["petal_width"],'*')
plt.xlabel('Petal length')
plt.ylabel('petal_width')
plt.show()


# Bivariate analysis can be performed on the characteristics of the three plants according to what you want

# In[26]:


sns.FacetGrid(df,hue="species",height=7).map(plt.scatter,"petal_length","petal_width").add_legend()


# In[27]:


sns.FacetGrid(df,hue="species",height=5).map(plt.scatter,"petal_length","sepal_width").add_legend()


# ### Multivariate Analysis

# In[28]:


# View analysis of the individual characteristics of the three plants
sns.pairplot(df,hue="species",height=3)


# In[29]:


# When there are many features or columns in the data set, the above method may not achieve the expected results, so we can use the following methods for data analysis
df.corr()


# The analysis results show that petal_length and petal_width have strong coherence, that is to say, the longer the length of the stamen, the wider the width of the stamen

# ### Histograms

# In[199]:


plt.hist(df["petal_length"]) 


# In[36]:


plt.hist(df_setosa["petal_length"]) 
plt.hist(df_virginica["petal_length"]) 
plt.hist(df_versicolor["petal_length"])


# In[37]:


sns.distplot(df["petal_length"])


# In[38]:


sns.distplot(df_setosa["petal_length"])
sns.distplot(df_virginica["petal_length"])
sns.distplot(df_versicolor["petal_length"])


# In[207]:


sns.distplot(df_versicolor["petal_length"])


# What Is a Bell Curve?
# 
# A bell curve is a common type of distribution for a variable, also known as the normal distribution. The term "bell curve" originates from the fact that the graph used to depict a normal distribution consists of a symmetrical bell-shaped curve.
# The highest point on the curve, or the top of the bell, represents the most probable event in a series of data (its mean, mode, and median in this case), while all other possible occurrences are symmetrically distributed around the mean, creating a downward-sloping curve on each side of the peak. The width of the bell curve is described by its standard deviation.
# 
# Normal distribution, also known as the Gaussian distribution, is a probability distribution that is symmetric about the mean, showing that data near the mean are more frequent in occurrence than data far from the mean. In graph form, normal distribution will appear as a bell curve.
