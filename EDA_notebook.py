# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.1",
# ]
# ///

import marimo

__generated_with = "0.23.8"
app = marimo.App(width="full", auto_download=["html"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Contexto do Case
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Você foi contratado como **Digital Marketing Analyst** do Nubank para analisar campanhas rodadas no Meta Ads durante o Q1. 1.

    O Nubank deseja acelerar a **abertura de contas digitais** utilizando Meta Ads (Facebook, Instagram e Audience Network). A operação já está rodando há alguns meses, com campanhas ativas em diferentes objetivos.

    O time interno percebeu crescimento em volume, mas não tem clareza sobre a eficiência real do investimento, nem sobre o impacto incremental das campanhas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Objetivos Do Trabalho
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Temos como objetivo principal do trabalho encontrar quais características das campanhas e ads apresentam o melhor desempenho. Essa não é uma tarefa fácil, pois precisamos não só realizar uma boa análise dos dados históricos, mas também compreender os objetivos estratégicos da empresa para otimizar as métricas adequadas. O conjunto é uma simulação que traz informações sobre campanhas do Nubank no Meta (Facebook, Instagram e Audience Network) com o objetivo de incentivar a abertura de novas contas no primeiro quatrimestre.

    Desta forma, devemos começar o nosso trabalho com a validação dos dados, em seguida, realizar uma análise exploratória deles e ,por fim, testar as hipóteses, produzidas na etapa anterior, e criar modelos capazes de prever o resultado das novas campanhas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Pacotes Usados
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    O pacotes usados nesse trabalho são:

    ---

    ## 📦

    - **pandas**: Biblioteca para análise e manipulação de dados em tabelas (*DataFrames*).
    - **polars**: Alternativa moderna ao pandas, otimizada para velocidade e uso eficiente de memória.
    - **numpy**: Ferramenta para cálculos numéricos e manipulação de arrays multidimensionais.
    - **pyarrow**: Suporte para o formato Apache Arrow, usado em processamento de dados em memória.

    ### Estatística e Machine Learning
    - **statsmodels**: Biblioteca para modelagem estatística, regressões e testes de hipóteses.
    - **scikit-learn (sklearn)**: Conjunto de algoritmos de machine learning e ferramentas de pré-processamento.

    ### Visualização de dados
    - **altair**: Biblioteca declarativa para criação de gráficos interativos e estatísticos.
    - **plotly**: Interface simples para gerar gráficos interativos rapidamente.

    ### Ferramentas adicionais
    - **marimo**: Framework para criar notebooks interativos e aplicações de dados em Python.

    ---
    """)
    return


@app.cell
def _():
    # Bibliotecas de manipulação de dados
    import pandas as pd
    import polars as pl
    import numpy as np
    import pyarrow

    # Bibliotecas de modelagem estatística e machine learning
    import statsmodels.formula.api as smf
    from sklearn.linear_model import LinearRegression

    # Visualização de dados
    import altair as alt
    import plotly.express as px
    import plotly.graph_objects as go
    from plotly.subplots import make_subplots

    # Ferramentas adicionais
    import marimo as mo


    # alt.data_transformers.enable("vegafusion")

    # import asyncio
    # import sys

    # if sys.platform == "win32":
    #     asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    return LinearRegression, alt, mo, pl, px, smf


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Dataset
    """)
    return


@app.cell
def _(pl):
    file_path = "D:\\portifolio\\python projects\\nubank_case\\nubank_MS_case\\data\\Nubank_ads_data.parquet"

    # df = pl.read_csv(file_path)
    df = pl.read_parquet(file_path)
    return (df,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    O dataset tem as seguintes colunas

    - **Reporting Start**: Data de início do período de relatório da campanha.
    - **Reporting End**: Data de término do período de relatório da campanha.
    - **Campaign Name**: Nome da campanha publicitária (inclui objetivo e trimestre).
    - **Campaign Type**: Tipo da campanha (ex.: Branding, Consideration).
    - **Ad Set Name**: Nome do conjunto de anúncios (segmentação de público).
    - **Ad Name**: Nome específico do anúncio veiculado.
    - **Delivery**: Status de entrega do anúncio (ex.: Active, Learning, Not Delivering).
    - **Attribution Setting**: Configuração de atribuição usada (ex.: 1-day click).
    - **Result Type**: Tipo de resultado esperado (ex.: Account Opening).
    - **Spend (BRL)**: Valor gasto em reais (BRL) na campanha.
    - **Impressions**: Número de vezes que o anúncio foi exibido.
    - **Link Clicks**: Quantidade de cliques no link do anúncio.
    - **Conversions**: Número de conversões atribuídas (ex.: abertura de conta).
    - **Reach**: Número de pessoas únicas alcançadas pelo anúncio.
    - **Frequency**: Frequência média de exibição do anúncio por pessoa.

    e 610 linhas. Com as informações contidas nele podemos realizar uma análise completa sobre o desempenho das campanhas, mas antes de iniciar qualquer investigação necessitamos verificar a qualidade dos dados.
    """)
    return


@app.cell
def _(df):
    df.head(3)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Validação Dos Dados
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A validação buscar encontrar erros no dataset, no nosso caso eles são

    - Valores ausentes.

    - Linhas duplicadas.

    - Valores negativos ou outros tipos de entrada incorreta.

    Assim, executando a análise, temos que
    """)
    return


@app.cell(hide_code=True)
def _(df, mo):
    def _(dataset):
        n_missing = dataset.null_count().sum_horizontal()

        if sum(n_missing) > 0:
            return mo.md(f"Existem {n_missing} valores faltantes no dataset.")
        else:
            return mo.md(f"Não há valores faltantes no dataset.")


    _(df)
    return


@app.cell
def _(df, mo):
    def _(dataset):
        n_duplicated = dataset.is_duplicated().sum()

        if n_duplicated > 0:
            return mo.md(f"Existem {n_duplicated} linhas duplicadas no dataset.")
        else:
            return mo.md(f"Não há {n_duplicated} linhas duplicadas no dataset.")


    _(df)
    return


@app.cell(hide_code=True)
def _(df, mo, pl):
    def _(dataset):
        numeric_columns = [
            "Spend (BRL)",
            "Impressions",
            "Link Clicks",
            "Conversions",
            "Reach",
            "Frequency",
        ]

        messages = [
            mo.md(
                f"⚠️ Existem **{dataset.filter(pl.col(col) < 0).shape[0]}** valores negativos na coluna **'{col}'**."
            )
            for col in numeric_columns
            if dataset.filter(pl.col(col) < 0).shape[0] > 0
        ]

        if not messages:
            return mo.md(
                "Não foram encontrados valores negativos nas colunas numéricas."
            )

        return mo.vstack(messages)


    _(df)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Resultados
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Verifico-se que no dataset

    ✅ Não há valores faltantes no dataset.

    ✅ Não há linhas repetidas no dataset.

    ✅ Não há valores negativos no dataset.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Criação De Novas Features
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    O conjunto de dados traz uma série de informações úteis sobre o desempenho das campanhas, mas podemos torná-lo mais rico ao construir novas features com base nas já existentes. As novas features são:

    - CTR = Link Clicks / Impressions

    - CPC = Spend / Link Clicks

    - CVR (Click → Conversion) = Conversions / Link Clicks

    - CPA = Spend / Conversions

    - CPM = (Spend / Impressions) × 1000

    - Conversões por 1.000 impressões

    - Conversões por 1.000 pessoas alcançadas

    Que têm como objetivo facilitar o estudo da performance das campanhas. Além dessas novas métricas, também serão criadas novas colunas com as informações contidas no "Ad Set Name" e "Ad Set Name", por exemplo, no caso, ad set name "**BR_18-24_Students**" serão criadas duas novas colunas,

    - ad_name_18-24
    - ad_name_students

    Cada uma contendo o valor 1, que representa as características do ad set e do ad.
    """)
    return


@app.cell(hide_code=True)
def _(df, pl):
    def parse_components(dataset: pl.DataFrame, column: str, prefix: str):
        # Cria lista de partes
        dataset = dataset.with_columns(
            pl.col(column).cast(pl.Utf8).str.split("_").alias(f"{column}_Parts")
        )

        # Pega todas as partes únicas
        all_parts = (
            dataset.select(f"{column}_Parts")
            .explode(f"{column}_Parts")
            .filter(
                pl.col(f"{column}_Parts").is_not_null()
                & (pl.col(f"{column}_Parts").str.strip_chars().str.len_chars() > 0)
            )
            .unique()
            .to_series()
            .to_list()
        )

        # Cria colunas dummy
        expressions = []
        for part in all_parts:
            clean_part = part.replace("-", "_").replace(".", "_")
            col_name = f"{prefix}_{clean_part}"

            expressions.append(
                pl.col(f"{column}_Parts")
                .list.contains(part)
                .cast(pl.Int8)
                .alias(col_name)
            )

        dataset = dataset.with_columns(expressions)
        return dataset, all_parts


    def _(
        dataset: pl.DataFrame, function_unused
    ):  # Removi a necessidade de passar a função se não for usá-la internamente de outra forma

        # 1. Limpeza dos nomes das colunas
        # Usando mapping para renomear de uma vez
        rename_map = {
            col: col.replace(" (BRL)", "").replace(" ", "_")
            for col in dataset.columns
        }
        dataset = dataset.rename(rename_map)

        # 2. Criação das métricas principais
        dataset = dataset.with_columns(
            [
                (pl.col("Link_Clicks") / pl.col("Impressions")).alias("CTR"),
                pl.when(pl.col("Link_Clicks") > 0)
                .then(pl.col("Spend") / pl.col("Link_Clicks"))
                .otherwise(None)
                .alias("CPC"),
                pl.when(pl.col("Link_Clicks") > 0)
                .then(pl.col("Conversions") / pl.col("Link_Clicks"))
                .otherwise(None)
                .alias("CVR"),
                pl.when(pl.col("Conversions") > 0)
                .then(pl.col("Spend") / pl.col("Conversions"))
                .otherwise(None)
                .alias("CPA"),
                ((pl.col("Spend") / pl.col("Impressions")) * 1000).alias("CPM"),
                ((pl.col("Conversions") / pl.col("Impressions")) * 1000).alias(
                    "Conv_per_1k_Impressions"
                ),
                ((pl.col("Conversions") / pl.col("Reach")) * 1000).alias(
                    "Conv_per_1k_Reach"
                ),
            ]
        )

        # Aplicando nos nomes (usando os novos nomes com underscore)
        dataset, all_ad_set_parts = parse_components(
            dataset, "Ad_Set_Name", "ad_set"
        )
        dataset, all_ad_name_parts = parse_components(
            dataset, "Ad_Name", "ad_name"
        )

        dataset = dataset.with_columns(
            pl.col("Reporting_Start").str.to_date().alias("Reporting_Start"),
            pl.col("Reporting_End").str.to_date().alias("Reporting_End"),
        )

        # Coluna especial Nu_Brand
        dataset = dataset.with_columns(
            (
                pl.col("Ad_Name").str.contains("Nu_Brand", literal=True)
                | (
                    pl.col("Ad_Name").str.contains("Nu", literal=True)
                    & pl.col("Ad_Name").str.contains("Brand", literal=True)
                )
            )
            .cast(pl.Int8)
            .alias("ad_name_Nu_Brand")
        )

        # ============================
        # Resumo geral das métricas
        # ============================

        metrics_cols = [
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

        overall_metrics = (
            dataset.select(metrics_cols)
            .select(
                [
                    pl.col("*").sum().name.prefix("sum_"),
                    pl.col("*").mean().name.prefix("mean_"),
                    pl.col("*").median().name.prefix("median_"),
                ]
            )
            .unpivot(variable_name="metric_full", value_name="value")
            .with_columns(
                [
                    pl.col("metric_full")
                    .str.extract(r"^(sum|mean|median)")
                    .alias("statistic"),
                    pl.col("metric_full")
                    .str.replace(r"^(sum|mean|median)_", "")
                    .alias("metric"),
                ]
            )
            .select(["metric", "statistic", "value"])  # Organiza as colunas
        )

        return dataset


    df_new = _(df, parse_components)
    return (df_new,)


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Análise Exploratária Dos Dados
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Antes de tomar qualquer decisão ou construir um modelo, é fundamental realizar uma análise exploratória dos dados. Essa etapa tem como objetivo principal aprofundar o conhecimento sobre o conjunto disponível e validar hipóteses já existentes.

    Como o propósito do trabalho é identificar quais campanhas apresentam melhor performance, esse será o nosso foco. O primeiro passo, portanto, consiste em definir as métricas que traduzem o desempenho de uma campanha.

    O Nubank busca acelerar o número de contas abertas. À primeira vista, seria natural avaliar a performance das campanhas apenas por esse indicador. No entanto, essa visão é limitada, pois não considera os custos envolvidos para consegui-los, nem o valor que esses clientes trarão ao longo do tempo.

    Para capturar a performance real da campanha, precisamos de quatro métricas principais: **CPA**, **LTV**, **conversions per 1k impressions** e **reach**. Onde

    - Custo por Aquisição(**CPA**): informa o custo do Nubank para adquirir o cliente.
    - Lifetime value(**LTV**): informa o retorno que o cliente vai trazer ao longo de toda a sua "vida".
    - **conversions per 1k impressions**: indica o quanto a campanha foi eficiente em estimular as pessoas que a visualizaram a abrir uma conta.
    **conversions per 1k reach**: indica o quanto a campanha foi eficiente em estimular as pessoas a abrirem uma conta.

    e os indicadores de qualidade da campanha, são

    - geram o maior número de contas abertas por 1.000 impressões (reach);
    - apresentam a melhor relação \(\frac{LTV}{CPA}\), ou seja, maior valor de vida útil por custo de aquisição.

    Porém como não é possível calcular o **LTV** com os dados a que temos acesso, temos que minimizar o **CPA** para maximizar o segundo indicado.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Desempenho Agregado Das Campanhas
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Começamos a análise com o estudo dos tipos de campanhas, que são

    - **Branding**: voltado para aumentar o reconhecimento da marca e reforçar sua mensagem.
    - **E-commerce (D&R)**: focado exclusivamente em gerar uma ação específica — no nosso caso, a abertura de conta.

    Onde as métricas **CTR, CPC, CVR, CPA e CPM** serão comparadas entre os dois grupos, com o objetivo de identificar qual tipo de anúncio apresenta melhor desempenho. No histograma do **CPR**, temos
    """)
    return


