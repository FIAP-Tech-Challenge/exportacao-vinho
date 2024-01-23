import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import urllib.request
from PIL import Image
import requests

st.markdown("<p style='text-align: center; color:purple; font-size:54px'> Produção de Vinhedos 🍇 </p>",  unsafe_allow_html=True)

st.markdown(
"<p style='text-align: center; color:gray; font-size:24px'><b>A produção de vinhos é essencial para garantir que todas as outras fases tenham um resultado positivo. Para o vinho chegar até a mesa do consumidor, existe um longo caminho, desde a colheita até o momento do engarrafamento. Para complementar nossa análise, traremos as informações segregadas abaixo</b></p>",  unsafe_allow_html=True
    )

tab1, tab2, tab3, tab4, tab5, tab6 = st.tabs(["Plantio", "Colheita", "Industrialização", "Fermentação", "Armazenamento", "Engarrafamento"])

with tab1:
    st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>Tudo começa no vinhedo, campo de plantação das uvas. Ele é planejado minuciosamente para oferecer as melhores condições às uvas, como a posição das frutas em relação ao sol.</p>",  unsafe_allow_html=True
    )

    url_plantio = "https://github.com/FIAP-Tech-Challenge/exportacao-vinho/blob/809941f30a3862ec38ce044d0f92a5e44de17d21/app/images/plantio.png?raw=true"

    with urllib.request.urlopen(url_plantio) as url_obj_plantio:
        img_plantio = np.array(Image.open(url_obj_plantio))
        st.image(img_plantio, width=400, caption='Fonte: Divvino Blog', use_column_width=True)

with tab2:
    st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>No instante da colheita, as frutas são verificadas atentamente – a fim de encontrar inconformidades – e selecionadas manualmente. Ainda no momento da colheita, são feitos diversos testes para saber se é o momento ideal para retirá-las, visto que, caso haja antecipação ou atraso do processo, as uvas podem perder a qualidade.</p>",  unsafe_allow_html=True
    )

    url_colheita = "https://github.com/FIAP-Tech-Challenge/exportacao-vinho/blob/809941f30a3862ec38ce044d0f92a5e44de17d21/app/images/colheita.png?raw=true"

    with urllib.request.urlopen(url_colheita) as url_obj_colheita:
        img_colheita = np.array(Image.open(url_obj_colheita))
        st.image(img_colheita, width=400, caption='Fonte: Divvino Blog', use_column_width=True)

with tab3:
    st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>Para produzir vinhos brancos, as uvas são transportadas para dois cilindros responsáveis pela extração do suco. Durante essa extração as uvas liberam os taninos suaves que estão presentes nas cascas e sementes.</p>",  unsafe_allow_html=True
    )
    st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>Para produzir vinhos tintos,  extração é realizada por gravidade: as uvas ficam dispostas uma em cima das outras dentro de um tanque de aço inox. Com o peso comprimido das frutas, o líquido é extraído.</p>",  unsafe_allow_html=True
    )

    url_industria = "https://github.com/FIAP-Tech-Challenge/exportacao-vinho/blob/809941f30a3862ec38ce044d0f92a5e44de17d21/app/images/industrializacao.png?raw=true"

    with urllib.request.urlopen(url_industria) as url_obj_industria:
        img_industria = np.array(Image.open(url_obj_industria))
        st.image(img_industria, width=400, caption='Fonte: Divvino Blog', use_column_width=True)

with tab4:
    st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>Nesses mesmos tanques acontece a fermentação, o que significa a adição de fungos para fazer a substituição e transformação do açúcar da fruta em álcool e gás carbônico.</p>",  unsafe_allow_html=True
    )

    url_fermentacao = "https://github.com/FIAP-Tech-Challenge/exportacao-vinho/blob/809941f30a3862ec38ce044d0f92a5e44de17d21/app/images/fermentacao.jpg?raw=true"

    with urllib.request.urlopen(url_fermentacao) as url_obj_fermentacao:
        img_fermentacao = np.array(Image.open(url_obj_fermentacao))
        st.image(img_fermentacao, width=400, caption='Fonte: Divvino Blog', use_column_width=True)

with tab5:
    st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>Teoricamente, ao fim da fermentação, o vinho já está pronto. Entretanto, deve ser armazenado para que as substâncias presentes na bebida possam “ganhar corpo” e sabor. Geralmente, são usados barris de carvalho para esse armazenamento, com a finalidade de fazer o líquido entrar em contato com a madeira.</p>",  unsafe_allow_html=True
    )

    url_armazem = "https://github.com/FIAP-Tech-Challenge/exportacao-vinho/blob/809941f30a3862ec38ce044d0f92a5e44de17d21/app/images/armazenamento.png?raw=true"

    with urllib.request.urlopen(url_armazem) as url_obj_armazem:
        img_armazem = np.array(Image.open(url_obj_armazem))
        st.image(img_armazem, width=400, caption='Fonte: Divvino Blog', use_column_width=True)

