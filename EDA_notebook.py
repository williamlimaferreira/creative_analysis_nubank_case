import marimo

__generated_with = "0.22.4"
app = marimo.App(width="full", auto_download=["html"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Project Description
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## load packages
    """)
    return


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import numpy as np
    import altair as alt

    return alt, mo, np, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## load dataset
    """)
    return


@app.cell
def _(pl):
    file_path = "D:\\portifolio\\python projects\\nubank_case\\nubank_MS_case\\data\\Nubank_ads_data.csv"

    df = pl.read_csv(file_path)
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Display basic information
    """)
    return


@app.cell
def _(df):
    df.head(3)
    return


@app.cell
def _(df):
    def _(df):
        print(
            f"There is {df.shape[0]} lines in the dataset and {df.shape[1]} columns"
        )


    _(df)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Data Validation Check
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Before using the data to make any decision or find an insight, it is necessary to do a data validation, where the dataset is inspected with the objective of finding any errors in it. We will verify if there is

    - Any missing value.
    - Duplicate row.
    - negative values or other types of wrong input.
    """)
    return


@app.cell
def _(df):
    def _(dataset):
        n_missing = int(dataset.is_empty())
        print(f"There are {n_missing} values in the dataset.")

    _(df)
    return


@app.cell
def _(df):
    def _(dataset):
        n_duplicated = dataset.is_duplicated().sum()
        print(f"There are {n_duplicated} duplicated rows in the dataset.")


    _(df)

    return


@app.cell
def _(df, pl):
    def _(dataset):
        numeric_columns = [
        "Spend",
        "Impressions",
        "Link_Clicks",
        "Conversions",
        "Reach",
        "Frequency",
        ]
        negative_values = {
        col: dataset.filter(pl.col(col) < 0).shape[0] for col in numeric_columns
        }

        for i in negative_values:
            print(
            f"There is {negative_values[i]} negative values in the column '{i}' "
        )

    _(df)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Our analysis did not find any arror in the dataset.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Exploratory Data Analysis(EDA)
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    The EDA !!!!
    """)
    return


@app.cell
def _(df):
    # 1. Estatísticas descritivas (mantido igual)
    def _(dataset):
        descriptive_stats = dataset.select(
        [
            "Spend",
            "Impressions",
            "Link_Clicks",
            "Conversions",
            "Reach",
            "Frequency",
        ]
        ).describe()

        return descriptive_stats.to_pandas().round(2)

    _(df)
    return


@app.cell
def _(alt, df, mo):
    def _(dataset):
    
        histogram = alt.Chart(df).mark_bar(opacity=0.7).encode(
        x=alt.X("Spend:Q", 
                bin=alt.Bin(maxbins=50), 
                title="Spend (BRL)"),
        y=alt.Y("count()", title="Count")
        ).properties(
        title="Histogram of Spend (BRL)",
        width=700,
        height=400
        )

        # Linha de densidade (KDE)
        kde = alt.Chart(df).transform_density(
        density="Spend",
        as_=["Spend", "density"]
        ).mark_line(color="red", strokeWidth=2).encode(
        x=alt.X("Spend:Q", title="Spend (BRL)"),
        y=alt.Y("density:Q", title="Density")
        )

    # Combinar os dois
        final_chart = (histogram + kde).resolve_scale(y='independent')

        return mo.ui.altair_chart(final_chart)

    _(df)
    return


@app.cell
def _(alt, df, mo):
    def _(dataset):
        chart_box = alt.Chart(dataset).mark_boxplot(
        size=50,          # largura da caixa
        opacity=0.8,
        color="steelblue"
        ).encode(
        x = alt.X("Delivery:N"),
        y=alt.Y("Impressions:Q", 
                title="Impressions",
                scale=alt.Scale(zero=False))  # permite valores negativos se existirem
    ).properties(
        title="Boxplot of Impressions",
        width=500,
        height=550
        ).configure_title(
        fontSize=16,
        anchor='start'
    )

        return mo.ui.altair_chart(chart_box)

    _(df)
    return


@app.cell
def _(alt, df, mo):
    def _(dataset):
        chart = alt.Chart(dataset).mark_bar(color="#4c78a8", opacity=0.85).encode(
        x=alt.X("Delivery:N", 
                title="Delivery Status",
                axis=alt.Axis(labelAngle=45)),
        y=alt.Y("count()", title="Number of Records"),
        tooltip=[
            alt.Tooltip("Delivery:N", title="Delivery Status"),
            alt.Tooltip("count()", title="Number of Records")
        ]
    ).properties(
        title="Number of Records by Delivery Status",
        width=650,
        height=450
    )

        return mo.ui.altair_chart(chart)

    _(df)
    return


@app.cell
def _(alt, df, mo):
    def _(dataset):
        chart_bar = alt.Chart(dataset).mark_bar(color="#4c78a8", opacity=0.85).encode(
        x=alt.X("Attribution_Setting:N", 
                title="Attribution Setting",
                axis=alt.Axis(labelAngle=45)),
        y=alt.Y("count()", title="Number of Records"),
        tooltip=[
            alt.Tooltip("Attribution Setting:N", title="Attribution Setting"),
            alt.Tooltip("count()", title="Número de Registros")
        ]
    ).properties(
        title="Number of Records by Attribution Setting",
        width=680,
        height=450
    )

        return mo.ui.altair_chart(chart_bar)

    _(df)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Rename columns for easier handling (remove spaces where possible)
    """)
    return


