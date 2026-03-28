# Loading and analyzing Nubank_ads_data.csv for missing, duplicate, and inconsistent values using Polars and Altair

import polars as pl
import altair as alt
import os



# Load dataset
file_path = "data/Nubank_ads_data.csv"
df = pl.read_csv(file_path)

# 1. Check for missing values
missing_values = df.null_count()

print(f"there are {missing_values}")

# 2. Identify duplicate rows
duplicate_rows = df.is_duplicated().sum()

print(f"there are {duplicate_rows}")


# 3. Check for negative values in numeric columns
numeric_columns = ["Spend (BRL)", "Impressions", "Link Clicks", "Conversions", "Reach", "Frequency"]
negative_values = {col: df.filter(pl.col(col) < 0).shape[0] for col in numeric_columns}

print(f"there are {negative_values} negative values")



descriptive_stats = df.select([
    "Spend (BRL)",
    "Impressions",
    "Link Clicks",
    "Conversions",
    "Reach",
    "Frequency"
]).describe()


# 5. Create visualizations with Altair

# Histogram of Spend
hist_spend = alt.Chart(df).mark_bar().encode(
    alt.X("Spend (BRL)", bin=alt.Bin(maxbins=50), title="Spend (BRL)"),
    y='count()'
).properties(
    title="Histogram of Spend (BRL)"
)
hist_spend

# Boxplot of Impressions
boxplot_impressions = alt.Chart(df).mark_boxplot().encode(
    y=alt.Y("Impressions", title="Impressions")
).properties(
    title="Boxplot of Impressions"
)
boxplot_impressions

# Bar chart of Delivery status
bar_delivery = alt.Chart(df).mark_bar().encode(
    x=alt.X("Delivery", type="nominal", title="Delivery Status"),
    y=alt.Y("count()", title="Number of Records")
).properties(
    title="Number of Records by Delivery Status"
)
bar_delivery

# Bar chart of Attribution Setting
bar_attribution = alt.Chart(df).mark_bar().encode(
    x=alt.X("Attribution Setting", type="nominal", title="Attribution Setting"),
    y=alt.Y("count()", title="Number of Records")
).properties(
    title="Number of Records by Attribution Setting"
)
bar_attribution

# Save charts
os.makedirs("picture/", exist_ok=True)
hist_spend.save("picture/hist_spend.html")
boxplot_impressions.save("picture/boxplot_impressions.html")
bar_delivery.save("picture/bar_delivery.html")
bar_attribution.save("picture/bar_attribution.html")






