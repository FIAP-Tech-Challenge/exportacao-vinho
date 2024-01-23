import requests
import streamlit as st
import polars as pl
import plotly.express as px
from classes import funcao as f

st.markdown("<p style='text-align: center; color:purple;font-size:54px'> Importação de Vinhedos 🌏</p>",  unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color:gray; font-size:24px'><b>Nosso objetivo é expandir a área de atuação, encontrando novos países que possam estabelecer vínculos comerciais. </b></p>",  unsafe_allow_html=True)

st.markdown("<p style='text-align: justify; color:gray; font-size:18px'>Entre 2016 e 2019, o Chile se destacou como um dos principais países na importação de vinhos para o Brasil, alcançando um valor significativo de 1 milhão de dólares. Esse aumento foi impulsionado pelo fenômeno climático El Niño, que gerou uma demanda crescente no mercado. </p>",  unsafe_allow_html=True)

st.markdown("<p style='text-align: justify; color:gray; font-size:18px'>Ao analisarmos as possibilidades de parcerias de mercado, a Argentina surge como um potencial parceiro expressivo, com um montante considerável de US$ 752 milhões de dólares e Portugal US$ 654 milhões de dólares. </p>",  unsafe_allow_html=True)

st.markdown("""**Fonte de Dados:** [Banco de dados de uva, vinho e derivados](http://vitibrasil.cnpuv.embrapa.br/)""")

with st.expander("↓ Download dos Arquivos", expanded=False):
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
        btn = st.download_button(
            label="📊 Baixar CSV importação vinho",
            data=file,
            file_name="importacao.csv",
            mime='text/csv',
            type='primary',
            key="download_csv_imp"
        )

st.markdown("<div style='margin-bottom: 40px'></div>", unsafe_allow_html=True)

df = pl.read_csv("https://raw.githubusercontent.com/FIAP-Tech-Challenge/exportacao-vinho/main/app/data/importacao.csv",truncate_ragged_lines=True)

f.tab_intro(df)