@app.cell(hide_code=True)
def _(alt, df_new, mo, pl):
    def CTR_histograma(dataset: pl.DataFrame):
        chart = (
            alt.Chart(dataset)
            .mark_bar()
            .transform_joinaggregate(total="count()")
            .transform_calculate(pct="1 / datum.total")
            .encode(
                x=alt.X("CTR", bin=alt.Bin(maxbins=20), title="CTR"),
                y=alt.Y(
                    "sum(pct):Q",
                    axis=alt.Axis(format="%"),
                    title="Frequência Relativa",
                ),
                color=alt.Color("Campaign_Type:N", title="Tipo De Campanha"),
            )
            .properties(title="Histograma CTR (Frequência)", height=300, width=800)
        )
        return mo.ui.altair_chart(chart)


    CTR_histograma(df_new)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    que campanhas do tipo E-commerce producem mais clicks. Já no caso do CPC, CVR, CPA e CPM, temos
    """)
    return


@app.cell(hide_code=True)
def _(alt, df_new, mo, pl):
    def gerar_dashboard_marketing_frequencia(dataset: pl.DataFrame):
        df_processado = dataset

        width = 320
        height = 200

        metricas = ["CPC", "CVR", "CPA", "CPM"]
        charts = []

        for metrica in metricas:
            chart = (
                alt.Chart(df_processado)
                .mark_bar(opacity=0.7)
                .transform_joinaggregate(total="count()")
                .transform_calculate(pct="1 / datum.total")
                .encode(
                    x=alt.X(
                        f"{metrica}:Q", bin=alt.Bin(maxbins=20), title=metrica
                    ),
                    y=alt.Y(
                        "sum(pct):Q",
                        axis=alt.Axis(format="%"),
                        title="Frequência Relativa",
                    ),
                    color=alt.Color("Campaign_Type:N", title="Tipo de Campanha"),
                    tooltip=[
                        alt.Tooltip("Campaign_Type:N"),
                        alt.Tooltip("sum(pct):Q", format=".2%", title="Proporção"),
                    ],
                )
                .properties(
                    width=width, height=height, title=f"Distribuição de {metrica}"
                )
            )
            charts.append(chart)

        matriz_final = (
            alt.vconcat(
                alt.hconcat(charts[0], charts[1]),
                alt.hconcat(charts[2], charts[3]),
            )
            .properties(
                title=alt.TitleParams(
                    text="Análise de Frequência Relativa por Métrica",
                    fontSize=18,
                    anchor="middle",
                ),
            )
            .resolve_scale(color="shared")
        )

        return mo.ui.altair_chart(matriz_final)


    gerar_dashboard_marketing_frequencia(df_new)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Novamente as campanhas do tipo E-commerce se mostraram superiores, em especial na comparação do **CPA**, onde há uma clara diferença entre as duas. Estudando a relação entre o **CPA** e frequência, temos
    """)
    return


