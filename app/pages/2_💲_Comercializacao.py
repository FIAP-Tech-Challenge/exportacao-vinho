import streamlit as st
import pandas as pd 
import numpy as np
import matplotlib.pyplot as plt
import requests

st.markdown("<p style='text-align: center; color:purple;font-size:54px'> Comercialização de Vinhos 💲</p>",  unsafe_allow_html=True)

st.markdown("<p style='text-align: center; color:gray; font-size:24px'><b>Agora começamos a falar sobre dinheiro 💸</b></p>",  unsafe_allow_html=True)

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