import streamlit as st
import plotly.express as px
import polars as pl

def tab_intro(df: pl.DataFrame) -> None:
    config_graph = {}
    config_graph["col_name"] = "value"
    config_graph["metric"] = "Valor Importado"
    config_graph["viz"] = "Visualização"

    config_graph_1 = {}
    config_graph_1['metric'] = "Valor Importado"
    config_graph_1['agg'] = "Valor Total"

    st.plotly_chart(graph_1(df,config_graph_1), use_container_width=True)
    st.markdown("<p style='text-align: justify; color:gray; font-size:18px'>No ano de 2016 devido ao fenômeno climático do El Niño, que gerou demanda crescente no mercado, vemos que importamos um valor consideravelmente maior principalmente do Chile, aumentando U$ 15 milhões no valor importado em apenas 1 ano. Podemos conferir a relação de importação com os demais países do mundo nos últimos 15 anos no gráfico abaixo:</p>",  unsafe_allow_html=True)
    st.plotly_chart(graph(df, config_graph), use_container_width=True)
    
    st.plotly_chart(graph_globe(df), use_container_width=True)

    st.markdown(
        """
        ###### Tabela com informações sobre a importação de vinho
        Tabela contém informações sobre a importação de vinho, como país de origem e de destino, ano de referência, quantidade de vinho importado (em litros) e valor total importado (em US$)
        """
    )
    st.dataframe(table_info(df), use_container_width=True)
    
    return None

def table_info(df: pl.DataFrame) -> pl.DataFrame:
    return df.filter(pl.col("year") >= 2004).select(
        pl.lit("Brasil").alias("País de Origem"),
        pl.col("country").alias("País de Destino"),
        pl.col("year").alias("Ano de Referência"),
        pl.col("liters").alias("Quantidade de Vinho Importado (Litros)"),
        pl.col("value").alias("Valor Total Importado (US$)"),
    )
      

def graph_globe(df: pl.DataFrame) -> px:
    df_aux = (
        df.filter(pl.col("liters") > 1000)
        .filter(pl.col("year") >= 2004)
        .group_by(["country","name"])
        .agg(pl.sum("value"))
        .sort("value", descending=True)
    )
    
    fig = px.scatter_geo(
        df_aux.head(10),
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
        height=600,
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

def graph_1(df: pl.DataFrame, config: dict) -> None:
    var = "value" if config['metric'] == "Valor Importado" else "liters"
    func = pl.sum if config['agg'] == "Valor Total" else pl.mean

    df_aux = df.filter(pl.col("year") >= 2004).group_by("country").agg(func(var)).sort(var, descending=True)
    df_aux2 = df_aux.head(10)
    fig = px.bar(df_aux2, x="country", y=var)

    layout_info = {
        "Valor Importado": {
            "Valor Total": {
                "yaxis": {"title": "Valor Total Importado (US$)"},
                "hovertemplate": "<b>%{x}</b><br>Total: U$ %{y}",
                "title": "Valor Total Importado por Região",
                "sup": "Gráfico de Barras exibindo o valor total de vinhos importado (em US$) para cada região do mundo",
            },
            "Valor Médio": {
                "yaxis": {"title": "Valor Médio Importado (US$)"},
                "hovertemplate": "<b>%{x}</b><br>Média: U$ %{y}",
                "title": "Valor Médio Importado por Região",
                "sup": "Gráfico de Barras exibindo o valor médio de vinho importado (em US$) para cada região do mundo",
            },
        },
        "Litros Importados": {
            "Valor Total": {
                "yaxis": {"title": "Total de Vinho Importados (Litros)"},
                "hovertemplate": "<b>%{x}</b><br>Total: %{y} Litros",
                "title": "Volume de Vinho Importado por Região",
                "sup": "Gráfico de Barras exibindo o volume total de vinho importado (em litros) para cada região do mundo",
            },
            "Valor Médio": {
                "yaxis": {"title": "Volume Médio de Vinho Importado (Litros)"},
                "hovertemplate": "<b>%{x}</b><br>Média: %{y} Litros",
                "title": "Volume Médio de Vinho Importado por Região",
                "sup": "Gráfico de Barras exibindo o volume médio de vinho importado (em litros) para cada região do mundo",
            },
        },
    }
    
    layout_info_selected = layout_info[config['metric']][config['agg']]

    layout_graphs(
        fig,
        yaxis=layout_info_selected["yaxis"],
        xaxis={"title": "Região"},
        hovertemplate=layout_info_selected["hovertemplate"],
        title_text=layout_info_selected["title"],
        title_sup=layout_info_selected["sup"],
        marker_color="#794A9E"
    )
    
    return fig

def graph(df: pl.DataFrame, config:dict) -> None:
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
            .limit(10)
        )

        list_selected = df_list_country.select(pl.col("country")).to_series().to_list()  

    with cols[0]:
        df_aux = (
            df.filter(pl.col("year") >= 2004)         
            .select(pl.col(col_name, "country", "year"))
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
            "Valor Importado": {
                "yaxis": {"title": "Valor Total Importado (US$)"},
                "hovertemplate": "<b>%{x}</b><br>U$ %{y}",
                "title": "Valor Total Importado nos Anos de Referência",
                "sup": "Gráfico de Linha exibindo o valor total de vinho importado (em US$) por país ao longo do tempo",
            },
            "Litros Importados": {
                "yaxis": {"title": "Total de Vinho Importados (Litros)"},
                "hovertemplate": "<b>%{x}</b><br>%{y} Litros",
                "title": "Total de Vinho Importados nos Anos de Referência",
                "sup": "Gráfico de Linha exibindo o volume total de vinho importado (em litros) por país ao longo do tempo",
            },
        }
        
        layout_info_selected = layout_info[config['metric']]

        layout_graphs(
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

def layout_graphs(
    fig: px,
    template: str = "seaborn",
    height: int = 500,
    margin: dict = {"l": 10, "r": 10, "b": 10, "t": 85, "pad": 5},
    legend: dict = {
        "orientation": "v",
        "yanchor": "middle",
        "xanchor": "center",
        "x": 1,
        "y": 0.5,
        "title": "",
        "itemsizing": "constant",
    },
    xaxis: dict = {"title": ""},
    yaxis: dict = {"title": ""},
    hovertemplate: str = "<b>%{x}</b><br>%{y}",
    title_text = "-",
    title_sup = "--",
    marker_color = '',
    line_color = '',
    other: dict = dict(),
) -> None:
    dic = dict(
        template=template,
        height=height,
        margin=margin,
        legend=legend,
        xaxis=xaxis,
        yaxis=yaxis,
        title={
            'text': f'{title_text}<br><sup style="color: #888; font-weight: normal;">{title_sup}</sup>',
            'xanchor': 'left',
            'xref': 'paper',
            'yanchor': 'auto',
            'x': 0,
            'y': .95,
            'font': {
                'size': 20,
                'color': '#666'
            }
        },
    )

    fig.update_layout(dic | other)
    
    if marker_color != '':
        fig.update_traces(marker_color = marker_color)
    if line_color != '':
        fig.update_traces(line_color = line_color)
    
    fig.update_traces(hovertemplate=hovertemplate)

    return None