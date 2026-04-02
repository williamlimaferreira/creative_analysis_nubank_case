import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import warnings
import polars as pl
warnings.filterwarnings('ignore')

# Load the data
file_path = "./Nubank_ads_data.csv"
df = pl.read_csv(file_path)


# Display basic information
print("Dataset Shape:", df.shape)
print("\nColumns:", list(df.columns))
print("\nFirst 3 rows:")
print(df.head(3).to_string())

# Rename columns for easier handling (remove spaces where possible)
df.columns = [col.replace(' (BRL)', '').replace(' ', '_') for col in df.columns]
print("\nRenamed Columns:", list(df.columns))

# Convert date columns to datetime
df['Reporting_Start'] = pd.to_datetime(df['Reporting_Start'])
df['Reporting_End'] = pd.to_datetime(df['Reporting_End'])

# Calculate core metrics, handling division by zero with NaN
df['CTR'] = df['Link_Clicks'] / df['Impressions']
df['CPC'] = np.where(df['Link_Clicks'] > 0, df['Spend'] / df['Link_Clicks'], np.nan)
df['CVR'] = np.where(df['Link_Clicks'] > 0, df['Conversions'] / df['Link_Clicks'], np.nan)
df['CPA'] = np.where(df['Conversions'] > 0, df['Spend'] / df['Conversions'], np.nan)
df['CPM'] = (df['Spend'] / df['Impressions']) * 1000
df['Conv_per_1k_Impressions'] = (df['Conversions'] / df['Impressions']) * 1000
df['Conv_per_1k_Reach'] = (df['Conversions'] / df['Reach']) * 1000

print("\nMetrics added. Sample metrics (first 3 rows):")
print(df[['CTR', 'CPC', 'CVR', 'CPA', 'CPM', 'Conv_per_1k_Impressions', 'Conv_per_1k_Reach']].head(3).to_string())

# Create parsed columns for Ad Set Name
df['Ad_Set_Parts'] = df['Ad_Set_Name'].astype(str).str.split('_')
all_ad_set_parts = set()
for parts in df['Ad_Set_Parts']:
    if isinstance(parts, list):
        for p in parts:
            if p and p.strip():
                all_ad_set_parts.add(p.strip())

print("\nUnique Ad Set components:", sorted(list(all_ad_set_parts)))

for part in all_ad_set_parts:
    col_name = f'ad_set_{part.replace("-", "_").replace(".", "_")}'
    df[col_name] = df['Ad_Set_Parts'].apply(lambda x: 1 if isinstance(x, list) and part in x else 0)

# Create parsed columns for Ad Name (following example: combine Nu_Brand etc.)
df['Ad_Name_Parts'] = df['Ad_Name'].astype(str).str.split('_')
all_ad_name_parts = set()
for parts in df['Ad_Name_Parts']:
    if isinstance(parts, list):
        for p in parts:
            if p and p.strip():
                all_ad_name_parts.add(p.strip())

print("\nUnique Ad Name components:", sorted(list(all_ad_name_parts)))

# For Ad Name, create columns for each part (example includes 'Nu_Brand' as special but we'll create per part; can combine later if needed)
for part in all_ad_name_parts:
    col_name = f'ad_name_{part.replace("-", "_").replace(".", "_")}'
    df[col_name] = df['Ad_Name_Parts'].apply(lambda x: 1 if isinstance(x, list) and part in x else 0)

# Note: To match example exactly for 'Nu_Brand', we can add special column if 'Nu' and 'Brand' both present
df['ad_name_Nu_Brand'] = ((df['Ad_Name'].str.contains('Nu_Brand', na=False)) | 
                          ((df['Ad_Name'].str.contains('Nu', na=False)) & (df['Ad_Name'].str.contains('Brand', na=False)))).astype(int)

print("\nParsed columns created. Example ad_set and ad_name columns:")
print(df.filter(regex='^ad_set_|^ad_name_').columns.tolist()[:20])  # first 20 for preview

# Overall summary metrics
overall_metrics = df[['Spend', 'Impressions', 'Link_Clicks', 'Conversions', 'Reach', 
                      'CTR', 'CPC', 'CVR', 'CPA', 'CPM', 
                      'Conv_per_1k_Impressions', 'Conv_per_1k_Reach']].agg(['sum', 'mean', 'median']).T
print("\nOverall Metrics Summary:")
print(overall_metrics.to_string())

# Grouped analysis by key categories
groups = ['Campaign_Type', 'Delivery', 'Attribution_Setting', 'Result_Type']

for group_col in groups:
    print(f"\n\n=== Grouped Metrics by {group_col} ===")
    grouped = df.groupby(group_col).agg({
        'Spend': 'sum',
        'Impressions': 'sum',
        'Link_Clicks': 'sum',
        'Conversions': 'sum',
        'Reach': 'sum',
        'CTR': 'mean',
        'CPC': 'mean',
        'CVR': 'mean',
        'CPA': 'mean',
        'CPM': 'mean',
        'Conv_per_1k_Impressions': 'mean',
        'Conv_per_1k_Reach': 'mean'
    }).round(4)
    print(grouped.to_string())

# Additional: ad set type example - group by one ad_set column e.g. ad_set_BR (most common)
print("\n\nExample: Metrics by ad_set_BR (1 vs 0)")
print(df.groupby('ad_set_BR').agg({
    'Spend': 'sum', 'Conversions': 'sum', 'CTR': 'mean', 'CPA': 'mean', 'CPM': 'mean'
}).round(4))

# Save cleaned df with metrics for further use if needed
df.to_csv("processed_nubank_ads.csv", index=False)
print("\nProcessed data saved to processed_nubank_ads.csv")