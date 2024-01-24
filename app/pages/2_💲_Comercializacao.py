import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import urllib.request
from PIL import Image
import requests

st.markdown("<p style='text-align: center; color:purple;font-size:54px'> Comercialização de Vinhos 💲</p>",  unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color:gray; font-size:24px'><b>Agora começamos a falar sobre dinheiro 💸</b></p>",  unsafe_allow_html=True)

url_com = "https://github.com/FIAP-Tech-Challenge/exportacao-vinho/blob/675dae91cd926352e9f23f991d3ad8c7dde74172/app/images/vinho-vida-rural.jpg?raw=true"

with urllib.request.urlopen(url_com) as url_obj_com:
    img_com = np.array(Image.open(url_obj_com))
    st.image(img_com, width=400, caption='Fonte: Google', use_column_width=True)

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

df = df.query('(`Produto` == "VINHO DE MESA") | (`Produto` == "VINHO  FINO DE MESA") | (`Produto` == "SUCO DE UVAS") | (`Produto` == "OUTROS PRODUTOS COMERCIALIZADOS")')
df = df.reset_index(drop=True)
df = df.set_index('Produto')
df.index = ['VINHO DE MESA', 'VINHO FINO DE MESA', 'SUCO DE UVA', 'DERIVADOS']
df = df.drop(columns=['Prefixo', 'ID'])
df = pd.DataFrame(df)
df_milhares = df / 1000000

st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>O vinho de mesa notoriamente é o produto mais comercializado na região do Rio Grande do Sul, destaca-se o ano de 2005, com um pico de vendas atingindo o valor de R$271 mil. No entanto, observamos uma queda nas vendas em 2008, totalizando apenas U$200 milhões, e também em 2016, totalizando apenas U$166 milhões, atribuída, em parte, às condições climáticas adversas, influenciadas pelo fenômeno El Niño no Brasil.</p>",  unsafe_allow_html=True
    )

st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>Outro insight importante é sobre o suco de uva que está conquistando espaço no mercado da região do Rio Grande do Sul, registrando um faturamento em 2019 de R$147 mil. Essa cifra o coloca como um potencial produto que está próximo do nosso líder, o Vinho de Mesa, que alcançou um faturamento de R$180 mil no mesmo período. Abaixo podemos ver mais claramente essas informações: </p>",  unsafe_allow_html=True
    )

st.markdown(
"<p style='text-align: center; color:gray; font-size:18px'>Valor comercializado de produtos feitos com uva em (U$)</p>",  unsafe_allow_html=True
    )

st.line_chart(df_milhares.T.loc['2005':])

st.markdown(
"<p style='text-align: center; color:gray; font-size:18px'>Não podemos falar de comercialização sem falar da importação e exportação de vinhos.</p>",  unsafe_allow_html=True
    )

st.link_button('Importação de Vinhos', "https://exportacao-vinho.streamlit.app/Importacao", use_container_width=True)

st.link_button('Exportação de Vinhos', "https://exportacao-vinho.streamlit.app/Exportacao", use_container_width=True)

#df.T.plot(figsize=(12, 6))
#plt.xticks(np.arange(16, len(df.columns), step=1), labels=df.columns)
#plt.title("Valor anual da comercialização de vinhos")
#plt.grid(linestyle = "--")
#plt.xlabel("Anos")

#st.pyplot(plt)

#df = df.query('(`Produto` == "VINHO DE MESA") | (`Produto` == "VINHO FINO DE MESA") | (`Produto` == "VINHO FRIZANTES") | (`Produto` == "VINHO ORGÂNICO") | (`Produto` == "VINHO ESPECIAL") | (`Produto` == "SUCO DE UVAS")')
#df = df.reset_index(drop=True)

#df = df.set_index('Produto')

#df.index = ['VINHO DE MESA', 'VINHO ORGÂNICO', 'VINHO ESPECIAL','SUCO DE UVAS']

#df = df.drop(columns=['Prefixo'])
#df = df.drop(columns=['ID','1970', '1971', '1972', '1973', '1974', '1975', '1976', '1977',
#       '1978', '1979', '1980', '1981', '1982', '1983', '1984', '1985', '1986',
#       '1987', '1988', '1989', '1990', '1991', '1992', '1993', '1994', '1995',
#       '1996', '1997', '1998', '1999', '2000', '2001', '2002', '2003'])

#df = pd.DataFrame(df)
#df.T.loc['2004':].plot(figsize=(12, 6))
#plt.xticks(np.arange(0, len(df.columns), step=1), labels=df.columns)
#plt.title("Valor anual da comercialização de vinhos")
#plt.grid(linestyle = "--")
#plt.xlabel("Anos")

#st.pyplot(plt)

#st.markdown(
#    "<p style='text-align: justify; color:gray; font-size:18px'> Contudo, mesmo com os excelentes números das vendas de nossos vinhos, houve uma compensação no número de produtos importados, que podemos analisar na próxima apresentação.</p>",  unsafe_allow_html=True
#)

#st.link_button('Importação de Vinhos', "https://exportacao-vinho.streamlit.app/Importacao", use_container_width=True)
