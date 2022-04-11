import numpy as np
import pandas as pd

df = pd.read_csv('Bike_Volume_-_Manual_Counts.csv')
df = df.drop(columns=['GLOBALID'])


def exploration(df):
    print(df.head())
    print(df.info())


def most_bikes_recorded(df, year):
    max = df[f'YR{year}_PM'].max()
    return (f'the most bikes recorded at one location in {year} is {max}')


def least_bikes_recorded(df, year):
    min_df = df[f'YR{year}_PM']
    min_arr = []
    for i in min_df:
        if i != -1:
            min_arr.append(i)
    return (f'the least bikes recorded at one location in {year} is {min(min_arr)}')


print(least_bikes_recorded(df, 2011))
#print(most_bikes_recorded(df, 2016))
