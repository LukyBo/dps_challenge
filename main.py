
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
df[df["Month"].str.contains("Summe")==False]

# Visualise historically the number of accidents per category
categories = ['Alkoholunfälle', 'Fluchtunfälle', 'Verkehrsunfälle']

for category in categories: 
    