with tab6:
    st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>Após um período que pode durar de seis meses a um ano e meio, os vinhos são engarrafados e guardados na posição horizontal, para o contato com a rolha e o bloqueio da entrada do oxigênio, ocasionando a perda de sabor.</p>",  unsafe_allow_html=True
    )

    url_engarrafa= "https://github.com/FIAP-Tech-Challenge/exportacao-vinho/blob/809941f30a3862ec38ce044d0f92a5e44de17d21/app/images/engarrafamento.jpg?raw=true"

    with urllib.request.urlopen(url_engarrafa) as url_obj_engarrafa:
        img_engarrafa = np.array(Image.open(url_obj_engarrafa))
        st.image(img_engarrafa, width=400, caption='Fonte: Divvino Blog', use_column_width=True)

st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>Com essa breve descrição partiremos para análise dos dados de produção da base do Embrapa conforme sugerido pela Head de dados. Primeiramente, resolvemos separar a base de dados em categórias mais genéricas. Elas são divididas em quatro: Vinho de mesa, Vinho Fino de Mesa, Suco e Derivados. A partir desse gráfico, conseguimos ter uma ideia dos últimos 15 anos qual das categorias é mais produzida dentre as presentes nessa análise:</p>",  unsafe_allow_html=True
    )

url_prod = 'https://raw.githubusercontent.com/FIAP-Tech-Challenge/exportacao-vinho/main/app/data/producao.csv'
response_prod = requests.get(url_prod)     
if response_prod.status_code == 200:
    # Assuming it's a text file
    content = response_prod.text

    # Now, you can work with the content as needed
    with open('file_prod.csv', 'w') as local_file_prod:
        local_file_prod.write(content)
else:
    print(f"Failed to download file. Status code: {response_prod.status_code}")   

with open(local_file_prod.name) as file:
    dados = pd.read_csv(file, sep=';', encoding='ISO-8859-1')
    dados_gerais = dados.drop('id', axis=1)
    dados_gerais = dados_gerais.query('(produto == "VINHO DE MESA") | (produto == "VINHO FINO DE MESA (VINIFERA)") | (produto == "SUCO") | (produto == "DERIVADOS")')
    dados_gerais = dados_gerais.reset_index(drop=True)
    dados_gerais = dados_gerais.set_index('produto')
    dados_gerais.index = ['VINHO DE MESA', 'VINHO FINO DE MESA (VINIFERA)', 'SUCO','DERIVADOS']
    dados_gerais_milhares = dados_gerais / 1000000

st.markdown(
"<p style='text-align: center; color:gray; font-size:18px'>Produção em Milhões de Litros de produtos feitos com uva</p>",  unsafe_allow_html=True
    )

st.line_chart(dados_gerais_milhares.T.loc['2007':])

st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>Deste gráfico, podemos tirar diversas conclusões, a mais clara e evidente é que os vinhos de mesa são os artigos mais produzidos pela Embrapa, seguidos dos derivados, sucos e por último os vinhos finos de mesa.</p>",  unsafe_allow_html=True
    )

st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>Analisando esse gráfico mais profundamente, é notório que no ano de 2016 houve uma queda considerável na produção de todas as categórias, precisamos extrair mais insights para ver o que ocorreu para ocasionar essa baixa.</p>",  unsafe_allow_html=True
    )

st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>O clima é um dos principais elementos que interferem na produção de uvas, influenciando na escolha do local de plantio, no desenvolvimento dos vinhedos implantados, no potencial vegetativo, na qualidade dos frutos, etc (DE MOURA, 2009). Por este motivo, buscamos dados climáticos nas principais regiões onde se cultivam uvas no Brasil, essas base de dados podem ser encontradas no site do INMETRO. Após fazer o devido tratamento, conseguimos obter os dados de precipitação total e umidade média na cidade de Porto Alegre (RS) nos últimos 15 anos. </p>",  unsafe_allow_html=True
    )

