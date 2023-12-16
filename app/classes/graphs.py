import streamlit as st
import plotly.express as px
import polars as pl
from . import functions as f


# Plotar Globo com a quantidade de litros Exportados por país
def graph_globe(df: pl.DataFrame) -> px:
    df_aux = (
        df.filter(pl.col("liters") > 1000)
        .group_by(["country","name"])
        .agg(pl.sum("value"))
    )

    fig = px.scatter_geo(
        df_aux,
        locations="name",
        locationmode="country names",
        size="value",
        color="country",
        projection="orthographic",
        size_max=50,
        custom_data=["value", "country"],
    )

    fig.update_traces(
        hovertemplate="<b>%{customdata[1]}</b><br>%{customdata[0]} Litros<extra>%{customdata[2]}</extra>"
    )

    fig.update_layout(
        title={
            "text": "Total de Litros de Vinho Vendidos por País",
            "xanchor": "center",
            "xref": "paper",
            "yanchor": "top",
            "x": 0.5,
            "y": 0.95,
            "font": {"size": 20},
        },
        template="seaborn",
        height=500,
        margin={"l": 10, "r": 10, "b": 140, "t": 130, "pad": 5},
        legend={
            "orientation": "v",
            "yanchor": "middle",
            "xanchor": "center",
            "x": 1,
            "y": 0.5,
            "title": "",
            "itemsizing": "constant",
        },
    )

    return fig

def table_info(df: pl.DataFrame) -> pl.DataFrame:
    return df.select(
        pl.lit("Brasil").alias("País de Origem"),
        pl.col("country").alias("País de Destino"),
        pl.col("year").alias("Ano de Referência"),
        pl.col("liters").alias("Quantidade de Vinho Exportado (Litros)"),
        pl.col("value").alias("Valor Total Exportado (US$)"),
    )

def graph_1(df: pl.DataFrame, config: dict) -> None:

    var = "value" if config['metric'] == "Valor Exportado" else "liters"
    func = pl.sum if config['agg'] == "Valor Total" else pl.mean

    df_aux = df.group_by("country").agg(func(var)).sort(var, descending=True)
    fig = px.bar(df_aux, x="country", y=var)

    layout_info = {
        "Valor Exportado": {
            "Valor Total": {
                "yaxis": {"title": "Valor Total Exportado (US$)"},
                "hovertemplate": "<b>%{x}</b><br>Total: U$ %{y}",
                "title": "Valor Total Exportado por Região",
                "sup": "Gráfico de Barras exibindo o valor total de vinhos exportado (em US$) para cada região do mundo",
            },
            "Valor Médio": {
                "yaxis": {"title": "Valor Médio Exportado (US$)"},
                "hovertemplate": "<b>%{x}</b><br>Média: U$ %{y}",
                "title": "Valor Médio Exportado por Região",
                "sup": "Gráfico de Barras exibindo o valor médio de vinho exportado (em US$) para cada região do mundo",
            },
        },
        "Litros Exportados": {
            "Valor Total": {
                "yaxis": {"title": "Total de Vinho Exportados (Litros)"},
                "hovertemplate": "<b>%{x}</b><br>Total: %{y} Litros",
                "title": "Volume de Vinho Exportado por Região",
                "sup": "Gráfico de Barras exibindo o volume total de vinho exportado (em litros) para cada região do mundo",
            },
            "Valor Médio": {
                "yaxis": {"title": "Volume Médio de Vinho Exportado (Litros)"},
                "hovertemplate": "<b>%{x}</b><br>Média: %{y} Litros",
                "title": "Volume Médio de Vinho Exportado por Região",
                "sup": "Gráfico de Barras exibindo o volume médio de vinho exportado (em litros) para cada região do mundo",
            },
        },
    }
    
    layout_info_selected = layout_info[config['metric']][config['agg']]

    f.layout_graphs(
        fig,
        yaxis=layout_info_selected["yaxis"],
        xaxis={"title": "Região"},
        hovertemplate=layout_info_selected["hovertemplate"],
        title_text=layout_info_selected["title"],
        title_sup=layout_info_selected["sup"],
        marker_color="#794A9E"
    )
    
    return fig