@app.cell
def _(df):
    df.columns = [
        col.replace(" (BRL)", "").replace(" ", "_") for col in df.columns
    ]
    print("\nRenamed Columns:", list(df.columns))
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Convert date columns to datetime
    """)
    return


@app.cell
def _():
    return


@app.cell
def _(df, pd):
    df["Reporting_Start"] = pd.to_datetime(df["Reporting_Start"])
    df["Reporting_End"] = pd.to_datetime(df["Reporting_End"])
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Calculate core metrics, handling division by zero with NaN
    """)
    return


@app.cell
def _(df, np):
    df["CTR"] = df["Link_Clicks"] / df["Impressions"]
    df["CPC"] = np.where(
        df["Link_Clicks"] > 0, df["Spend"] / df["Link_Clicks"], np.nan
    )
    df["CVR"] = np.where(
        df["Link_Clicks"] > 0, df["Conversions"] / df["Link_Clicks"], np.nan
    )
    df["CPA"] = np.where(
        df["Conversions"] > 0, df["Spend"] / df["Conversions"], np.nan
    )
    df["CPM"] = (df["Spend"] / df["Impressions"]) * 1000
    df["Conv_per_1k_Impressions"] = (df["Conversions"] / df["Impressions"]) * 1000
    df["Conv_per_1k_Reach"] = (df["Conversions"] / df["Reach"]) * 1000


    df[
        [
            "CTR",
            "CPC",
            "CVR",
            "CPA",
            "CPM",
            "Conv_per_1k_Impressions",
            "Conv_per_1k_Reach",
        ]
    ].head(3).round(2)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Create parsed columns for Ad Set Name
    """)
    return


@app.cell
def _(df):
    def _():
        df["Ad_Set_Parts"] = df["Ad_Set_Name"].astype(str).str.split("_")
        all_ad_set_parts = set()
        for parts in df["Ad_Set_Parts"]:
            if isinstance(parts, list):
                for p in parts:
                    if p and p.strip():
                        all_ad_set_parts.add(p.strip())

        print("\nUnique Ad Set components:", sorted(list(all_ad_set_parts)))

        for part in all_ad_set_parts:
            col_name = f"ad_set_{part.replace('-', '_').replace('.', '_')}"
            df[col_name] = df["Ad_Set_Parts"].apply(
                lambda x: 1 if isinstance(x, list) and part in x else 0
            )

        # Create parsed columns for Ad Name (following example: combine Nu_Brand etc.)
        df["Ad_Name_Parts"] = df["Ad_Name"].astype(str).str.split("_")
        all_ad_name_parts = set()
        for parts in df["Ad_Name_Parts"]:
            if isinstance(parts, list):
                for p in parts:
                    if p and p.strip():
                        all_ad_name_parts.add(p.strip())

        print("\nUnique Ad Name components:", sorted(list(all_ad_name_parts)))

        return all_ad_name_parts


    all_ad_name_parts = _()
    return (all_ad_name_parts,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## For Ad Name, create columns for each part (example includes 'Nu_Brand' as special but we'll create per part; can combine later if needed)
    """)
    return


@app.cell
def _(all_ad_name_parts, df):
    for part in all_ad_name_parts:
        col_name = f"ad_name_{part.replace('-', '_').replace('.', '_')}"
        df[col_name] = df["Ad_Name_Parts"].apply(
            lambda x: 1 if isinstance(x, list) and part in x else 0
        )

    # Note: To match example exactly for 'Nu_Brand', we can add special column if 'Nu' and 'Brand' both present

    df["ad_name_Nu_Brand"] = (
        (df["Ad_Name"].str.contains("Nu_Brand", na=False))
        | (
            (df["Ad_Name"].str.contains("Nu", na=False))
            & (df["Ad_Name"].str.contains("Brand", na=False))
        )
    ).astype(int)

    print("\nParsed columns created. Example ad_set and ad_name columns:")
    print(
        df.filter(regex="^ad_set_|^ad_name_").columns.tolist()[:20]
    )  # first 20 for preview

    # Overall summary metrics
    overall_metrics = (
        df[
            [
                "Spend",
                "Impressions",
                "Link_Clicks",
                "Conversions",
                "Reach",
                "CTR",
                "CPC",
                "CVR",
                "CPA",
                "CPM",
                "Conv_per_1k_Impressions",
                "Conv_per_1k_Reach",
            ]
        ]
        .agg(["sum", "mean", "median"])
        .T
    )
    print("\nOverall Metrics Summary:")
    print(overall_metrics.to_string())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Grouped analysis by key categories
    """)
    return


@app.cell
def _(df):
    groups = ["Campaign_Type", "Delivery", "Attribution_Setting", "Result_Type"]


    for group_col in groups:
        print(f"\n\n=== Grouped Metrics by {group_col} ===")
        grouped = (
            df.groupby(group_col)
            .agg(
                {
                    "Spend": "sum",
                    "Impressions": "sum",
                    "Link_Clicks": "sum",
                    "Conversions": "sum",
                    "Reach": "sum",
                    "CTR": "mean",
                    "CPC": "mean",
                    "CVR": "mean",
                    "CPA": "mean",
                    "CPM": "mean",
                    "Conv_per_1k_Impressions": "mean",
                    "Conv_per_1k_Reach": "mean",
                }
            )
            .round(4)
        )
        print(grouped.to_string())
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Additional: ad set type example - group by one ad_set column e.g. ad_set_BR (most common)
    """)
    return


@app.cell
def _(df):
    df.groupby("ad_set_BR").agg(
        {
            "Spend": "sum",
            "Conversions": "sum",
            "CTR": "mean",
            "CPA": "mean",
            "CPM": "mean",
        }
    ).round(4)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Save cleaned df with metrics for further use if needed
    """)
    return


@app.cell
def _():
    # df.to_csv("data\\processed_nubank_ads.csv", index=False)
    # print("\nProcessed data saved to processed_nubank_ads.csv")
    return


if __name__ == "__main__":
    app.run()
