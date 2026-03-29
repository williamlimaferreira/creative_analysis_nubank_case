# Generating EDA metrics and interactive dashboard for Nubank Meta campaign performance
import polars as pl
import pandas as pd
import re
import altair as alt
import streamlit as st

# Load dataset
df = pl.read_csv("data/Nubank_ads_data.csv")


# Compute performance metrics
df = df.with_columns([
    (pl.col("Spend (BRL)") / pl.col("Conversions").cast(pl.Float64)).alias("CPA"),
    ((pl.col("Spend (BRL)") / pl.col("Impressions")) * 1000).alias("CPM"),
    (pl.col("Link Clicks") / pl.col("Impressions")).alias("CTR"),
    (pl.col("Impressions") / pl.col("Reach")).alias("Frequency_Calc")
])


# Extract ad set types from 'Ad Set Name'
def extract_ad_set_types(ad_set_name):
    parts = ad_set_name.split("_")
    country = parts[0]
    age = parts[1]
    message = "_".join(parts[2:])
    return country, age, message

ad_set_types = df.select("Ad Set Name").unique().to_series()
ad_set_type_cols = set()

for name in ad_set_types:
    if name is None:
        continue
    country, age, message = extract_ad_set_types(name)
    ad_set_type_cols.update([f"ad_set_type_{country}", f"ad_set_type_{age}", f"ad_set_type_{message}"])

# Add ad set type columns
for col in ad_set_type_cols:
    key = col.replace("ad_set_type_", "")
    df = df.with_columns([
        pl.col("Ad Set Name").apply(lambda x: 1 if x and key in x else 0).alias(col)
    ])

# Extract campaign type and ad type from 'Ad Name'
def extract_campaign_type(ad_name):
    if ad_name is None:
        return "Unknown"
    match = re.search(r"Brand_(\w+)", ad_name)
    return match.group(1) if match else "Unknown"

def extract_ad_type(ad_name):
    if ad_name is None:
        return "Unknown"
    if "Video" in ad_name:
        return "Video"
    elif "Carousel" in ad_name:
        return "Carousel"
    elif "Banner" in ad_name or "Static" in ad_name:
        return "Banner"
    elif "Story" in ad_name:
        return "Story"
    elif "Reel" in ad_name:
        return "Reel"
    else:
        return "Other"

df = df.with_columns([
    pl.col("Ad Name").apply(extract_campaign_type).alias("Campaign_Type"),
    pl.col("Ad Name").apply(extract_ad_type).alias("Ad_Type")
])

# Convert to pandas for Altair and Streamlit
df_pd = df.to_pandas()

# Aggregate metrics
group_cols = ["Attribution Setting", "Delivery", "Campaign_Type", "Ad_Type"]
agg_df = df_pd.groupby(group_cols).agg({
    "Spend (BRL)": "sum",
    "Impressions": "sum",
    "Link Clicks": "sum",
    "Conversions": "sum",
    "CPA": "mean",
    "CPM": "mean",
    "CTR": "mean",
    "Frequency_Calc": "mean"
}).reset_index()

# Identify 25% best and worst combinations by CPA
agg_df["CPA"] = agg_df["Spend (BRL)"] / agg_df["Conversions"].replace(0, float("nan"))
agg_df_sorted = agg_df.sort_values("CPA")
top_25 = agg_df_sorted.head(int(len(agg_df_sorted) * 0.25))
bottom_25 = agg_df_sorted.tail(int(len(agg_df_sorted) * 0.25))

# Scatter plot: Frequency vs CPA
scatter = alt.Chart(df_pd).mark_circle(size=60).encode(
    x=alt.X("Frequency_Calc", title="Frequency"),
    y=alt.Y("CPA", title="Cost per Action (BRL)"),
    color="Campaign_Type",
    tooltip=["Ad Name", "CPA", "Frequency_Calc", "Campaign_Type"]
).interactive().properties(title="Frequency vs CPA")

# Save outputs
df_pd.to_csv("/mnt/data/nubank_ads_enriched.csv", index=False)
top_25.to_csv("/mnt/data/top_25_percent_cpa.csv", index=False)
bottom_25.to_csv("/mnt/data/bottom_25_percent_cpa.csv", index=False)
scatter.save("/mnt/data/frequency_vs_cpa.html")

print("EDA completed: calculated metrics, extracted ad set and campaign types, identified top/bottom 25% CPA, and saved scatter plot and CSVs.")