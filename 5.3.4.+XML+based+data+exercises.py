
# coding: utf-8

# In[1]:

# importing pandas library
import pandas as pd

# importing ElementTree library from the xml package
from xml.etree import ElementTree as ET


# In[71]:

#######################################################
# 10 countries with the lowest infant mortality rates #
#######################################################

# reading the input XML file
# while running the below command, you may need to change the path of the input XML file
document_tree = ET.parse( r'C:\Users\User\Desktop\springboard\python\5.3 Working with data in files\data_wrangling_xml\data\mondial_database.xml' )

# creating an empty dataframe to store the output
df = pd.DataFrame(columns=['country', 'infant_mortality_rate'])

# initializing a count variable for data loading into the dataframe
i = 0

# iterating over the XML file for all the countries
for child in document_tree.getroot():
    mortality_flag = child.find('infant_mortality')
    # checking whether mortality information is present or not
    if mortality_flag != None:
        country_name = child.find('name').text
        infant_mortality_rate = child.find('infant_mortality').text
        # loading the extracted information into the dataframe
        df.loc[i]=[country_name, infant_mortality_rate]
        i+=1

# changing the data type from str to numeric
df[['infant_mortality_rate']] = df[['infant_mortality_rate']].apply(pd.to_numeric)

# calculating the top 10 countries with lowest mortality rate
df.sort_values(by = 'infant_mortality_rate').head(10)


# In[101]:

#########################################
# 10 cities with the largest population #
#########################################

# reading the input XML file
# while running the below command, you may need to change the path of the input XML file
document_tree = ET.parse( r'C:\Users\User\Desktop\springboard\python\5.3 Working with data in files\data_wrangling_xml\data\mondial_database.xml' )

# creating an empty dataframe to store the output
df = pd.DataFrame(columns=['city', 'population'])

# initializing a count variable for data loading into the dataframe
i = 0

# iterating over the XML file for all the countries
for element in document_tree.iterfind('country'):
    for subelement in element.getiterator('city'):
        population_flag = subelement.find('population')
        # checking whether population information is present or not
        if population_flag != None:
            city = subelement.find('name').text
            pop_iter = subelement.iterfind('population')
            for p in pop_iter:
                population = p.text
            # loading the extracted information into the dataframe
            df.loc[i]=[city, population]
            i+=1

# changing the data type from str to numeric
df[['population']] = df[['population']].apply(pd.to_numeric)

# calculating the top 10 countries with largest population
df.sort_values(by = 'population', ascending = False).head(10)


# In[8]:

#########################################################
# 10 ethnic groups with the largest overall populations #
#   (sum of best/latest estimates over all countries)   #
#########################################################

# reading the input XML file
# while running the below command, you may need to change the path of the input XML file
document_tree = ET.parse( r'C:\Users\User\Desktop\springboard\python\5.3 Working with data in files\data_wrangling_xml\data\mondial_database.xml' )

# creating an empty dataframe to store the output
df = pd.DataFrame(columns=['city', 'population', 'ethnicgroup'])

# initializing a count variable for data loading into the dataframe
i = 0

# iterating over the XML file for all the countries
for element in document_tree.iterfind('country'):
    for subelement in element.getiterator('city'):
        population_flag = subelement.find('population')
        ethnicgroup_flag = element.find('ethnicgroup')
        # checking whether ethnicgroup information is present or not
        if ethnicgroup_flag != None:
            city = subelement.find('name').text
            ethnicgroup = element.find('ethnicgroup').text
            pop_iter = subelement.iterfind('population')
            for p in pop_iter:
                population = p.text
            # loading the extracted information into the dataframe
            df.loc[i]=[city, population, ethnicgroup]
            i+=1

# calculating the top 10 ethnic groups with largest population
df.groupby(df.ethnicgroup).size().sort_values(ascending=False).head(10)


# In[27]:

###################################
# name and country of             #
# a) longest river                #
# b) largest lake                 #   
# c) airport at highest elevation #
###################################

# reading the input XML file
# while running the below command, you may need to change the path of the input XML file
document_tree = ET.parse( r'C:\Users\User\Desktop\springboard\python\5.3 Working with data in files\data_wrangling_xml\data\mondial_database.xml' )

# creating an empty dataframe to store the output for longest river
df1 = pd.DataFrame(columns=['river_name', 'river_length'])

# creating an empty dataframe to store the output for the largest lake
df2 = pd.DataFrame(columns=['lake_name', 'lake_area'])

# creating an empty dataframe to store the output for the airport with the highest elevation
df3 = pd.DataFrame(columns=['airport_name', 'airport_elevation'])

# initializing a count variable for data loading into the dataframe
i = 0

# iterating over the XML file for all the rivers
for element in document_tree.iterfind('river'):
    river_name = element.find('name').text
    river_length_flag = element.find('length')
    # checking whether river length information is present or not
    if river_length_flag != None:
        river_length = element.find('length').text
        # loading the extracted information into the dataframe
        df1.loc[i] = [river_name, river_length]
        i+=1

# initializing a count variable for data loading into the dataframe
i=0

# iterating over the XML file for all the lakes
for element in document_tree.iterfind('lake'):
    lake_name = element.find('name').text
    lake_area_flag = element.find('area')
    # checking whether lake area information is present or not
    if lake_area_flag != None:
        lake_area = element.find('area').text
        # loading the extracted information into the dataframe
        df2.loc[i] = [lake_name, lake_area]
        i+=1

# initializing a count variable for data loading into the dataframe
i=0

# iterating over the XML file for all the airports
for element in document_tree.iterfind('airport'):
    airport_name = element.find('name').text
    airport_elevation_flag = element.find('elevation')
    # checking whether airport elevation information is present or not
    if airport_elevation_flag != None:
        airport_elevation = element.find('elevation').text
        # loading the extracted information into the dataframe
        df3.loc[i] = [airport_name, airport_elevation]
        i+=1
    
# calculating the longest river
df1.sort_values(by = 'river_length', ascending = False).head(1)

# calculating the largest lake
df2.sort_values(by = 'lake_area', ascending = False).head(1)

# calculating the airport with the highest elevation
df3.sort_values(by = 'airport_elevation', ascending = False).head(1)

