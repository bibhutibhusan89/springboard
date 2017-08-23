
# coding: utf-8

# In[1]:

# doing the pandas import
import pandas as pd


# In[2]:

# importing json libraries
import json
# importing json_normalize functionality from the json library
from pandas.io.json import json_normalize


# In[54]:

############################################
# Find the 10 countries with most projects #
############################################

# reading the input json file as the string
# while running the below command, you may need to change the path of the input JSON file
input_data = json.load((open(r'C:\Users\User\Desktop\springboard\python\5.3 Working with data in files\data_wrangling_json\data_wrangling_json\data\world_bank_projects.json')))

# performing the normalization operation to extract country and project level information
df = json_normalize(input_data, 'majorsector_percent', ['countryshortname'])

# performing the group by operation on the country name to get the count of the projects
df1 = df.groupby(df.countryshortname)

# performing the count operation, followed by the descending sort and concluding with getting the top 10 countries
df2 = df1.size().sort_values(ascending = False).head(10)

# printing the final output
df2


# In[63]:

##########################################################################
# Find the top 10 major project themes (using column 'mjtheme_namecode') #
##########################################################################

# reading the input json file as the string
# while running the below command, you may need to change the path of the input JSON file
input_data = json.load((open(r'C:\Users\User\Desktop\springboard\python\5.3 Working with data in files\data_wrangling_json\data_wrangling_json\data\world_bank_projects.json')))

# performing the normalization operation to extract the project names
df = json_normalize(input_data, 'mjtheme_namecode')

# performing the group operation, followed by count, and then sorting operation
# once we get all the counts, the top 10 is extracted using the head() command
# it is seen that in top 10 projects, null project is also included
df.groupby(df.name).size().sort_values(ascending=False).head(10)


# In[73]:

############################################################################
# In 2. above you will notice that some entries have only the code and the #
#  name is missing. Create a dataframe with the missing names filled in.   #
############################################################################

# reading the input json file as the string
# while running the below command, you may need to change the path of the input JSON file
input_data = json.load((open(r'C:\Users\User\Desktop\springboard\python\5.3 Working with data in files\data_wrangling_json\data_wrangling_json\data\world_bank_projects.json')))

# performing the normalization operation to extract the project names
# replacing the null project names with string ***Not Available***
df = json_normalize(input_data, 'mjtheme_namecode')
df[df.name=='']='***Not Available***'

# performing the group operation, followed by count, and then sorting operation
# once we get all the counts, the top 10 is extracted using the head() command
# it is seen that in top 10 projects, previous null project is replaced with ***Not Available***
df.groupby(df.name).size().sort_values(ascending=False).head(10)