@app.cell(hide_code=True)
def _(alt, df_new, mo, pl):
    def _(dataset: pl.DataFrame):
        # calcular média e desvio padrão
        mean_cpa = dataset["CPA"].mean()
        std_cpa = dataset["CPA"].std()
        y_min = mean_cpa - 2 * std_cpa
        y_max = mean_cpa + 2 * std_cpa

        mean_cpa_branding = dataset.filter(pl.col("Campaign_Type") == "Branding")[
            "CPA"
        ].mean()
        std_cpa_branding = dataset.filter(pl.col("Campaign_Type") == "Branding")[
            "CPA"
        ].std()
        y_min_branding = mean_cpa_branding - 2 * std_cpa_branding
        y_max_branding = mean_cpa_branding + 2 * std_cpa_branding

        mean_cpa_dr = dataset.filter(pl.col("Campaign_Type") == "E-commerce")[
            "CPA"
        ].mean()
        std_cpa_dr = dataset.filter(pl.col("Campaign_Type") == "E-commerce")[
            "CPA"
        ].std()
        y_min_dr = mean_cpa_dr - 2 * std_cpa_dr
        y_max_dr = mean_cpa_dr + 2 * std_cpa_dr

        # gráfico original
        chart_all = (
            alt.Chart(dataset)
            .mark_line()
            .encode(
                x=alt.X("Frequency:Q", title="frequência"),
                y=alt.Y(
                    "mean(CPA):Q",
                    title="CPA médio",
                ),
            )
            .properties(width=800, height=130, title="Frequência vs CPA")
        )

        # gráfico para Branding
        chart_branding = (
            alt.Chart(dataset.filter(pl.col("Campaign_Type") == "Branding"))
            .mark_line(color="blue")
            .encode(
                x=alt.X("Frequency:Q", title="frequência"),
                y=alt.Y(
                    "mean(CPA):Q",
                    title="CPA médio",
                    scale=alt.Scale(domain=(y_min_branding, y_max_branding)),
                ),
            )
            .properties(width=410, height=130, title="Branding")
        )

        # gráfico para E-commerce
        chart_ecommerce = (
            alt.Chart(dataset.filter(pl.col("Campaign_Type") == "E-commerce"))
            .mark_line(color="green")
            .encode(
                x=alt.X("Frequency:Q", title="frequência"),
                y=alt.Y(
                    "mean(CPA):Q",
                    title="CPA médio",
                    scale=alt.Scale(domain=(y_min_dr, y_max_dr)),
                ),
            )
            .properties(width=410, height=130, title="E-commerce")
        )

        # organizar os gráficos
        combined = alt.vconcat(
            chart_all, alt.hconcat(chart_branding, chart_ecommerce)
        )

        return mo.ui.altair_chart(combined)


    _(df_new)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Vemos que o **CPA** permanece constante conforme a frequência varia, no intervalo, para ambos os tipos de campanhas e que campanhas do tipo E-commerce possuem **CPA** menor que as de braiding em qualquer frequência. Juntando as informações, conclui-se que

    - As campanhas de D&R são superiores em todas as métricas analisadas, em especial no caso do **CPA**
    - Não há frequência de saturação no intervalo observado para ambos os tipos de campanha.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Performace Por 1k De impressões e Reaches
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A análise inicial já indica que as campanhas de D&R apresentam desempenho superior em relação às de branding. No entanto, ainda é necessário aprofundar o estudo nas métricas de volume e nos modelos de atribuição para tomar uma decisão definitiva. Ao avaliar os resultados pelas métricas de volume e pelos diferentes modelos de atribuição, observamos
    """)
    return


@app.cell(hide_code=True)
def _(alt, df_new, mo, pl):
    def gerar_dashboard_marketing_impressions(dataset: pl.DataFrame):
        df_processado = dataset

        # Configuração de tamanho padrão para os subgráficos
        width = 390
        height = 130

        # Gráfico 1: Linhas - Duração vs Conversões
        chart1 = (
            alt.Chart(df_processado)
            .mark_line(smooth=True)
            .encode(
                x=alt.X("Reporting_End:T", title=""),
                y=alt.Y(
                    "mean(Conv_per_1k_Impressions):Q",
                    title="Conversões por 1k Impressões",
                ),
                color=alt.Color("Campaign_Type:N", title="Tipo de Campanha"),
                tooltip=["mean(Conv_per_1k_Impressions)"],
            )
            .properties(width=width, height=height, title="Desempenho por Duração")
        )

        # Gráfico 2: Boxplot - Tipo de Campanha vs Conversões
        chart2 = (
            alt.Chart(df_processado)
            .mark_boxplot()
            .encode(
                x=alt.X(
                    "Campaign_Type:N", title="", axis=alt.Axis(labelAngle=-55)
                ),
                y=alt.Y("Conv_per_1k_Impressions:Q", title=""),
                color=alt.Color("Campaign_Type:N", legend=True),
            )
            .properties(width=width, height=height, title="Distribuição por Tipo")
        )

        # Gráfico 3: Boxplot - Modelo de Atribuição vs Conversões
        chart3 = (
            alt.Chart(df_processado)
            .mark_boxplot()
            .encode(
                x=alt.X(
                    "Attribution_Setting:N",
                    title="",
                    axis=alt.Axis(labelAngle=-70),
                ),
                y=alt.Y(
                    "Conv_per_1k_Impressions:Q",
                    title="Conversões por 1k Impressões",
                ),
                color=alt.Color("Attribution_Setting:N", legend=None),
            )
            .properties(width=width, height=height, title="Impacto da Atribuição")
        )

        # Gráfico 4: Linhas - Frequência vs Conversões
        chart4 = (
            alt.Chart(df_processado)
            .mark_line()
            .encode(
                x=alt.X("Frequency:Q", title=""),
                y=alt.Y("mean(Conv_per_1k_Impressions):Q", title=""),
                color=alt.Color("Campaign_Type:N", title="Tipo de Campanha"),
                tooltip=["Frequency", "mean(Conv_per_1k_Impressions)"],
            )
            .properties(
                width=width, height=height, title="Frequência vs. Performance."
            )
        )

        # Agrupando em matriz 2x2
        matriz_final = (
            alt.vconcat(alt.hconcat(chart1, chart4), alt.hconcat(chart3, chart2))
            .properties(
                title=alt.TitleParams(
                    text="Análise de Campanhas Meta Ads",
                    fontSize=18,
                    anchor="middle",
                ),
            )
            .resolve_scale(color="independent")
        )

        return mo.ui.altair_chart(matriz_final)


    # Exemplo de uso no marimo:
    gerar_dashboard_marketing_impressions(df_new)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A análise dos gráficos mostra que as campanhas com o modelo de atribuição *7-day click, 1-day view* apresentam melhor desempenho. Resultado já esperado, uma vez que a janela de atribuição é significativamente maior do que a utilizada pelo concorrente. Também era previsível que as campanhas de D&R superassem as de branding.

    No entanto, observa-se que a performance de ambos os tipos de campanha não demonstra qualquer tendência consistente ao longo do tempo. Além disso, não há correlação entre a frequência e as conversões por mil impressões. Já ao avaliar os resultados por mil *reaches*, verificamos que
    """)
    return


