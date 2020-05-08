#!/usr/bin/env python
# coding: utf-8

# In[1]:


# In these exercises we'll apply groupwise analysis to our dataset.


# In[2]:


#Importing the library
import pandas as pd
import numpy as np


# In[3]:


#Creating data set in dictionary form
data = {'Name':['Prabhat', 'Aditya', 'Prabhat', 'Deepak',  
                 'Gaurav', 'Aditya', 'Deepak', 'Abhi'],  
        'Age':[25, 24, 22, 30,  
               33, 28, 32, 35],  
        'Address':['Bangalore', 'Delhi', 'Patna', 'Bhopal', 
                   'Ranchi', 'Delhi', 'Patna', 'Pune'],  
        'Qualification':['M.Tech', 'MA', 'MCA', 'Phd', 
                         'B.Tech', 'B.com', 'M.Tech', 'MA'], 
        'Score': [28, 34, 35, 45, 47, 50, 40, 45]}


# In[4]:


#Converting data set into Dataframe
df = pd.DataFrame(data)
df


# In[5]:


#Grouping Dataset for Name column   
df.groupby('Name').groups


# In[6]:


#Grouping Data set with the Name column in different way
#first() function will give top first data set values
gk = df.groupby('Name')
gk.first()


# In[7]:


#Grouping Data set with two columns together Name and Qualification 
df.groupby(['Name','Qualification']).groups


# In[8]:


#Grouping data set with Name column
#Summing up all numeric dataset w.r.t Name columns
df.groupby('Name').sum()


# In[9]:


#Grouping Data set with Name column
#Without sorting in ascending order
df.groupby(['Name'] , sort=False).sum()


# In[10]:


#Grouping Data set with Name column
#With sorting in ascending order
df.groupby(['Name'] , sort=True).sum()


# In[11]:


#Grouping data set with Name column
#Iterating over grouped data set
gp = df.groupby('Name')
for name,group in gp:
    print(name)
    print(group)


# In[12]:


#Grouping  data set with multiple column(Name,Qualificaton)
#Iterating over grouped data set
grp = df.groupby(['Name','Qualification'])
for name,group in grp:
    print(name)
    print(group)
    print()


# In[13]:


#Chosing specific name from Name column
grp = df.groupby('Name')
grp.get_group('Prabhat')


# In[14]:


#Grouping data set with multiple columns
#Chosing specific item from grouped columns
grp = df.groupby(['Name','Qualification'])
grp.get_group(('Abhi','MA'))


# In[15]:


#Grouping data set with Name column
# Aggregated performed operation on grouped data 
grp = df.groupby('Name')
grp.aggregate(np.sum)


# In[16]:


#Grouping data set with multiple columns
# Aggregated performed operation on grouped data
grp = df.groupby(['Name','Qualification'])
grp.aggregate(np.sum)


# In[17]:


#Grouping data set with Name column
# Aggregated multiple performed operation on grouped data
grp = df.groupby('Name')
grp['Age'].agg([np.sum, np.mean, np.std])


# In[18]:


grp = df.groupby('Name')
grp.agg({'Age':"sum",'Score':"std"})


# In[19]:


grp = df.groupby('Name')
sc = lambda x : (x - x.sum())/x.std()*10
grp.transform(sc)


# In[20]:


grp = df.groupby('Name')
grp.filter(lambda x : len(x)>=2)


# In[21]:


Cricket= {'Team':['Australia', 'England', 'South Africa', 
                   'Australia', 'England', 'India', 'India', 
                        'South Africa', 'England', 'India'], 
           'Player':['Ricky Ponting', 'Joe Root', 'Hashim Amla', 
                     'David Warner', 'Jos Buttler', 'Virat Kohli', 
                     'Rohit Sharma', 'David Miller', 'Eoin Morgan', 
                                                 'Dinesh Karthik'],                                           
          'Runs':[345, 336, 689, 490, 989, 672, 560, 455, 342, 376], 
             'Salary':[34500, 33600, 68900, 49000, 98899, 
                    67562, 56760, 45675, 34542, 31176] }


# In[22]:


df3 = pd.DataFrame(Cricket)


# In[23]:


df3


# In[24]:


#Total_Salary = df3['Salary'].groupby(df3['Team'])
Total_Salary = df3['Runs'].groupby(df3['Team'])


# In[25]:


Total_Salary.sum()


# In[26]:


#Creating dataset for college student for semester wise marks
Marks_Sem_wise = { 'Student_Name':['Aditya','Prabhat','Deepak'],
     'Semester_1':['60','65','70'],
     'Semester_2': ['68','73','80'],
     'Semester_3': ['58','69','76'],
     'Semester_4': ['60','78','70'],
     'Semester_5': ['80','68','69'],
     'Semester_6': ['79','90','81'],
     'Semester_7': ['80','80','60'],
     'Semester_8': ['70','80','60']
                 }


# In[27]:


#Converting sem_wise marks dataset into Dataframe
marks_data=pd.DataFrame(Marks_Sem_wise)
marks_data


# In[28]:


#Converting the column data in different columns name
grp = { 'Semester_1':'Year_1',
     'Semester_2': 'Year_1',
     'Semester_3': 'Year_2',
     'Semester_4': 'Year_2',
     'Semester_5': 'Year_3',
     'Semester_6': 'Year_3',
     'Semester_7': 'Year_4',
     'Semester_8': 'Year_4'}


# In[29]:


#Set the student name as a index
marks_data = marks_data.set_index('Student_Name')


# In[30]:


#Applying the converting column name into data frame
marks_data = marks_data.groupby(grp, axis=1).max()
print(marks_data)


# In[31]:


#Created data set of cheatan bhagat book list with number of readers
Chetan_bhagat_Book = { 
    "ID":[1, 2, 3], 
    "Novel_Book":["Half Girlfriend", "2 States", "The 3 mistakes of my life"], 
    "Month1_Reader":[300, 300, 400], 
    "Month2_Reader":[600, 400, 800], 
    "Month3_Reader":[400, 200, 200] }


# In[32]:


# Convert dictionary to dataframe 
df = pd.DataFrame(Chetan_bhagat_Book)
print(df)


# In[33]:


# Create the groupby_dict
#with single columns instead of multiple columns as Total Readers
groupby_dict = {"Month1_Reader":"Total_Readers", 
           "Month2_Reader":"Total_Readers", 
           "Month3_Reader":"Total_Readers", 
           "Novel_Book":"Novel_Book" } 
  
df = df.set_index('ID') 
df = df.groupby(groupby_dict, axis = 1).sum() 
print(df)


# In[ ]:




