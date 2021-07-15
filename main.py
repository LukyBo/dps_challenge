
# Designed by: Lukas Bock
#-------------
# Created on: 14.07.2021
# ------------
# Version: Python 3.7.6, Spyder 4.0.1
# -------------
# Description: 
# This schript is used to visualise historically the number of accidents per category and 
# to forecast the values for the future. The method is applied to a data set which contains 
# the monthly values for traffic accidents in Munich until the end of 2020.
# ------------
# Input: 
#   Input data (csv file) -> (Input/Monatszahlen_Verkehrsunfälle.csv)

# %% Import libraries and functions

# Import libraries
import pandas as pd

# load data
df = pd.read_csv('Input/Monatszahlen_Verkehrsunfälle.csv')

# Print a list with column names using the pandas.DataFrame.columns method
list(df.columns)

# Drop unnecessary columns
df.drop(['VORJAHRESWERT','VERAEND_VORMONAT_PROZENT','VERAEND_VORJAHRESMONAT_PROZENT', 'ZWOELF_MONATE_MITTELWERT'],axis=1 ,inplace=True)

# Drop unnecessary rows
df = df[df.Month != 'Summe']

# Change Month Column to numbers between 1-12 and safe to df1
df1 = df['Month'].str.extract('.*(\d{2})', expand = False)

# Replace column 'Month' of df with column of df1
df = df.assign(Month=df1[:])

# Change the non-numeric objects into integers
df["Month"] = pd.to_numeric(df["Month"])

# Change the non-string objects into strings to be able to filter the df
df[['Category', 'Accident-type']] = df[['Category', 'Accident-type']].astype(pd.StringDtype())

# Create Column for days as datetime needs days as input
df["Day"] = 1

# Obtain a datetime column to be able to visualise historically the number of accidents 
df['date']=pd.to_datetime(df[['Year', 'Month', 'Day']])

# Create df for 'Alkoholunfälle'
#df_alk = df[df['Category'].isin(['Alkoholunfälle'])]
                                 #& df['Accident-type'] == 'insgesamt']

# Create df for 'Fluchtunfälle'

# Create df for 'Verkehrsunfälle'
#
MyPlots.historically_data(df)

# Visualise historically the number of accidents per category
categories = ['Alkoholunfälle', 'Fluchtunfälle', 'Verkehrsunfälle']

for category in categories: 
    