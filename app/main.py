import streamlit as st
import urllib.request
from PIL import Image
import numpy as np

st.set_page_config(
    page_title="FIAP - Vinhos",
    page_icon="🍷",
)

st.markdown("<p style='text-align: center; color:purple; font-size:54px'> Bem vindo a nossa página 👋 </p>",  unsafe_allow_html=True)

st.markdown(
        "<p style='text-align: center; color:gray; font-size:24px'><b> O Tech Challenge – FIAP é o projeto que integra os conhecimentos adquiridos na fase 1 do curso Data Analytics.</b> </p>",  unsafe_allow_html=True
    )

st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'> Somos uma empresa especializada na exportação de vinhos brasileiros para mercados globais. Nossa equipe de Data Analytics desempenha um papel crucial na geração de relatórios iniciais, os quais apresentaremos aos acionistas e investidores. Esses relatórios destacam nosso potencial de mercado e identifica oportunidades para novos negócios. Estamos comprometidos em fornecer análises abrangentes que respaldam decisões estratégicas e impulsionam o crescimento sustentável da nossa empresa. </p>",  unsafe_allow_html=True
    )

st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'> A página foi divida de forma segmentada com intuito de facilitar o entendimento dos gestores acerca de toda cadeia produtiva. Ao clicar em cima de cada tópico no menu ao lado esquerdo da página (👈), será possível analisar os insights extraídos pela equipe de dados. </p>",  unsafe_allow_html=True
    )

url = "https://github.com/FIAP-Tech-Challenge/exportacao-vinho/blob/9236ecf980bb469685605ee5588cd6c6767ea544/app/images/cacho_uvas.jpg?raw=true"

with urllib.request.urlopen(url) as url_obj:
    img = np.array(Image.open(url_obj))
    st.image(img, width=400, caption='Fonte: Imagem de sergiorojoes no Freepik', use_column_width=True)

st.markdown(
"<p style='text-align: center; color:gray; font-size:18px'> Convido você a conhecer um pouco do processo de produção de vinhedos</p>",  unsafe_allow_html=True
    )

st.link_button('Produção de Vinhedos', "https://exportacao-vinho.streamlit.app/Producao_e_Processamento", use_container_width=True)

#st.markdown(    
#    """**Veja nossa revista:** [FIAP Tech Challenge](https://my.visme.co/view/1jkord63-new-project)"""
#)
