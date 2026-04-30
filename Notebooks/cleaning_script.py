import pandas as pd
import numpy as np

df = pd.read_csv('Master_TimeSeries_Data.csv')

df['Date'] = pd.to_datetime(df['Date'])


cols_to_fix = ['Tasmax_C', 'Tasmin_C', 'Tasmean_C']
for col in cols_to_fix:
    df.loc[(df[col] < -50) | (df[col] > 60), col] = np.nan

df.loc[df['Precipitation_mm'] < 0, 'Precipitation_mm'] = 0

df = df.sort_values(by=['Region_ID', 'Date'])

def clean_group(group):
  
    group[cols_to_fix] = group[cols_to_fix].interpolate(method='linear')
    # استخدام ffill و bfill للقيم في الأطراف
    group[cols_to_fix] = group[cols_to_fix].ffill().bfill()
    return group

df = df.groupby('Region_ID', group_keys=False).apply(clean_group)

df['Temp_Range_C'] = df['Tasmax_C'] - df['Tasmin_C']

print("--- Descriptive Statistics After Cleaning ---")
print(df.describe())

df.to_csv(r'C:\Users\user\flood warnnig\cleaned_data.csv', index=False)
print("\nCleaned data saved to cleaned_data.csv")
