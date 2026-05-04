# /// script
# requires-python = ">=3.13"
# dependencies = [
#     "marimo>=0.23.1",
# ]
# ///

import marimo

__generated_with = "0.23.4"
app = marimo.App(width="full", auto_download=["html"])


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    Faça uma análise dos dados destas campanhas do NuBank **(Campanhas SImuladas)**

    Os exemplos abaixo são de referência; você pode criar da maneira que achar mais adequada de acordo com o que foi aprendido no curso até o momento.

    CASE: Nubank – Análise de Performance e Planejamento de Próximas Campanhas

    ## Contexto do Case

    Você foi contratado como **Digital Marketing Analyst** do Nubank para analisar campanhas rodadas no Meta Ads durante o Q1. 1.

    O Nubank deseja acelerar a **abertura de contas digitais** utilizando Meta Ads (Facebook, Instagram e Audience Network). A operação já está rodando há alguns meses, com campanhas ativas em diferentes objetivos.

    O time interno percebeu crescimento em volume, mas não tem clareza sobre a eficiência real do investimento, nem sobre o impacto incremental das campanhas.

    ---

    A base de dados contém:

    - Campanhas de **Branding** e **Conversão (Account Opening)**

    - Métricas de:

        - Spend (BRL)

        - Impressions

        - Reach

        - Frequency

        - Link Clicks

        - Conversions

        - Attribution Setting

        - Delivery Status


    O objetivo do Nubank é:

    Maximizar Account Openings mantendo eficiência de mídia e escalabilidade.
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


@app.cell
def _():
    import marimo as mo
    import polars as pl
    import numpy as np
    import altair as alt

    import asyncio
    import sys

    if sys.platform == "win32":
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    return alt, mo, pl


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Dataset
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
    O resultado da validação mostrou

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

    Todas têm como objetivo facilitar o estudo da performance das campanhas. Além dessas novas métricas, também serão criadas novas colunas com as informações contidas no "Ad Set Name" e "Ad Set Name", por exemplo, no caso, ad set name "BR_18-24_Students" duas novas colunas serão criadas, ad_name_18-24 e ad_name_students, e os seus valores serão 1, para representar as características do ad.
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

    O Nubank busca acelerar o número de contas abertas. À primeira vista, seria natural avaliar a performance das campanhas apenas por esse indicador. No entanto, essa visão é limitada, pois não considera os custos envolvidos nem o valor que esses clientes trarão ao longo do tempo.

    Para capturar essas relações de forma mais completa, selecionamos quatro métricas principais: **CPA**, **LTV**, **conversions per 1k impressions** e **reach**.

    Assim, devemos identificar as campanhas que:
    - geram o maior número de contas abertas por 1.000 impressões (reach);
    - apresentam a melhor relação \(\frac{LTV}{CPA}\), ou seja, maior valor de vida útil por custo de aquisição.
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
    Os anúncios podem ser classificados em dois grupos principais:
    - **Branding**: voltados para aumentar o reconhecimento da marca e reforçar sua mensagem.
    - **E-commerce (D&R)**: focados exclusivamente em gerar uma ação específica — no nosso caso, a abertura de conta.

    A primeira etapa da análise será concentrada nesses dois grupos. As métricas **CTR, CPC, CVR, CPA e CPM** serão comparadas entre eles, com o objetivo de identificar qual tipo de anúncio apresenta melhor desempenho. O histograma do CTR por tipo de campanha
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
    Mostra que campanhas do tipo E-commerce producem mais clicks. No caso do CPC, CVR, CPA e CPM, temos
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
    novamente as campanhas do tipo E-commerce se mostraram superior, em expecial na comparação do **CPA**, onde há uma clara difrença entre as duas. Estudando a relação entre o **CPA** e frequência, temos
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
    Vemos que o **CPA** permanece constante conforme a frequência varia para ambos os tipos de campanhas e que campanhas do tipo E-commerce possuem **CPA** menor que as de braiding em qualquer frequência. Juntando as informações, conclui-se que

    - As campanhas de D&R são superiores em todas as métricas analisadas, em especial no caso do **CPA**
    - Não há frequência de saturação no intervalo observado para ambos os tipos de campanha.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    # Performace Por 1k De impressões e Reaches
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    A nossa análise já indica que as campanhas de D&R apresentam desempenho superior em relação às de E-commerce. No entanto, ainda é necessário aprofundar o estudo dos dados antes de tomar uma decisão definitiva. Ao avaliar os resultados pelas métricas de volume e pelos diferentes modelos de atribuição, observamos
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
    A análise dos gráficos mostra que as campanhas com o modelo de atribuição *7-day click, 1-day view* apresentam melhor desempenho. Esse resultado já era esperado, uma vez que a janela de atribuição é significativamente maior do que a utilizada pelo concorrente. Também era previsível que as campanhas de D&R superassem as de branding.

    No entanto, observa-se que a performance de ambos os tipos de campanha não revela uma tendência consistente ao longo do tempo. Além disso, não há correlação entre a frequência e as conversões por mil impressões. Já ao avaliar os resultados por mil *reaches*, verificamos que
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
    Que os resultados permanecem identicos, com novamente as campanhas de D&R tendo melhor perfomace em dos os paramêntros
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
    Na análise dos ad sets buscamos encontrar quais características mais reduzem/aumenta o CPA da campanha. Pelos gráficos abaixo, vemos
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

    com um **CPA** médio de $3$ reais menor.
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    ## Análise De ADs
    """)
    return


@app.cell(hide_code=True)
def _(mo):
    mo.md(r"""
    No caso dos ads, temos
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

    possuem o **CPA** $7$ reais mais baixo na média.
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
    As comfinfurações a nível de ad sets e ads não geram tanto impacto quanto as no nívem de campanha, entrentanto ainda podemos usar as informações obititas para otimizar futuras campanhas.
    """)
    return


@app.cell
def _(df_new, pl):
    a = df_new.group_by(pl.col("^.*ad_set_.*|Campaign_Type$")).agg(
        pl.col("CTR").mean().alias("s")
    )

    a
    return


@app.cell
def _():
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
