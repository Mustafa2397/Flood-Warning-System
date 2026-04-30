import pandas as pd
import numpy as np

df = pd.read_csv('Master_TimeSeries_Data.csv')

print("--- Data Info ---")
print(df.info())

print("\n--- First 5 Rows ---")
print(df.head())

print("\n--- Descriptive Statistics ---")
print(df.describe())

print("\n--- Missing Values ---")
print(df.isnull().sum())

print("\n--- Column Names ---")
print(df.columns.tolist())

print("\n--- Data Types ---")
print(df.dtypes)
