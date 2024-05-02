#!/usr/bin/env python
# coding: utf-8

# # Introduce dataset
# 

# In[ ]:


import pandas as pd


# Exported dataset from NYC OpenData, saved in Downloads, then uploaded to Jupyter Notebook
# 

# In[14]:


df=pd.read_csv('NYPD_Arrest_Data__Year_to_Date.csv')


# In[17]:


#Display the first few rows of the dataset to verify it was imported correctly
df.head()


# # Data Cleansing

# In[19]:


#Exploratory Data Analysis (EDA)
df.info()


# In[22]:


#Check for missing values
missing_values=df.isnull().sum()


# In[23]:


missing_values


# In[134]:


#Define columns to keep
columns_to_keep=['ARREST_KEY','PD_DESC','ARREST_BORO','AGE_GROUP','PERP_SEX','PERP_RACE']


# In[135]:


#Subset the DataFrame to include only the selected columns
subset_df=df[columns_to_keep]


# In[136]:


#Display the first few rows of of the dataset, to ensure only displaying the selected columns
subset_df.head()


# In[137]:


#Exploratory Data Analysis (EDA) on the subset dataframe
subset_df.info()


# # Covert Data Type

# In[138]:


#List of columns to covert
categorical_columns=['PD_DESC','ARREST_BORO','AGE_GROUP','PERP_SEX','PERP_RACE']


# In[139]:


#Covert selected columns to categorical data type
for col in categorical_columns:
    subset_df[col]=subset_df[col].astype('category')


# In[140]:


#Perform EDA to ensure data type was successfully coverted
subset_df.info()


# In[141]:


#Initialize a dictionary to store unique values and their counts
unique_counts={}


# In[142]:


#Iterate over categorical columns
for col in subset_df.select_dtypes(include='category'):
    #Store unique values and their counts in the dictionary
    unique_counts[col]=subset_df[col].value_counts().to_dict()


# In[144]:


#Display unique values and their counts
unique_counts


# # Determining an initial comparison point using borough
# 

# In[153]:


#Group the data by 'ARREST_BORO', and count the occurrances
grouped_arrest_boro=subset_df.groupby(['ARREST_BORO']).size().reset_index(name='Counts')


# In[154]:


grouped_arrest_boro


# # Checking Overall 'Arrest Case' Occurances based on Sex, Race, and Age Group

# In[159]:


#Group the data by 'PERP_SEX', and count the occurrances
grouped_arrest_sex=subset_df.groupby(['PERP_SEX']).size().reset_index(name='Counts')


# In[158]:


grouped_arrest_sex


# In[161]:


#Group the data by 'PERP_RACE', and count the occurrances
grouped_arrest_race=subset_df.groupby(['PERP_RACE']).size().reset_index(name='Counts')


# In[162]:


grouped_arrest_race


# In[163]:


#Group the data by 'AGE_GROUP', and count the occurrances
grouped_arrest_age=subset_df.groupby(['AGE_GROUP']).size().reset_index(name='Counts')


# In[164]:


grouped_arrest_age


# # Filter DataFrame for Brooklyn 

# Based on the grouped_data, selecting Boro-'K' (Brooklyn) as the initial comparison point because it has the highest number (17402) of arrest cases out of all the other boroughs

# In[167]:


brooklyn_data=subset_df[subset_df['ARREST_BORO']=='K']


# In[166]:


brooklyn_data


# In[227]:


#Filter by race in Brooklyn
brooklyn_arrest_race=brooklyn_data.groupby(['PERP_RACE']).size().reset_index(name='Counts')


# In[228]:


brooklyn_arrest_race


# In[177]:


#Filter by age in Brooklyn
brooklyn_arrest_age=brooklyn_data.groupby(['AGE_GROUP']).size().reset_index(name='Counts')


# In[178]:


brooklyn_arrest_age


# In[179]:


#Filter by gender in Brooklyn
brooklyn_arrest_gender=brooklyn_data.groupby(['PERP_SEX']).size().reset_index(name='Counts')


# In[180]:


brooklyn_arrest_gender


# # Comparison within Brooklyn cases, based on Sex, Race and Age Group 

# In[190]:


#Group the data by sex and race, and calculate the total count for each
grouped_sex_race_counts=brooklyn_data.groupby(['PERP_SEX','PERP_RACE']).size().reset_index(name='Total_Count')


# In[191]:


grouped_sex_race_counts


# In[193]:


#Group the data by sex and age group, and calculate the total count for each
grouped_sex_age_counts=brooklyn_data.groupby(['PERP_SEX','AGE_GROUP']).size().reset_index(name='Total_Count')


# In[194]:


grouped_sex_age_counts


# # Visualization

# In[202]:


import matplotlib.pyplot as plt
import seaborn as sns


# In[207]:


#Plot a stcked bar chart using Seaborn
plt.figure(figsize=(10,6))
sns.barplot(x='PERP_RACE',y='Total_Count',hue='PERP_SEX', data=grouped_sex_race_counts, palette='Set1')
plt.title('Distribution of Arrests by Sex and Race in Brooklyn')
plt.xlabel('Race and Sex')
plt.ylabel('Number of Arrests')
plt.xticks(rotation=50,ha='right')
plt.legend(title='Sex')
plt.tight_layout()
plt.show()


# In[209]:


#Plot a stcked bar chart using Seaborn
plt.figure(figsize=(10,6))
sns.barplot(x='AGE_GROUP',y='Total_Count',hue='PERP_SEX', data=grouped_sex_age_counts, palette='Set1')
plt.title('Distribution of Arrests by Age Group and Sex in Brooklyn')
plt.xlabel('Sex and Age Group')
plt.ylabel('Number of Arrests')
plt.xticks(rotation=50,ha='right')
plt.legend(title='Sex')
plt.tight_layout()
plt.show()


# # Conclusion Statement

# Based on the plotted outcome, it is evident that Black individuals, both male and female, constitute the demographic with the highest number of arrest case in Brooklyn. Additionally, among all Brooklyn arrest cases, individual within the age group of 25-44 exhibit the highest freequency of arrests for both males and females.However, it is important to acknowledge the potential influence of bias within the dataset, such as the size of Black population relative to other racial groups. 

# In[ ]:




