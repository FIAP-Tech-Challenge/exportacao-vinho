import streamlit as st
import polars as pl
import plotly.express as px
from . import graphs as g
from . import functions as f
from . import structure as s

def struct_graph_1(df: pl.DataFrame) -> None:   
    config_graph = {}
    cols = st.columns([2, 1], gap="large")
    
    with cols[1]:      
        with st.expander("⚙️ Configuração do Gráfico", expanded=False):
            metric = st.selectbox(
                "Métrica",
                ("Valor Exportado", "Litros Exportados"),
                key="metric_graph_two",
            )
            agg = st.selectbox(
                "Visualização", ("Valor Total", "Valor Médio"),
                key="agg_graph_two",
            )
        
        config_graph["metric"] = metric
        config_graph["agg"] = agg
        struct_description('Podemos observar a relação do valor exportado em US$ desde a 1970, o Chile significa nosso principal exportador de vinhos.<br><br>\
                            Notem no mesmo gráfico que o valor médio das importações (preço médio de cada país por exportação), verifique que os países da América do Norte mais importam, isto é, embora uma quantidade menor o valor consumido é maior.')
            
    with cols[0]:      
        fig = g.graph_1(df, config_graph)
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.markdown("<div style='margin-bottom: 30px'></div>", unsafe_allow_html=True)

    return None

def struct_graph_2(df: pl.DataFrame) -> None:    
    config_graph = {}
    cols = st.columns([2, 1], gap="large")
       
    with cols[1]:
        with st.expander("⚙️ Configuração do Gráfico", expanded=False):
            year = st.slider(
                "Período", 1970, 2022, (1970, 2022),
                key="year_graph_three"
            )
            metric = st.selectbox(
                "Métrica",
                ("Valor Exportado", "Litros Exportados"),
                key="metric_graph_three",
            )
            agg = st.selectbox(
                "Visualização",
                ("Valor Total", "Valor Médio"),
                key="agg_graph_three",
            )
        
        config_graph["metric"] = metric
        config_graph["agg"] = agg
        config_graph["year"] = year
        struct_description('O continente das Américas (Sul, Central e Norte) é o principal destino das exportações. O Paraguai é nosso maior importador, seguido dos Estados Unidos e Rússia.<br><br>Esta relação entre Brasil e Paraguai é explicado por serem os únicos países cujos vinhos são de castas americanas e híbridas pre-dominantes <a target="_blank" href="https://web.bndes.gov.br/bib/jspui/bitstream/1408/2603/1/BS%2019%20Desafios%20da%20vitinicultura%20brasileira_P.pdf">[Fonte]</a>.')
            
    with cols[0]:       
        fig = g.graph_2(df, config_graph)
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.markdown("<div style='margin-bottom: 30px'></div>", unsafe_allow_html=True)

    return None

def struct_graph_3(df: pl.DataFrame) -> None:    
    config_graph = {}
    cols = st.columns([2, 1], gap="large")
    
    with cols[1]:
        with st.expander("⚙️ Configuração do Gráfico", expanded=False):
            metric = st.selectbox(
                "Métrica",
                ("Valor Exportado", "Litros Exportados"),
                key="metric_graph_3",
            )
            viz = st.selectbox("Visualização", ("Top 3 Países", "Customizar"), key="viz_graph_3")
            
            var = {"Valor Exportado": "value", "Litros Exportados": "liters"}
            col_name = var[metric]
            
            if viz == "Customizar":
                list_name = (
                    df.select(pl.col("country"), pl.col(col_name))
                    .group_by("country")
                    .agg(pl.sum(col_name))
                    .sort(col_name, descending=True)
                    .select(pl.col("country"))
                    .to_series()
                    .to_list()
                )
                config_graph['list_selected'] = st.multiselect("Paises selecionados", list_name)
            
        
        config_graph["metric"] = metric
        config_graph["viz"] = viz
        config_graph["col_name"] = col_name
        struct_description('Apesar da exportação de vinho em sua maioria para o Paraguai, os Estados Unidos e Rússia são mercados em potencial crescimento, e ao longo dos anos, ultrapassando o Paraguai em valor total importado.')
            
    with cols[0]:
        
        fig = g.graph_3(df, config_graph)
        st.plotly_chart(fig, use_container_width=True)

    st.divider()
    st.markdown("<div style='margin-bottom: 30px'></div>", unsafe_allow_html=True)

    return None

def struct_description(text: str) -> None:
    st.markdown(
        f"""
        <div style="background: #f8f8f8; padding: 20px 25px 10px 20px; border-radius: 5px; border: 1px solid #ddd; margin-bottom: 100px">
            <p style="text-align: left; font-size:13px; color: #bbb">
                💡 Análise
            </p>
            <p style="text-align: left;">
                {text}
            </p>
        </div>
        """,
        unsafe_allow_html=True,
    )

    return None

