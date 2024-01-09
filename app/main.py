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

url_exp = 'https://github.com/FIAP-Tech-Challenge/exportacao-vinho/blob/9236ecf980bb469685605ee5588cd6c6767ea544/app/images/cacho_uvas.jpg'
    response_exp = requests.get(url_exp)     
    if response_exp.status_code == 200:
        # Assuming it's a text file
        content = response_exp.text

        # Now, you can work with the content as needed
        with open('cacho_uvas.jpg', 'w') as local_file_exp:
            local_file_exp.write(content)
    else:
        print(f"Failed to download file. Status code: {response_exp.status_code}")   
st.image(url_exp, caption='Fonte: Imagem de sergiorojoes no Freepik')