@app.cell(hide_code=True)
def _(alt, df_new, mo, pl):
    def gerar_dashboard_marketing_reach(dataset: pl.DataFrame):
        df_processado = dataset

        # Configuração de tamanho padrão para os subgráficos
        width = 390
        height = 130

        # Gráfico 1: Linhas - Duração vs Conversões
        chart1 = (
            alt.Chart(df_processado)
            .mark_line(smooth=True)
            .encode(
                x=alt.X("Reporting_End:T", title=""),
                y=alt.Y(
                    "mean(Conv_per_1k_Reach):Q",
                    title="Conversões por 1k Reach",
                ),
                color=alt.Color("Campaign_Type:N", title="Tipo de Campanha"),
                tooltip=["mean(Conv_per_1k_Reach)"],
            )
            .properties(width=width, height=height, title="Desempenho por Duração")
        )

        # Gráfico 2: Boxplot - Tipo de Campanha vs Conversões
        chart2 = (
            alt.Chart(df_processado)
            .mark_boxplot()
            .encode(
                x=alt.X(
                    "Campaign_Type:N", title="", axis=alt.Axis(labelAngle=-45)
                ),
                y=alt.Y("Conv_per_1k_Reach:Q", title=""),
                color=alt.Color("Campaign_Type:N", legend=True),
            )
            .properties(width=width, height=height, title="Distribuição por Tipo")
        )

        # Gráfico 3: Boxplot - Modelo de Atribuição vs Conversões
        chart3 = (
            alt.Chart(df_processado)
            .mark_boxplot()
            .encode(
                x=alt.X(
                    "Attribution_Setting:N",
                    title="",
                    axis=alt.Axis(labelAngle=-70),
                ),
                y=alt.Y(
                    "Conv_per_1k_Reach:Q",
                    title="Conversões por 1k Reach",
                ),
                color=alt.Color("Attribution_Setting:N", legend=None),
            )
            .properties(width=width, height=height, title="Impacto da Atribuição")
        )

        # Gráfico 4: Linhas - Frequência vs Conversões
        chart4 = (
            alt.Chart(df_processado)
            .mark_line(smooth=True)
            .encode(
                x=alt.X("Frequency:Q", title=""),
                y=alt.Y("mean(Conv_per_1k_Reach):Q", title=""),
                color=alt.Color("Campaign_Type:N", title="Tipo de Campanha"),
                tooltip=["Frequency", "mean(Conv_per_1k_Reach)"],
            )
            .properties(
                width=width, height=height, title="Frequência vs. Performance."
            )
        )

        # Agrupando em matriz 2x2
        matriz_final = (
            alt.vconcat(alt.hconcat(chart1, chart4), alt.hconcat(chart3, chart2))
            .properties(
                title=alt.TitleParams(
                    text="Análise de Campanhas Meta Ads",
                    fontSize=18,
                    anchor="middle",
                ),
            )
            .resolve_scale(color="independent")
        )

        return mo.ui.altair_chart(matriz_final)


    gerar_dashboard_marketing_reach(df_new)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Que os resultados permanecem identicos, com novamente as campanhas de D&R tendo melhor perfomace em todos os paramêntros
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Resultados
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A primeira parte da análise exploratória já trouxe um resultado claro: a superioridade das campanhas D&R sobre Branding em todas as métricas. Desta forma, o primeiro insight é fazer uso apenas de campanhas D&R para maximizar o volume de contas abertas com o menor custo. Com a exploração no nível de campanha encerrada, seguimos para o nível dos ads set e ads.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Análise De AD Sets
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Na análise dos ad sets buscamos encontrar quais características reduzem/aumenta o CPA da campanha. Pelos gráficos abaixo, vemos
    """)
    return


@app.cell(hide_code=True)
def _(alt, df_new, mo, pl):
    def _(dataset: pl.DataFrame):

        columns_names = dataset.select(pl.col("^.*ad_set_.*$")).columns

        dataset_diff = pl.DataFrame()

        for nome in columns_names:
            n = (
                dataset.filter(pl.col("Campaign_Type") == "E-commerce")
                .group_by(nome)
                .agg(pl.col("CPA").mean().alias("CPA_mean"))
                .sort(nome, descending=False)
                .with_columns(pl.col("CPA_mean").diff())
                .filter(pl.col(nome) == 1)
            )

            n = n.rename({nome: "ad_set"}).with_columns(
                pl.lit(nome).alias("ad_set")
            )

            dataset_diff = pl.concat([dataset_diff, n])

        width = 400
        hight = 200

        dataset_diff_top = dataset_diff.top_k(5, by="CPA_mean")
        dataset_diff_bottom = dataset_diff.bottom_k(5, by="CPA_mean")

        chart_top = (
            alt.Chart(dataset_diff_top)
            .mark_bar(color="red")
            .encode(
                x=alt.X("ad_set", title=""), y=alt.Y("CPA_mean", title="Mean CPA")
            )
            .properties(width=width, hight=hight)
        )

        chart_bottom = (
            alt.Chart(dataset_diff_bottom)
            .mark_bar(color="green")
            .encode(
                x=alt.X("ad_set", title=""), y=alt.Y("CPA_mean", title="Mean CPA")
            )
            .properties(width=width, hight=hight)
        )

        chart = chart_top | chart_bottom

        return mo.ui.altair_chart(
            chart, label="Melhores/Piores Atributos Do AD Set"
        )


    _(df_new)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Que as propriedades do ad set não possuem grande influência no CPA, o que não reduz a importância da análise, pois a otimização de uma campanha se dá por meio de pequenos passos. Sendo as características que aumentam o **CPA**:

    - campanhas lookalike
    - High internet
    - voltada para o público 25-34

      que têm em média um **CPA** $5$ reais mais alto. Já aquelas que mais reduzem, são:

    - voltadas para os públicos 18-24 ou 18-44
    - foca em usuários de celular
    - trazer usuários dos concorrentes.

    com um **CPA** médio de $3$ reais menor. Olhando para o 25% top quartil e o inferior, temos
    """)
    return


