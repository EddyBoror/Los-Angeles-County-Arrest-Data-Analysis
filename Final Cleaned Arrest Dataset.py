#!/usr/bin/env python
# coding: utf-8

# # Step 1: Imports and Reading Data
# 
# Data Source: https://data.lacity.org/Public-Safety/Arrest-Data-from-2020-to-Present/amvf-fr72/about_data

# In[1]:


import pandas as pd # Manipulate Data Frame
import numpy as np # Computation
import matplotlib.pyplot as plt #visualization
import seaborn as sns #visualization
plt.style.use('ggplot')


# In[2]:


# Load the dataset from a CSV File
pd.read_csv('C:\\Users\\eledd\\OneDrive\\Desktop\\Arrest_2020.csv')


# In[3]:


# DF become my variable to reference, instead of using 
df = pd.read_csv('C:\\Users\\eledd\\OneDrive\\Desktop\\Arrest_2020.csv')


# In[4]:


#Display the first 5 rows of the dataset. # can be change to show more rows.
df.head()


# In[5]:


#Display the Last 5 rows of the dataset. # can be change to show more rows.
df.tail()


# In[6]:


# allows users to know how many "rows,columns" are in the CSV.
df.shape


# In[7]:


#looks for any duplicate data in the dataset.
df.duplicated().sum()


# In[8]:


#removes all duplcate data. If there was any. 
df.drop_duplicates(inplace=True)


# In[9]:


# shows all column in the dataset.
df.columns 


# In[10]:


#allows us to use a subset of our columns we only want to use.
df = df [['Report ID', 'Report Type', 'Arrest Date', 'Time',
       'Area Name', 'Age', 'Sex Code', 'Descent Code',
       'Charge Group Description', 'Arrest Type Code',
       'Charge', 'Charge Description', 'Disposition Description', 'LAT', 
        'LON', 'Booking Date','Booking Time', 'Booking Location',]].copy()


# In[11]:


# now you see 25 columns become 19 from the removal of unwanted data.
df.shape 


# In[12]:


df.info()


# # STEP 2: DATA CLEANING 

# In[13]:


#Arrest Date & Booking Date COLUMN need to be changeed to DATETIME
df.dtypes 


# In[14]:


#Change Arrest Date to date type
df['Arrest Date'] = pd.to_datetime(df['Arrest Date']).copy()


# In[15]:


#Change Booking Date to date type
df['Booking Date'] = pd.to_datetime(df['Booking Date']).copy()


# In[16]:


#format TIME to 12-hour format
df['Booking Time'] = pd.to_datetime(df['Booking Time'], format='%H%M', errors='coerce').dt.strftime('%I:%M %p').copy()


# In[17]:


#format TIME to 12-hour format
df['Time'] = pd.to_datetime(df['Time'], format='%H%M', errors='coerce').dt.strftime('%I:%M %p').copy()


# In[18]:


df


# In[19]:


#Dates type have been changed from object to date type. 
df.dtypes 


# In[20]:


#Check for NaaN/Missing values in the dataset.
df.isna().sum() 


# In[24]:


#Select columns with NaN value
columns_of_interest = ['Charge Group Description', 'Time', 'Arrest Type Code', 'Charge Description', 'Disposition Description', 'Booking Date', 'Booking Time', 'Booking Location']

# Replace NaN values with 'N/A' only in specified columns
df[columns_of_interest] = df[columns_of_interest].fillna('N/A')

# Check for NaN values in the cleaned DataFrame
print(df.isna().sum())


# In[25]:


df.shape


# In[27]:


#Show N/A output 
df


# # Step 3 Summary Statistic

# In[28]:


# Show statisic of the number value of the dataset
df.describe() 


# In[29]:


#Summary Information on the non-numeric columns
df.describe(include='object')  


# In[31]:


# What are Top 10 highest Charges Description?  
df['Charge Group Description'].value_counts()[:10]


# # Step 3: Data Visualization And Questions Answered
# 
# What are the Top 10 Age Group in dataste?
# 
# Answer- 29 years old

# In[32]:


charge_description = df['Charge Group Description'].value_counts()[:10]

# Display the relative frequencies
display(charge_description / df.shape[0])

# Bar Chart
(charge_description / df.shape[0]).plot(kind='bar')
plt.title('Top 10 Charges (as % of all charges)')
plt.show()


# In[33]:


# Bar Chart
ax = df['Age'].value_counts() \
    .head(10) \
    .plot(kind='bar', title='Top Age group in Arrest Data')
ax.set_xlabel('Age Range')
ax.set_ylabel('Count')


# In[34]:


# Pie Chart

top_age_groups = df['Age'].value_counts().head(20)

top_age_groups.plot(kind='pie', autopct='%1.1f%%')
plt.axis('equal') #Equal aspect ratio ensures that the pie chart is circular
plt.title('Top Age Groups in Arrest Data')
plt.show()


# In[35]:


#Seaborn library create visually appealing and informative statistical graphics

sns.barplot(data=df, x='Age', 
            y='Charge Group Description', 
            hue='Sex Code', 
            palette={'M': 'blue', 'F': 'red'})

plt.title('Stacked Bar Chart of Charges by Age Group')
plt.xlabel('Age')
plt.ylabel('Charge Group Description')
plt.legend(title='Sex Code')

plt.show()


# # Step 4: Export Cleaned Data

# In[36]:


#Data cleaned now I can export the new cleaned data into a CSV file.
df.to_csv('new_cleaned_data.csv', index=False)


# In[ ]:




