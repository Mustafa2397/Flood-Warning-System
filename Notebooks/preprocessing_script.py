import pandas as pd
import numpy as np

original_df = pd.read_csv('Master_TimeSeries_Data.csv', usecols=['Region_ID'])

cleaned_df = pd.read_csv('cleaned_data.csv')

df = pd.concat([original_df, cleaned_df], axis=1)

df['Date'] = pd.to_datetime(df['Date'])
df = df.sort_values(by=['Region_ID', 'Date'])

df['Precip_Lag1'] = df.groupby('Region_ID')['Precipitation_mm'].shift(1)

df['Precip_3Days_Sum'] = df.groupby('Region_ID')['Precipitation_mm'].transform(lambda x: x.rolling(window=3).sum())

df['Tasmean_Lag1'] = df.groupby('Region_ID')['Tasmean_C'].shift(1)

def calculate_flood_risk(row):
    if row['Precip_3Days_Sum'] > 50:
        return 2
    elif row['Precip_3Days_Sum'] > 20:
        return 1
    else:
        return 0

df['Flood_Risk'] = df.apply(calculate_flood_risk, axis=1)

df = df.dropna()

print("--- Flood Risk Distribution ---")
print(df['Flood_Risk'].value_counts())

df.to_csv(r'C:\Users\user\flood warnnig\preprocessed_data.csv', index=False)
print("\nPreprocessed data saved to preprocessed_data.csv")