def graph_2(df: pl.DataFrame, config: dict) -> None:

    var = "value" if config['metric'] == "Valor Exportado" else "liters"
    func = pl.sum if config['agg'] == "Valor Total" else pl.mean
    year = config['year']

    df_aux = (
        df.filter((pl.col("year") >= year[0]) & (pl.col("year") <= year[1]))
        .group_by(["name","country"])
        .agg(func(var))
        .sort("country")
    )

    fig = px.scatter_geo(
        df_aux,
        size=var,
        locations="name",
        locationmode="country names",
        color="country",
        projection="natural earth",
        size_max=30,
        custom_data=["country", var],
    )

    layout_info = {
        "Valor Exportado": {
            "Valor Total": {
                "yaxis": {"title": "Valor Total Exportado (US$)"},
                "hovertemplate": "<b>%{customdata[0]}</b><br>Total: U$ %{customdata[1]}",
                "title": "Valor Total Exportado (US$) por País",
                "sup": "Mapa exibindo o valor total de vinho exportado (em US$) para cada país do mundo",
            },
            "Valor Médio": {
                "yaxis": {"title": "Valor Médio Exportado (US$)"},
                "hovertemplate": "<b>%{customdata[0]}</b><br>Média: U$ %{customdata[1]:.2f}",
                "title": "Valor Médio Exportado por País",
                "sup": "Mapa exibindo o valor médio de vinho exportado (em US$) para cada país do mundo",
            },
        },
        "Litros Exportados": {
            "Valor Total": {
                "yaxis": {"title": "Total de Vinho Exportados (Litros)"},
                "hovertemplate": "<b>%{customdata[0]}</b><br>Total: %{customdata[1]} Litros",
                "title": "Total de Vinho Exportados por País",
                "sup": "Mapa exibindo o volume total de vinho exportado (em litros) para cada país do mundo",
            },
            "Valor Médio": {
                "yaxis": {"title": "Volume Médio de Vinho Exportado (Litros)"},
                "hovertemplate": "<b>%{customdata[0]}</b><br>Média: %{customdata[1]:.2f} Litros",
                "title": "Volume Médio de Vinho Exportado por País",
                "sup": "Mapa exibindo o volume médio de vinho exportado (em litros) para cada país do mundo",
            },
        },
    }
    
    layout_info_selected = layout_info[config['metric']][config['agg']]

    f.layout_graphs(
        fig,
        yaxis=layout_info_selected["yaxis"],
        xaxis={"title": "Continente"},
        hovertemplate=layout_info_selected["hovertemplate"],
        legend={
            "orientation": "h",
            "xanchor": "center",
            "x": 0.5,
            "y": -0.1,
            "title": "",
            "itemsizing": "constant",
        },
        title_text=layout_info_selected["title"],
        title_sup=layout_info_selected["sup"]
    )

    return fig

def graph_3(df: pl.DataFrame, config:dict) -> None:
    cols = st.columns([2, 1], gap="large")
    col_name = config['col_name']
    
    if config['viz'] == "Customizar":
        list_selected = config['list_selected']
    else:
        df_list_country = (
            df.select(pl.col(col_name, "country"))
            .group_by("country")
            .agg(pl.sum(col_name))
            .sort(col_name, descending=True)
            .limit(3)
        )

        list_selected = df_list_country.select(pl.col("country")).to_series().to_list()  

    with cols[0]:

        df_aux = (
            df.select(pl.col(col_name, "country", "year"))
            .with_columns(
                pl.when(pl.col("country").is_in(list_selected))
                .then(pl.col("country"))
                .otherwise(pl.lit("Outros"))
                .alias("group"),
                pl.when(pl.col("country").is_in(list_selected))
                .then(pl.col(col_name))
                .otherwise(0)
                .alias("order"),
            )
            .group_by("year", "group")
            .agg(pl.sum(col_name), pl.sum("order"))
            .sort(["year", "order"])
        )

        fig = px.line(
            df_aux,
            x="year",
            y=col_name,
            color="group",
            color_discrete_sequence=px.colors.qualitative.Plotly,
            color_discrete_map={"Outros": "#ccc"},
            markers=True,
        )

        layout_info = {
            "Valor Exportado": {
                "yaxis": {"title": "Valor Total Exportado (US$)"},
                "hovertemplate": "<b>%{x}</b><br>U$ %{y}",
                "title": "Valor Total Exportado nos Anos de Referência",
                "sup": "Gráfico de Linha exibindo o valor total de vinho exportado (em US$) por país ao longo do tempo",
            },
            "Litros Exportados": {
                "yaxis": {"title": "Total de Vinho Exportados (Litros)"},
                "hovertemplate": "<b>%{x}</b><br>%{y} Litros",
                "title": "Total de Vinho Exportados nos Anos de Referência",
                "sup": "Gráfico de Linha exibindo o volume total de vinho exportado (em litros) por país ao longo do tempo",
            },
        }
        
        layout_info_selected = layout_info[config['metric']]

        f.layout_graphs(
            fig,
            yaxis=layout_info_selected["yaxis"],
            xaxis={"title": "Ano de Referência"},
            hovertemplate=layout_info_selected["hovertemplate"],
            legend={
                "orientation": "h",
                "yanchor": "middle",
                "xanchor": "center",
                "x": 0.5,
                "y": -0.3,
                "title": "",
                "itemsizing": "constant",
                "traceorder": "reversed",
            },
            title_text=layout_info_selected["title"],
            title_sup=layout_info_selected["sup"]
        )
        
    return fig