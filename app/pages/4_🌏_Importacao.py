import streamlit as st
import polars as pl
import plotly.express as px
import requests
from . import funcao as f0

url_imp = 'https://raw.githubusercontent.com/FIAP-Tech-Challenge/exportacao-vinho/main/app/data/importacao.csv'
response_imp = requests.get(url_imp)     
if response_imp.status_code == 200:
    # Assuming it's a text file
    content = response_imp.text

    # Now, you can work with the content as needed
    with open('file_imp.csv', 'w') as local_file_imp:
        local_file_imp.write(content)
else:
    print(f"Failed to download file. Status code: {response_imp.status_code}")   

with open(local_file_imp.name) as file:
    df = pl.read_csv(local_file_imp,truncate_ragged_lines=True)

st.markdown("<p style='text-align: center; color:purple;font-size:54px'> Importação de Vinhedos 🌏</p>",  unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color:gray; font-size:24px'><b>Nosso objetivo é crescer nossas vendas e expandir a área de atuação, encontrando novos países que possam estabelecer vínculos comerciais. </b></p>",  unsafe_allow_html=True)

st.markdown("<p style='text-align: justify; color:gray; font-size:18px'>Nesta breve introdução, percebemos que na década de 90, os Estados Unidos apresentou ser o principal parceiro comercial, porém houve um decréscimo nos últimos anos. </p>",  unsafe_allow_html=True)

st.markdown("<p style='text-align: justify; color:gray; font-size:18px'>Entre 2013, a Rússia, destaca-se como um outlier em nossa análise.. </p>",  unsafe_allow_html=True)

st.markdown("""**Fonte de Dados:** [Banco de dados de uva, vinho e derivados](http://vitibrasil.cnpuv.embrapa.br/)""")


with open(local_file_imp.name) as file:
    btn = st.download_button(
        label="📊 Baixar CSV importação vinho",
        data=file,
        file_name="importacao.csv",
        mime='text/csv',
        type='primary',
        key="download_csv_imp"
    )

st.markdown("<div style='margin-bottom: 40px'></div>", unsafe_allow_html=True)

f.tab_intro(df)

