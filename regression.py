#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import matplotlib.pyplot as plt
import pandas as pd


# In[2]:


dataset = pd.read_csv('Train.csv')
X = dataset.iloc[:, :-1].values
y = dataset.iloc[:, -1].values


# In[ ]:


print(x)


# In[ ]:


print(y)


# In[5]:


# Splitting the dataset into the Training set and Test set
from sklearn.model_selection import train_test_split
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.2, random_state = 0)


# In[ ]:


# Training the Simple Linear Regression model on the Training set
from sklearn.linear_model import LinearRegression
regressor = LinearRegression()
regressor.fit(X_train, y_train)


# In[4]:


# Predicting the Test set results
y_pred = regressor.predict(X_test)


# In[ ]:




