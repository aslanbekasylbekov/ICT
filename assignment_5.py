'''
The objective of this assignment is to clean the csv file of the attendance.
The path to the csv file is "attendance_to_clean.csv"
You can find it in the instruction folder.
List of installed and authorized packages :
    - csv
    - pandas
    - datetime
    - numpy
You cannot use other packages than the listed ones (except built-in default package in python).
You can write you code after this comment :
'''

#Your code here:

import csv 
import pandas as pd 
import datetime
import numpy as np


na_value = ['NaN', 'error', '_', 'Null', 'NULL', '-', 'na']

df = pd.read_csv(r"attendance_to_clean.csv", na_values = na_value)



for index, row in df.iterrows():
    try:
        int(row['NAME_STUDENT'])
        df.loc[index, 'NAME_STUDENT'] = np.NAN
    except:
        pass

for index, row in df.iterrows():
    try:
        int(row['COUNT'])
    except:
        df.loc[index, 'COUNT'] = np.NAN

for index, row in df.iterrows():
    try:
        datetime.datetime.strptime(row['DATE'], '%Y-%m-%d')
    except:
        df.loc[index, 'DATE'] = np.NAN
df.dropna(inplace = True)

for x in df.index:
  if df.loc[x, "BEGIN_HOUR"] > 17:
    df.loc[x, "BEGIN_HOUR"] = np.NAN
  if float(df.loc[x, "COUNT"]) > 2:
        df.loc[x, 'COUNT'] = np.NAN

for index, row in df.iterrows():
    df.loc[index, 'COUNT'] = float(row['COUNT'])
    df.loc[index, 'WEEK'] = int(row['WEEK'])
    if (datetime.datetime.strptime(row['DATE'], '%Y-%m-%d') < datetime.datetime(2022, 8, 1)):
        df.loc[index, 'DATE'] = np.NAN

df.dropna(inplace=True)

df['DATE'] = pd.to_datetime(df['DATE'])
df.fillna(np.NAN, inplace = True)
df = df[df['NAME_STUDENT'].str.contains('[a-zA-Z]$')]
df = df[df['TYPE'].str.contains('[a-zA-Z]$')]
df = df.drop_duplicates()

df.sort_values(["NAME_STUDENT", "DATE", "BEGIN_HOUR", "WEEK"],
               axis = 0, ascending = True,
               inplace = True,
               na_position = "first")
df = df.reset_index()
df = df.drop('index', axis=1)

print(df)
