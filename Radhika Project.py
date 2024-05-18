# -*- coding: utf-8 -*-
"""
Created on Tue Jul  4 18:18:58 2023

@author: HP
"""

import pandas as pd
import numpy as np

# Create a dataframe “Camera_data” using Camera.csv
camera_data=pd.read_csv(r"D:\Nikhil Analytics\PYTHON\PYTHON Project\Camera.csv")


camera_data.shape
camera_data.columns

# Find out the percentage of blank values in each column.
camera_data.isnull().sum()
camera_data.isnull().sum()/len(camera_data)*100

# View the statistical summary of the data
camera_data.describe()

# Replace all the blank values with NaN.
camera_data.isnull().sum()
camera_data.replace("", np.nan, inplace=True)


# Now replace all the Blank values with the column median.
camera_data.fillna(camera_data.median())


# Add a new column “Discounted_Price” in which give a discount of 5% in the Price column.

camera_data['Discount_Price']=camera_data['Price']*0.05
camera_data


# Drop the columns Zoom Tele & Macro Focus range
camera_data.drop(['Zoom tele (T)'],axis=1)
camera_data.drop(['Macro focus range'],axis=1)

# OR
camera_data.drop(columns=['Zoom tele (T)'], inplace=True)
print(camera_data.columns)

camera_data.drop(columns=['Macro focus range'], inplace=True)
print(camera_data.columns)


# Replace the Model Name “Agfa ePhoto CL50” with “Agfa ePhoto CL250”

camera_data['Model']=camera_data['Model'].astype(str)
camera_data['Model']=camera_data['Model'].str.replace("Agfa ePhoto CL50","Agfa ePhoto CL250")

# OR
camera_data['Model'].replace('Agfa ePhoto CL50', 'Agfa ePhoto CL250', inplace=True)
print(camera_data['Model'].unique())


# Rename the column name from Release Date to Release Year

camera_data.rename(columns={'Release date': 'Release Year'}, inplace=True)
print(camera_data.columns)

# Which is the most expensive Camera?

most_expensive_index = camera_data['Price'].idxmax()
most_expensive_camera = camera_data.loc[most_expensive_index]
print(most_expensive_camera)

# Which camera have the least weight

least_weight_index = camera_data['Weight (inc. batteries)'].idxmin()
least_weight_camera = camera_data.loc[least_weight_index]
print(least_weight_camera)


# Group the data on the basis of their release year.
group_data = camera_data.groupby('Release Year')
group_data


# Extract the Name, Storage Include, Price, Disounted_Price & Dimensions columns.

camera_data[['Model','Storage included','Price','Discount_Price','Dimensions']]


# Extract the records for the cameras released in the year 2005 & 2006

cameras_2005_2006 = camera_data[(camera_data['Release Year'] == 2005) | (camera_data['Release Year'] == 2006)]

print(cameras_2005_2006)


# Find out 2007’s expensive & Cheapest Camera

cameras_2007 = camera_data[camera_data['Release Year'] == 2007]

most_expensive_2007 = cameras_2007.loc[cameras_2007['Price'].idxmax()]
cheapest_2007 = cameras_2007.loc[cameras_2007['Price'].idxmin()]

print("Most Expensive Camera in 2007:",most_expensive_2007)
print("\nCheapest Camera in 2007:",cheapest_2007)


# Which Year maximum number of models is released?

models_per_year = camera_data['Release Year'].value_counts()

max_models_year = models_per_year.idxmax()
  
print(f"The year with the maximum number of models released is {max_models_year} with {models_per_year[max_models_year]} models.")
















