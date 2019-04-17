#!/usr/bin/env python
# coding: utf-8

# # Setup

# The goal here is to:
# 1. Setup your Anaconda virtual environment
# 2. Setup your project structure using cookiecutter
# 3. Run the code in this notebook

# Once you have Anaconda installed, you should be able to use the following [command](https://conda.io/projects/conda/en/latest/commands.html) ([cheat sheet](https://docs.conda.io/projects/conda/en/4.6.0/_downloads/52a95608c49671267e40c689e0bc00ca/conda-cheatsheet.pdf)) to create your virtual environment (feel free to use your own environment name, i.e., change the value of "first-project"):
# ```sh
# $ conda create --name first-project python=3.7 -y
# ```

# Install the jupyter package so you can launch your own notebook (or run this one):
# ```sh
# $ conda install jupyter
# ```
# Note that Jupyter Notebook is included in the Anaconda 4.4+ distributions, so this may not be required.

# Install the cookiecutter package that will enable you to create a data science organization for your project:
# ```sh
# $ conda install -c conda-forge cookiecutter
# ```

# Navigate to the directory in which you want your project to reside in and execute the following command:
# ```sh
# $ cookiecutter https://github.com/drivendata/cookiecutter-data-science
# ```
# Look at the README.md file in this project to get a sense of the project structure.

# If you just want to download the notebook and ensure you have the requirements to run it, download requirements.txt and execute the following to install the packages:
# ```sh
# $ conda install --file requirements.txt
# ```

# # Exploratory Data Analysis

# Import packages

# In[1]:


import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt


# Import the dataset (mock dataset using [Mockaroo](https://mockaroo.com/)).

# In[2]:


df = pd.read_csv('../data/raw/MOCK_DATA.csv')


# Take a look at the first 10 records.

# In[3]:


df.head(10)


# Create a column 'year' by pulling the first 4 characters of the 'date' field.

# In[4]:


df['year'] = df['date'].str[:4]


# In[5]:


df.head()


# Summarize the numeric values in the dataframe.

# In[6]:


df.describe()


# Take a look at the distribution of 401k amounts by month.

# In[7]:


df['month'] = pd.to_datetime(df['date']).dt.strftime('%b')


# In[8]:


df.head()


# In[9]:


fig, ax = plt.subplots()
fig.set_size_inches((12,4))
sns.boxplot(x='month',y='401k_amount',data=df,ax=ax)
plt.show()