@app.cell(hide_code=True)
def _(df_new, mo, pl):
    def gerar_ui_dashboard(dataset: pl.DataFrame):
        columns_names = dataset.select(pl.col("^.*ad_set_.*$")).columns

        dataset_diff = pl.DataFrame()

        for nome in columns_names:
            n = (
                dataset.filter(pl.col("Campaign_Type") == "E-commerce")
                .group_by(nome)
                .agg(pl.col("CPA").mean().alias("CPA_mean"))
                .sort(nome, descending=False)
                .with_columns(pl.col("CPA_mean").diff())
                .filter(pl.col(nome) == 1)
            )

            n = n.rename({nome: "ad_set"}).with_columns(
                pl.lit(nome).alias("ad_set")
            )

            dataset_diff = pl.concat([dataset_diff, n])

        # calcular quartis
        q25 = dataset_diff["CPA_mean"].quantile(0.25)
        q75 = dataset_diff["CPA_mean"].quantile(0.75)

        # filtrar quartil inferior e superior
        bottom_25 = dataset_diff.filter(pl.col("CPA_mean") <= q25)[
            "ad_set"
        ].to_list()
        top_25 = dataset_diff.filter(pl.col("CPA_mean") >= q75)["ad_set"].to_list()

        # Garante que os dados sejam strings e limpa as listas
        top_list = [str(item) for item in top_25]
        bottom_list = [str(item) for item in bottom_25]

        # Criando os itens HTML com segurança
        top_items_html = "".join(
            [
                f"<li style='padding: 8px 0; border-bottom: 1px solid #b2f5ea;'>✅ {item}</li>"
                for item in top_list
            ]
        )
        bottom_items_html = "".join(
            [
                f"<li style='padding: 8px 0; border-bottom: 1px solid #fed7d7;'>⚠️ {item}</li>"
                for item in bottom_list
            ]
        )

        ui_dashboard = mo.hstack(
            [
                mo.vstack(
                    [
                        mo.md("## 🚀 Top 25% Quartil"),
                        mo.Html(f"""
                <div style='background-color: #e6fffa; border-left: 5px solid #38b2ac; padding: 20px; border-radius: 8px; min-width: 300px;'>
                    <ul style='list-style-type: none; padding: 0; margin: 0; color: #2c7a7b;'>
                        {top_items_html if top_list else "<li>Nenhum dado encontrado</li>"}
                    </ul>
                </div>
                """),
                    ]
                ),
                mo.vstack(
                    [
                        mo.md("## 📉 Bottom 25% Quartil"),
                        mo.Html(f"""
                <div style='background-color: #fff5f5; border-left: 5px solid #f56565; padding: 20px; border-radius: 8px; min-width: 300px;'>
                    <ul style='list-style-type: none; padding: 0; margin: 0; color: #c53030;'>
                        {bottom_items_html if bottom_list else "<li>Nenhum dado encontrado</li>"}
                    </ul>
                </div>
                """),
                    ]
                ),
            ],
            justify="start",
            gap=2,
        )

        return ui_dashboard


    gerar_ui_dashboard(df_new)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Análise De Creativos
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Para os criativos repetimos o mesmo processo, onde encontramos
    """)
    return


@app.cell(hide_code=True)
def _(alt, df_new, mo, pl):
    def _(dataset: pl.DataFrame):

        columns_names = dataset.select(pl.col("^.*ad_name_.*$")).columns

        dataset_diff = pl.DataFrame()

        for nome in columns_names:
            n = (
                dataset.filter(pl.col("Campaign_Type") == "E-commerce")
                .group_by(nome)
                .agg(pl.col("CPA").mean().alias(f"CPA_mean"))
                .sort(nome, descending=False)
                .with_columns(pl.col("CPA_mean").diff())
                .filter(pl.col(nome) == 1)
            )

            n = n.rename({nome: "ad_set"}).with_columns(
                pl.lit(nome).alias("ad_set")
            )

            dataset_diff = pl.concat([dataset_diff, n])

        width = 400
        hight = 200

        dataset_diff_top = dataset_diff.top_k(5, by="CPA_mean")
        dataset_diff_bottom = dataset_diff.bottom_k(5, by="CPA_mean")

        chart_top = (
            alt.Chart(dataset_diff_top)
            .mark_bar(color="red")
            .encode(
                x=alt.X("ad_set", title=""), y=alt.Y("CPA_mean", title="Mean CPA")
            )
            .properties(width=width, hight=hight)
        )

        chart_bottom = (
            alt.Chart(dataset_diff_bottom)
            .mark_bar(color="green")
            .encode(
                x=alt.X("ad_set", title=""), y=alt.Y("CPA_mean", title="Mean CPA")
            )
            .properties(width=width, hight=hight)
        )

        chart = chart_top | chart_bottom

        return mo.ui.altair_chart(
            chart, label="Melhores/Piores Atributos Do AD Set"
        )


    _(df_new)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    que ads com foco

    - em bônus
    - anualidade zero
    - seguros no geral

    têm um **CPA** $10$ reais mais alto na média, enquanto os com

    - vídeos de $30s$
    - cartão virtual
    - conta digital

    possuem o **CPA** $7$ reais mais baixo na média. E novamente não há uma grande diferença entre tipos de criativos. Olhando o top e bottom quartil, temos
    """)
    return