def tratar_dados_imet():
    dados_imet_rs_prec_lista = []
    dados_imet_rs_umd_lista = []

    for i in range(0,16):
        url = f'https://raw.githubusercontent.com/FIAP-Tech-Challenge/exportacao-vinho/main/app/data/INMET_S_RS_A801_PORTO%20ALEGRE_{2007+i}.CSV'
       
        response = requests.get(url)     
        if response.status_code == 200:
            # Assuming it's a text file
            content = response.text

            # Now, you can work with the content as needed
            with open(f'INMET_S_RS_A801_PORTO ALEGRE_{2007+i}.csv', 'w', encoding="utf-8") as local_file:
                local_file.write(content)
        else:
            print(f"Failed to download file. Status code: {response_prod.status_code}") 
        
        dados_imet_rs = pd.read_csv(f'INMET_S_RS_A801_PORTO ALEGRE_{2007+i}.csv', encoding='ISO-8859-1', sep=';',skiprows=8)

        dados_imet_rs['PRECIPITACAO TOTAL, HORARIO (mm)'] = dados_imet_rs['PRECIPITACAO TOTAL, HORARIO (mm)'].str.replace(',','.')
        dados_imet_rs['PRECIPITACAO TOTAL, HORARIO (mm)'] = dados_imet_rs['PRECIPITACAO TOTAL, HORARIO (mm)'].astype('float')
        dados_imet_rs = dados_imet_rs[dados_imet_rs['PRECIPITACAO TOTAL, HORARIO (mm)'] >= 0]
        dados_imet_rs_prec_lista.append(dados_imet_rs['PRECIPITACAO TOTAL, HORARIO (mm)'].sum())
        dados_imet_rs_umd_lista.append(dados_imet_rs['UMIDADE RELATIVA DO AR, HORARIA (%)'].mean())
    return dados_imet_rs_prec_lista, dados_imet_rs_umd_lista
dados_imet_rs_listas = tratar_dados_imet()
dic_imet = {'Ano': np.arange(2007,2023), 'Precipitacao_Total': dados_imet_rs_listas[0], 'Umidade_Media_%': dados_imet_rs_listas[1]}
df_imet_tratado = pd.DataFrame(data = dic_imet)
df_imet_tratado2 = df_imet_tratado.set_index('Ano')
st.dataframe(df_imet_tratado2.style.highlight_max(axis=0), width=720)

st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>Os campos destacados mostram os maiores valores de precipitação total (No ano de 2015) e umidade relativa média (No ano de 2018). Para termos uma melhor ideia dos dados climáticos nos últimos 15 anos, fizemos dois gráficos de barras: </p>",  unsafe_allow_html=True
    )

st.markdown(
"<p style='text-align: center; color:gray; font-size:18px'>Precipitação Total (mm) por ano em Porto Alegre - RS</p>",  unsafe_allow_html=True
    )
st.bar_chart(data=df_imet_tratado, x='Ano', y='Precipitacao_Total')

st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>No primeiro gráfico de barras notamos uma precipitação total acima da média no ano de 2015 levando em consideração os últimos 15 anos. Logo, podemos inferir que o excesso de chuvas nesse ano afetou diretamente a produção de uvas no ano de 2016, ocasionando uma brusca queda conforme mostrado no primeiro gráfico de linhas. O excesso de chuvas pode estar correlacionado com o fenômeno do Super El Nino que ocorreu entre os anos de 2015 e 2016, acentuando inundações na região sul e uma grande seca nas regiões ao norte do Brasil.</p>",  unsafe_allow_html=True
    )

st.markdown(
"<p style='text-align: center; color:gray; font-size:18px'>Umidade média por ano em Porto Alegre - RS</p>",  unsafe_allow_html=True
    )
st.bar_chart(data=df_imet_tratado, x='Ano', y='Umidade_Media_%')

st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>Já no segundo gráfico de barras não foi possível tirar conclusões se a umidade média afetou de algum modo a produção.</p>",  unsafe_allow_html=True
    )

st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'>Agora que conseguimos extrair os dados de produção das categorias gerais, iremos focar na produção dos vinhos de mesa. Os vinhos de mesa possuem 3 tipos: Tinto, Branco e Rosado. No gráfico abaixo, podemos ver que o carro forte de produção de vinhos da Embrapa são os vinhos tintos, seguido pelo vinho branco e por último o vinho rosado.</p>",  unsafe_allow_html=True
    )

df_vinho_mesa = dados.drop('id', axis = 1)
df_vinho_mesa = df_vinho_mesa[1:4]
df_vinho_mesa = df_vinho_mesa.reset_index(drop=True)
df_vinho_mesa = df_vinho_mesa.set_index('produto')
df_vinho_mesa_milhares = df_vinho_mesa / 1000000
df_vinho_mesa_milhares['2017'][0] = 217.527985
df_vinho_mesa_milhares['2017'][1] = 36.121245
df_vinho_mesa_milhares['2017'][2] = 1.365957

st.markdown(
"<p style='text-align: center; color:gray; font-size:18px'>Produção em Milhões de Litros de vinhos de mesa</p>",  unsafe_allow_html=True
    )
st.line_chart(df_vinho_mesa_milhares.T.loc['2007':])

st.markdown(
"<p style='text-align: justify; color:gray; font-size:18px'> Assim como constatado no gráfico das categorias gerais anteriormente, vemos que a queda de produção em 2016 se confirma mais uma vez. Veremos se esse mesmo efeito ocorre com a comercialização de vinhos.</p>",  unsafe_allow_html=True
    )

st.link_button('Comercialização de Vinhos', "https://exportacao-vinho.streamlit.app/Comercializacao", use_container_width=True)