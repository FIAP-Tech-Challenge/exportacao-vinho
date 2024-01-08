import streamlit as st

st.set_page_config(
    page_title="FIAP - Vinhos",
    page_icon="🍷",
)

st.markdown("<p style='text-align: center; color:white; font-size:54px'> Bem vindo a nossa página 👋 </p>",  unsafe_allow_html=True)

st.markdown(
        "<p style='text-align: center; color:MediumPurple; font-size:24px'> Lideramos o mercado nacional nos quesitos de Produção, Processamento, Comercialização, Importação e Exportação de vinhos </p>",  unsafe_allow_html=True
    )

st.markdown(
"<p style='text-align: justify; color:white; font-size:18px'> Essa página tem o intuito de demonstrar a administração geral da empresa fatores que possam influenciar diretamente e indiretamente a cadeia produtiva de vinhos, desde a produção das safras até a exportação. </p>",  unsafe_allow_html=True
    )

st.markdown(
"<p style='text-align: justify; color:white; font-size:18px'> A página foi divida de forma segmentada com intuito de facilitar o entendimento dos gestores acerca de toda cadeia produtiva. Ao clicar em cima de cada tópico no menu ao lado esquerdo da página (👈), será possível analisar os insights extraídos pela equipe de dados. </p>",  unsafe_allow_html=True
    )

st.image('images/cacho_uvas.jpg', caption='Fonte: Imagem de sergiorojoes no Freepik')