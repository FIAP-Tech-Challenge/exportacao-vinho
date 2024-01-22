import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import requests

st.markdown("<p style='text-align: center; color:purple;font-size:54px'> Comercialização de Vinhos 💲</p>",  unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color:gray; font-size:24px'><b>Lorem Ipsum is simply dummy text of the printing and typesetting industry. Lorem Ipsum has been the industry's standard dummy text ever since the 1500s, when an unknown printer took a galley of type and scrambled it to make a type specimen book. It has survived not only five centuries, but also the leap into electronic typesetting, remaining essentially unchanged. It was popularised in the 1960s with the release of Letraset sheets containing Lorem Ipsum passages, and more recently with desktop publishing software like Aldus PageMaker including versions of Lorem Ipsum. </b></p>",  unsafe_allow_html=True)

url_com = 'https://raw.githubusercontent.com/FIAP-Tech-Challenge/exportacao-vinho/main/app/data/comercializacao.csv'
response_com = requests.get(url_com)     
if response_com.status_code == 200:
    # Assuming it's a text file
    content = response_com.text

    # Now, you can work with the content as needed
    with open('file_com.csv', 'w', encoding="utf-8") as local_file_com:
        local_file_com.write(content)
else:
    print(f"Failed to download file. Status code: {response_com.status_code}")   

with open(local_file_com.name, encoding="utf-8") as file:
    df = pd.read_csv(file, sep=';')

df = df.query('(`Produto` == "VINHO DE MESA") | (`Produto` == "VINHO FINO DE MESA") | (`Produto` == "VINHO FRIZANTES") | (`Produto` == "VINHO ORGÂNICO") | (`Produto` == "VINHO ESPECIAL") | (`Produto` == "SUCO DE UVAS")')
df = df.reset_index(drop=True)

df = df.set_index('Produto')

df.index = ['VINHO DE MESA', 'VINHO ORGÂNICO', 'VINHO ESPECIAL','SUCO DE UVAS']

df = df.drop(columns=['Prefixo'])

df = pd.DataFrame(df)
df.T.loc['1970':].plot(figsize=(12, 6))
plt.xticks(np.arange(0, len(df.columns), step=1), labels=df.columns)
plt.title("Valor anual da comercialização de vinhos")
plt.grid(linestyle = "--")
plt.xlabel("Anos")

st.pyplot(plt)