def header() -> None:
    st.markdown("<p style='text-align: center; color:violet; font-size:72px'> FIAP - Vinhos </p>",  unsafe_allow_html=True)
    
    st.markdown(
        "<p style='text-align: center; color:white; font-size:24px'> Somos a empresa número 1 que mais exporta vinhos do Brasil para o mundo. </p>",  unsafe_allow_html=True
    )

    st.markdown(
        """ :gray[Nosso objetivo é crescer nossas vendas e expandir a área de atuação, encontrando novos países que possam estabelecer vínculos comerciais.]"""
    )
    st.markdown(    
        """**Fonte de Dados:** [Banco de dados de uva, vinho e derivados](http://vitibrasil.cnpuv.embrapa.br/)"""
    )
 
    with st.expander("↓ Download dos Arquivos", expanded=False):
        with open('/data/ExpVinho.csv', 'rb') as file:
            btn = st.download_button(
                label="📊 Baixar CSV exportação vinho",
                data=file,
                file_name="expVinho.csv",
                mime='text/csv',
                type='primary',
                key="download_csv_exp"
            )

        with open('/data/pais.csv', 'rb') as file:
            btn = st.download_button(
                label="📊 Baixar CSV países",
                data=file,
                file_name="pais.csv",
                mime='text/csv',
                type='primary',
                key="download_csv_pais"
            )
            
        with open('/data/dataframe_final.csv', 'rb') as file:
            btn = st.download_button(
                label="📊 Baixar CSV completo",
                data=file,
                file_name="data.csv",
                mime='text/csv',
                type='primary',
                key="download_csv"
            )
            
    st.markdown("<div style='margin-bottom: 40px'></div>", unsafe_allow_html=True)


    return None

def tab_intro(df: pl.DataFrame) -> None:
    config_graph = {}
    config_graph["col_name"] = "value"
    config_graph["metric"] = "Valor Exportado"
    config_graph["viz"] = "Visualização"
    
    cols1, cols2 = st.columns(spec=[2, 2])
    with cols1:
        st.plotly_chart(g.graph_3(df, config_graph))
    with cols2:
        st.plotly_chart(g.graph_globe(df), use_container_width=True)

    st.markdown(
        """
        ###### Tabela com informações sobre a exportação de vinho
        Tabela contém informações sobre a exportação de vinho, como país de origem e de destino, ano de referência, quantidade de vinho exportado (em litros) e valor total exportado (em US$)
        """
    )
    st.dataframe(g.table_info(df), use_container_width=True)

    return None


def tab_tabela(df: pl.DataFrame) -> None:
    st.markdown(
        """
        ###### Tabela Geral
        Tabela contém informações sobre a exportação de vinho e os paises de destino
        """
    )
    
    with st.expander("📄 Descrição dos Campos", expanded=False):
        st.markdown(
            """
                **País de Origem**: País onde o vinho foi produzido
                \n**País de Destino**: País onde o vinho foi exportado
                \n**Ano de Referência**: Ano em que a exportação foi realizada
                \n**Vinho Exportado (Litros)**: Quantidade Total Exportado (em Litros)                
                \n**Valor Exportado (US\$)**: Valor Total Exportado (em US\$)
                \n**Preço do Vinho (US\$/Litro)**: Preço do Vinho em US\$/Litro
            """
        )
    df_aux = (
        df.select(
            pl.lit("Brasil").alias("País de Origem"),
            pl.col("country").alias("País de Destino"),
            pl.col("year").alias("Ano de Referência"),
            pl.col("liters").alias("Vinho Exportado (Litros)"),
            pl.col("value").alias("Valor Exportado (US$)"),
        )
        .fill_nan(0)
        .fill_null(0)
    )

    st.dataframe(
        df_aux,
        use_container_width=True,
        column_config={
            "Valor Exportado (US$)": st.column_config.NumberColumn(
                "Valor Exportado (US$)",
                help="Valor Total Exportado (em US\$)",
                format="US$ %.2f",
            ),
            "Preço do Vinho (US$/Litro)": st.column_config.NumberColumn(
                "Preço do Vinho (US$/Litro)",
                help="Preço do Vinho em US\$/Litro",
                format="US$ %.2f",
            ),
        },
    )

    return None


def tab_graph(df: pl.DataFrame) -> None:
    st.markdown("<div style='margin-bottom: 40px'></div>", unsafe_allow_html=True)
    
    s.struct_graph_1(df)
    s.struct_graph_2(df)
    s.struct_graph_3(df)

    return None