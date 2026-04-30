import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np

# تحميل البيانات المعالجة
df = pd.read_csv('/home/ubuntu/preprocessed_data.csv')
df['Date'] = pd.to_datetime(df['Date'])

# إعداد مظهر الرسوم البيانية
sns.set_theme(style="whitegrid")
plt.rcParams['font.family'] = 'DejaVu Sans' # استخدام خط يدعم الإنجليزية لتجنب مشاكل الخطوط العربية في البيئة الحالية

# 1. توزيع خطر الفيضانات (Flood Risk Distribution)
plt.figure(figsize=(10, 6))
sns.countplot(data=df, x='Flood_Risk', palette='viridis')
plt.title('Distribution of Flood Risk Levels (0=Safe, 1=Warning, 2=Danger)')
plt.xlabel('Risk Level')
plt.ylabel('Count')
plt.savefig('/home/ubuntu/flood_risk_distribution.png')
plt.close()

# 2. متوسط الأمطار الشهري (Seasonal Pattern)
plt.figure(figsize=(12, 6))
monthly_precip = df.groupby('Month')['Precipitation_mm'].mean().reset_index()
sns.barplot(data=monthly_precip, x='Month', y='Precipitation_mm', color='skyblue')
plt.title('Average Monthly Precipitation (Seasonal Pattern)')
plt.xlabel('Month')
plt.ylabel('Average Rainfall (mm)')
plt.savefig('/home/ubuntu/monthly_precipitation.png')
plt.close()

# 3. العلاقة بين درجة الحرارة وهطول الأمطار (Scatter Plot)
# سنأخذ عينة من البيانات للرسم لتجنب البطء (10,000 نقطة)
sample_df = df.sample(10000, random_state=42)
plt.figure(figsize=(10, 6))
sns.scatterplot(data=sample_df, x='Tasmean_C', y='Precipitation_mm', hue='Flood_Risk', alpha=0.5, palette='Set1')
plt.title('Temperature vs Precipitation (Sampled Data)')
plt.xlabel('Mean Temperature (C)')
plt.ylabel('Precipitation (mm)')
plt.savefig('/home/ubuntu/temp_vs_precip.png')
plt.close()

# 4. خريطة الحرارة للارتباط (Correlation Heatmap)
plt.figure(figsize=(12, 10))
corr = df[['Precipitation_mm', 'Precip_Lag1', 'Precip_3Days_Sum', 'Tasmean_C', 'Tasmean_Lag1', 'Flood_Risk']].corr()
sns.heatmap(corr, annot=True, cmap='coolwarm', fmt=".2f")
plt.title('Correlation Heatmap of Key Features')
plt.savefig('/home/ubuntu/correlation_heatmap.png')
plt.close()

# 5. اتجاه الأمطار السنوي (Time Series Trend)
plt.figure(figsize=(15, 6))
yearly_precip = df.groupby('Year')['Precipitation_mm'].mean().reset_index()
sns.lineplot(data=yearly_precip, x='Year', y='Precipitation_mm', marker='o')
plt.title('Yearly Average Precipitation Trend')
plt.xlabel('Year')
plt.ylabel('Average Rainfall (mm)')
plt.savefig('/home/ubuntu/yearly_trend.png')
plt.close()

print("Visualizations saved to /home/ubuntu/")