@app.cell(hide_code=True)
def _(df_new, mo, pl):
    def gerar_ui_dashboard_ad_name(dataset: pl.DataFrame):
        columns_names = dataset.select(pl.col("^.*ad_name_.*$")).columns

        dataset_diff = pl.DataFrame()

        for nome in columns_names:
            n = (
                dataset.filter(pl.col("Campaign_Type") == "E-commerce")
                .group_by(nome)
                .agg(pl.col("CPA").mean().alias("CPA_mean"))
                .sort(nome, descending=False)
                .with_columns(pl.col("CPA_mean").diff())
                .filter(pl.col(nome) == 1)
            )

            n = n.rename({nome: "ad_name"}).with_columns(
                pl.lit(nome).alias("ad_name")
            )

            dataset_diff = pl.concat([dataset_diff, n])

        # calcular quartis
        q25 = dataset_diff["CPA_mean"].quantile(0.25)
        q75 = dataset_diff["CPA_mean"].quantile(0.75)

        # filtrar quartil inferior e superior
        bottom_25 = dataset_diff.filter(pl.col("CPA_mean") <= q25)[
            "ad_name"
        ].to_list()
        top_25 = dataset_diff.filter(pl.col("CPA_mean") >= q75)[
            "ad_name"
        ].to_list()

        # Garante que os dados sejam strings e limpa as listas
        top_list = [str(item) for item in top_25]
        bottom_list = [str(item) for item in bottom_25]

        # Criando os itens HTML com segurança
        top_items_html = "".join(
            [
                f"<li style='padding: 8px 0; border-bottom: 1px solid #b2f5ea;'>✅ {item}</li>"
                for item in top_list
            ]
        )
        bottom_items_html = "".join(
            [
                f"<li style='padding: 8px 0; border-bottom: 1px solid #fed7d7;'>⚠️ {item}</li>"
                for item in bottom_list
            ]
        )

        ui_dashboard = mo.hstack(
            [
                mo.vstack(
                    [
                        mo.md("## 🚀 Top 25% Quartil"),
                        mo.Html(f"""
                <div style='background-color: #e6fffa; border-left: 5px solid #38b2ac; padding: 20px; border-radius: 8px; min-width: 300px;'>
                    <ul style='list-style-type: none; padding: 0; margin: 0; color: #2c7a7b;'>
                        {top_items_html if top_list else "<li>Nenhum dado encontrado</li>"}
                    </ul>
                </div>
                """),
                    ]
                ),
                mo.vstack(
                    [
                        mo.md("## 📉 Bottom 25% Quartil"),
                        mo.Html(f"""
                <div style='background-color: #fff5f5; border-left: 5px solid #f56565; padding: 20px; border-radius: 8px; min-width: 300px;'>
                    <ul style='list-style-type: none; padding: 0; margin: 0; color: #c53030;'>
                        {bottom_items_html if bottom_list else "<li>Nenhum dado encontrado</li>"}
                    </ul>
                </div>
                """),
                    ]
                ),
            ],
            justify="start",
            gap=2,
        )

        return ui_dashboard


    gerar_ui_dashboard_ad_name(df_new)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Resultados
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    As configurações no nível de ad sets e criativos não geram tanto impacto quanto as do nível de campanha; entretanto, a escolha dos atributos certos é um importante passo na otimização das próximas campanhas.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Teste De Hipóteses:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A nossa análise foi capaz de produzir uma série de insights de grande utilidade para o lançamento e otimização das próximas campanhas, porém é preciso testar se esses resultados são de fato válidos. Para tanto, precisamos realizar testes para validá-los. Os principais pontos que precisam ser testados são:

    - Campanhas de branding estão contribuindo indiretamente para a performance das campanhas de D&R?
    - Qual atribuição é mais precisa?
    - Há algum efeito de interação entre os atributos do ad set e dos ads?

    Para testar a primeira hipótese usamos um gráfico de regressão parcial para visualizar o efeito das campanhas de branding sobre as de D&R. Este tipo de gráfico é usado para mostrar a relação entre duas variáveis controlando outras, no nosso caso, buscamos a saber qual é a relação entre uma variável exógena, **CPA**, e uma endógena, diferença em dias entre o começo das campanhas (início branding - início D&R), controlando pelo número de campanhas ativas dentro desse intervalo. O seu funcionamento é bastante simples: para remover a influência da variável que queremos controlar, realiza-se uma regressão entre esta e a exógena e outra com a endógena; então, usam-se os resíduos dessas regressões para encontrar a relação entre variáveis. Assim, temos
    """)
    return


@app.cell(hide_code=True)
def _(df_new, pl):
    df_date = df_new.group_by(["Campaign_Type", "Reporting_Start"]).agg(
        [pl.col("CPA").mean().alias("CPA_mean"), pl.len().alias("Campaign_count")]
    )


    # Supondo que Reporting_Start seja do tipo Date
    df_ecom = df_date.filter(pl.col("Campaign_Type") == "E-commerce")
    df_brand = df_date.filter(pl.col("Campaign_Type") == "Branding")

    # Faz join cruzado (cartesiano) entre E-commerce e Branding
    df_cross = df_ecom.join(df_brand, how="cross")

    df_cross
    # Calcula diferença de dias
    df_cross = df_cross.with_columns(
        (pl.col("Reporting_Start") - pl.col("Reporting_Start_right"))
        .dt.total_days()
        .alias("days_diff")
    )

    # Agora cria os grupos
    grupo_1 = df_cross.filter(
        (pl.col("days_diff") >= 0) & (pl.col("days_diff") <= 3)
    )
    grupo_2 = df_cross.filter(
        (pl.col("days_diff") > 3) & (pl.col("days_diff") <= 7)
    )
    grupo_3 = df_cross.filter(
        (pl.col("days_diff") > 7) & (pl.col("days_diff") <= 15)
    )
    grupo_4 = df_cross.filter(pl.col("days_diff") > 15)
    return (df_cross,)


@app.cell(hide_code=True)
def linear_regression(LinearRegression, alt, df_cross, mo, pl):
    from typing import Tuple


    def plot_added_variable(
        df: pl.DataFrame,
        y_col: str = "CPA",
        x_col: str = "days_diff",
        z_col: str = "Campaign_count_right",
        title: str = None,
    ) -> alt.Chart:
        """
        Cria um Added-Variable Plot (Partial Regression Plot) usando Altair.

        Parâmetros:
            df: DataFrame Polars com os dados
            y_col: Variável dependente (ex: CPA)
            x_col: Variável de interesse (ex: days_diff)
            z_col: Variável de controle
            title: Título personalizado (opcional)
        """
        width = 900
        height = 350

        df = df.group_by(["days_diff", "Campaign_count_right"]).agg(
            pl.col("CPA_mean").mean().alias("CPA")
        )

        # Converter para numpy para regressões
        y = df[y_col].to_numpy().reshape(-1, 1)
        x = df[x_col].to_numpy().reshape(-1, 1)
        z = df[z_col].to_numpy().reshape(-1, 1)

        # ========================
        # Modelo completo (para extrair o coeficiente)
        # ========================
        X_full = df[[x_col, z_col]].to_numpy()
        model_full = LinearRegression()
        model_full.fit(X_full, y.ravel())
        coef = model_full.coef_[0]

        # ========================
        # Cálculo dos resíduos
        # ========================
        # Resíduos: y ~ z
        model_yz = LinearRegression().fit(z, y.ravel())
        res_y = y.ravel() - model_yz.predict(z)

        # Resíduos: x ~ z
        model_xz = LinearRegression().fit(z, x.ravel())
        res_x = x.ravel() - model_xz.predict(z)

        # Criar DataFrame com resíduos
        df_res = pl.DataFrame({"res_x": res_x, "res_y": res_y})

        # ========================
        # Gráfico Altair
        # ========================
        if title is None:
            title = f"Added-Variable Plot: Efeito de {x_col} sobre {y_col}\n(controlando por {z_col})"

        # Scatter + linha de regressão
        chart = (
            alt.Chart(df_res)
            .mark_circle(size=60, opacity=0.7, color="blue")
            .encode(
                x=alt.X(
                    "res_x:Q",
                    title=f"diferença de dias entre campanhas (controlando por n° de campanhas)",
                ),
                y=alt.Y(
                    "res_y:Q", title=f"CPA médio (controlando por n° de campanhas)"
                ),
                tooltip=[
                    alt.Tooltip("res_x:Q", format=".3f"),
                    alt.Tooltip("res_y:Q", format=".3f"),
                ],
            )
            .properties(width=width, height=height, title=title)
        )

        # Linha de regressão
        regression_line = chart.transform_regression(
            "res_x", "res_y", method="linear"
        ).mark_line(color="red", strokeWidth=2.5)

        # Combinar os dois
        final_chart = (
            (chart + regression_line)
            .configure_title(fontSize=16, anchor="middle")
            .configure_axis(labelFontSize=12, titleFontSize=13)
        )

        # Adicionar texto com o coeficiente
        text = (
            alt.Chart(pl.DataFrame({"text": [f"Coeficiente β = {coef:.4f}"]}))
            .mark_text(
                align="left",
                baseline="top",
                dx=10,
                dy=10,
                fontSize=14,
                color="red",
            )
            .encode(text="text:N")
        )

        final_chart = final_chart + text

        return mo.ui.altair_chart(final_chart)


    # Exemplo de uso:
    chart = plot_added_variable(
        df=df_cross,
        y_col="CPA",
        x_col="days_diff",
        z_col="Campaign_count_right",
        title="Efeito Das Campanhas De Branding Sobre O CPA Das Campanhas De D&R",
    )

    chart
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    O gráfico, que no eixo X mostra a diferença em dias entre inicil campanha D&R - inicil campanha Branding controlado pelo n° de campanhas de branding, mostra a existência de uma pequena influência possitiva das campanhas de branding sobre a performance de D&R. Quando esta começa um pouco depois de uma campanha de branding, tende a ter o **CPA** um pouco melhor, mas podemos ignorar este efeito, já que ele é de apenas $≃0.03$.

    No caso da atribuição, o problema é semelhante: como a janela de atribuição é bem maior no caso do 7 days view, one day click, uma conversão tem maior probabilidade de ser erroneamente atribuída. Para solucionar esse problema, devemos isolar o efeito de cada atribuição para saber qual é o melhor método de atribuição. Nesse caso, só olharemos para as campanhas de D&R, que serão divididas em dois grupos: Ambos utilizam o mesmo método de atribuição (one day view, seven days click). A diferença é que um deles não possui campanhas com atribuição de 1-day click dentro da sua janela, enquanto o outro possui. Se houver variação no CPA entre os grupos, isso indicará um possível erro na atribuição. Também será construído um segundo gráfico com as campanhas de D&R com o tipo de atribuição 1-day view, 7-day click, com o **CPA** agrupado pelo dia em que começaram as campanhas com o outro tipo de atribuição.
    """)
    return


@app.cell(hide_code=True)
def _(alt, df_new, mo, pl):
    alt.data_transformers.enable("vegafusion")


    def gerar_boxplots(df_new: pl.DataFrame):
        # Filtrar datasets
        df_1_day = df_new.filter(pl.col("Attribution_Setting") == "1-day click")
        df_7_days_clicks_1_day_view = df_new.filter(
            pl.col("Attribution_Setting") != "1-day click"
        )

        # Criar mix
        df_mix = df_7_days_clicks_1_day_view.join(df_1_day, how="cross")

        # Calcular diff_days
        df_inside = df_mix.with_columns(
            (pl.col("Reporting_Start") - pl.col("Reporting_Start_right"))
            .dt.total_days()
            .alias("diff_days")
        ).filter(pl.col("diff_days") <= 0)

        # Criar coluna condicional "a"
        df_inside = df_inside.with_columns(
            pl.when(pl.col("diff_days") < -7)
            .then(pl.lit("fora"))
            .otherwise(pl.lit("dentro"))
            .alias("a")
        )

        # Boxplot por categoria "a"
        boxplot = (
            alt.Chart(df_inside)
            .mark_boxplot()
            .encode(x=alt.X("a:N", title=""), y="CPA:Q")
            .properties(title="Boxplot de CPA por categoria", width=400)
        )

        # Boxplot por diff_days entre -7 e 0
        boxplot_days = (
            alt.Chart(df_inside.filter(pl.col("diff_days").is_between(-7, 0)))
            .mark_boxplot()
            .encode(x=alt.X("diff_days:Q", title=""), y="CPA:Q")
            .properties(
                title="CPA por intervalo entre início das campanhas de Branding e D&R",
                width=400,
            )
        )

        return mo.ui.altair_chart(boxplot | boxplot_days)


    gerar_boxplots(df_new)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Pelos gráficos acima, vemos que não existe atribuição incorreta, já que não há diferença entre o CPA médio para campanhas com atribuição 1 day view 7 days click que possuem campanhas do tipo 1 day click dentro da sua janela de atribuição. Desta forma excluímos essa hipótese. No caso da última hipótese podemos testá-la dividindo o dataset em quatro grupos:

    - Ad sets que estão no top/bottom $25$% quartil em relação ao CPA.
    - Ads que estão no top/bottom $25$% quartil em relação ao CPA.

    Caso haja sinergia entre as características dos ad sets e ads pode quantificá-la pelo termo de interação da regressão linear

    $$
    \text{n° de campanhas no grupo X} = \beta_{1} \times (\text{grupo ad set}) + \beta_{2} \times (\text{grupo ad}) + \beta_{int} \times (\text{grupo ad set}) \times (\text{grupo ad}) + \alpha
    $$

    pois este será zero quando o efeito de cada grupo for meramente aditiva. Se

    $$
    \beta_{int} > 0
    $$

    há sinergia entre os grupos, se

    $$
    \beta_{int} < 0
    $$

    há conflito entre eles, e quando esse é nulo, não existe qualquer interação. Dessa forma, temos
    """)
    return


@app.cell(hide_code=True)
def _(df_new, mo, pl, px, smf):
    def analisar_interacao_ad_set_ad_name_1(dataset: pl.DataFrame):
        """
        Analisa interação entre Ad Set e Ad (quartis) com foco em Número de Campanhas.
        Calcula e exibe o termo de interação (β_int).
        """

        # ====================== PROCESSAMENTO DOS QUARTIS ======================
        # === Ad_Set ===
        columns_ad_set = dataset.select(pl.col("^.*ad_set_.*$")).columns
        dataset_diff_set = pl.DataFrame()
        for nome in columns_ad_set:
            n = (
                dataset.filter(pl.col("Campaign_Type") == "E-commerce")
                .group_by(nome)
                .agg(pl.col("CPA").mean().alias("CPA_mean"))
                .sort(nome, descending=False)
                .with_columns(pl.col("CPA_mean").diff())
                .filter(pl.col(nome) == 1)
            )
            n = n.rename({nome: "ad_set"}).with_columns(
                pl.lit(nome).alias("ad_set_name")
            )
            dataset_diff_set = pl.concat([dataset_diff_set, n])

        q25_set = dataset_diff_set["CPA_mean"].quantile(0.25)
        q75_set = dataset_diff_set["CPA_mean"].quantile(0.75)

        top_list_ad_set = "|".join(
            [
                str(x).replace("ad_set_", "")
                for x in dataset_diff_set.filter(pl.col("CPA_mean") >= q75_set)[
                    "ad_set_name"
                ].to_list()
            ]
        )
        bottom_list_ad_set = "|".join(
            [
                str(x).replace("ad_set_", "")
                for x in dataset_diff_set.filter(pl.col("CPA_mean") <= q25_set)[
                    "ad_set_name"
                ].to_list()
            ]
        )

        # === Ad_Name ===
        columns_ad_name = dataset.select(pl.col("^.*ad_name_.*$")).columns
        dataset_diff_ad = pl.DataFrame()
        for nome in columns_ad_name:
            n = (
                dataset.filter(pl.col("Campaign_Type") == "E-commerce")
                .group_by(nome)
                .agg(pl.col("CPA").mean().alias("CPA_mean"))
                .sort(nome, descending=False)
                .with_columns(pl.col("CPA_mean").diff())
                .filter(pl.col(nome) == 1)
            )
            n = n.rename({nome: "ad"}).with_columns(pl.lit(nome).alias("ad_name"))
            dataset_diff_ad = pl.concat([dataset_diff_ad, n])

        q25_ad = dataset_diff_ad["CPA_mean"].quantile(0.25)
        q75_ad = dataset_diff_ad["CPA_mean"].quantile(0.75)

        top_list_ad = "|".join(
            [
                str(x).replace("ad_name_", "")
                for x in dataset_diff_ad.filter(pl.col("CPA_mean") >= q75_ad)[
                    "ad_name"
                ].to_list()
            ]
        )
        bottom_list_ad = "|".join(
            [
                str(x).replace("ad_name_", "")
                for x in dataset_diff_ad.filter(pl.col("CPA_mean") <= q25_ad)[
                    "ad_name"
                ].to_list()
            ]
        )

        # ====================== CRIAÇÃO DAS VARIÁVEIS ======================
        df = dataset.with_columns(
            [
                pl.when(pl.col("Ad_Set_Name").str.contains(bottom_list_ad_set))
                .then(pl.lit("Top 25% Ad Set"))
                .when(pl.col("Ad_Set_Name").str.contains(top_list_ad_set))
                .then(pl.lit("Bottom 25% Ad Set"))
                .otherwise(pl.lit("Outros"))
                .alias("ad_set_quartil"),
                pl.when(pl.col("Ad_Name").str.contains(bottom_list_ad))
                .then(pl.lit("Top 25% Ad"))
                .when(pl.col("Ad_Name").str.contains(top_list_ad))
                .then(pl.lit("Bottom 25% Ad"))
                .otherwise(pl.lit("Outros"))
                .alias("ad_quartil"),
            ]
        )

        # Filtra apenas as combinações relevantes
        df_interacao = df.filter(
            (pl.col("ad_set_quartil") != "Outros")
            & (pl.col("ad_quartil") != "Outros")
        )

        # ====================== TABELA DE CONTAGEM ======================
        tabela = (
            df_interacao.group_by(["ad_set_quartil", "ad_quartil"])
            .agg(pl.len().alias("n_campanhas"))
            .sort(["ad_set_quartil", "ad_quartil"])
        )

        # ====================== REGRESSÃO LINEAR COM INTERAÇÃO ======================
        # Cria dummies para regressão
        df_reg = df_interacao.with_columns(
            [
                (pl.col("ad_set_quartil") == "Top 25% Ad Set")
                .cast(pl.Int8)
                .alias("ad_set_top"),
                (pl.col("ad_quartil") == "Top 25% Ad")
                .cast(pl.Int8)
                .alias("ad_top"),
            ]
        )

        # Converte para pandas (statsmodels)
        df_pd = df_reg.select(["ad_set_top", "ad_top"]).to_pandas()
        df_pd["n_campanhas"] = 1  # Cada linha é uma campanha

        # Modelo de regressão
        model = smf.ols(
            "n_campanhas ~ ad_set_top + ad_top + ad_set_top:ad_top", data=df_pd
        ).fit()

        beta_int = model.params["ad_set_top:ad_top"]
        p_value = model.pvalues["ad_set_top:ad_top"]

        # ====================== GRÁFICO ======================
        fig = px.line(
            tabela,
            x="ad_set_quartil",
            y="n_campanhas",
            color="ad_quartil",
            markers=True,
            title="Interação entre Ad Set e Ad<br><sup>Número de Campanhas por Combinação</sup>",
            labels={
                "n_campanhas": "Número de Campanhas",
                "ad_set_quartil": "Qualidade do Ad Set",
            },
            color_discrete_sequence=["#1f77b4", "#ff7f0e"],
        )

        # Adiciona anotação com o β_int
        annotation_text = (
            f"<b>β_int = {beta_int:.3f}</b><br>p-value = {p_value:.3f}"
        )
        if p_value < 0.05:
            annotation_text += " <b>*</b>"

        fig.add_annotation(
            x=0.5,
            y=0.95,
            xref="paper",
            yref="paper",
            text=annotation_text,
            showarrow=False,
            font=dict(size=14, color="black"),
            bgcolor="rgba(255,255,255,0.8)",
            bordercolor="black",
            borderwidth=1,
            borderpad=4,
            align="center",
        )

        fig.update_layout(
            height=580,
            template="plotly_dark",
            legend_title="Qualidade do Ad",
            yaxis_title="Número de Campanhas",
        )

        # fig.show()

        return mo.ui.plotly(fig)


    # Uso:
    # resultado, modelo = analisar_interacao_ad_set_ad_name(df_new)

    analisar_interacao_ad_set_ad_name_1(df_new)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    O gráfico evidencia o comportamento de cada grupo, acompanhado do valor do termo de interação, que é igual a zero. Esse resultado indica que os atributos no nível dos ad sets e dos próprios ads contribuem de forma independente para o desempenho da campanha.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ### Resultados
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Todas as hipóteses se mostraram inválidas

    ❌ Campanhas de branding estão contribuindo indiretamente para a performance das campanhas de D&R

    ❌ Há erro nas atribuições de conversões no modelo 1-day view, 7-day click

    ❌ Existe efeito de interação entre os tributos do ad set e ad

    Resultado que valida os insights obtidos ao longo do trabalho.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ---
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Resultado Final:
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    #### 🎯 Objetivo Principal
    O trabalho teve como objetivo realizar uma análise sobre as campanhas de marketing do Nubank na Meta, buscando compreender padrões, relações e possíveis fatores relevantes para o problema de negócio. A meta era transformar dados brutos em informações úteis, capazes de apoiar decisões estratégicas e comprovar hipóteses para etapas posteriores de modelagem ou tomada de decisão.

    ---

    #### 🛠️ Principais Métodos Utilizados

    - **Limpeza e tratamento de dados**: remoção de valores nulos, duplicados e inconsistências.
    - **Análise estatística descritiva**: cálculo de médias, medianas, distribuições e correlações.
    - **Visualizações gráficas**: histogramas, boxplots, scatterplots e heatmaps para identificar padrões e outliers.
    - **Segmentação e agrupamento exploratório**: análise por categorias e variáveis-chave para entender diferenças entre grupos.
    - **Testes de hipóteses iniciais**: verificação de relações estatisticamente significativas entre variáveis.

    ---

    #### 📈 Principais Resultados e Insights

    - **Campanhas De E-commerce(D&R)**: Têm performance superior em todas as métricas, principalmente nas de maior impacto para os objetivos da empresa.
    - **O modelo de atribuição**: não interfere nos resultados das campanhas.
    - **Os atributos do ad set e dos ads**: Não impactam de forma significativa o **CPA** da campanha.

    ---

    #### ⚡ Impactos Quantificados

    - **Tipo de campanha**: Utilizar apenas campanhas de D&R reduz o **CPA** em aproximadamente $200$ reais.

    - **Trend**: O dia da semana não influencia a performance das campanhas.

    - **Ad set**: Escolher os atributos corretos reduz o **CPA** em aproximadamente $3$ reais.

    - **set**: Escolher os atributos corretos reduz o **CPA** em aproximadamente $8$ reais.

    ---
    """)
    return


if __name__ == "__main__":
    app.run()
