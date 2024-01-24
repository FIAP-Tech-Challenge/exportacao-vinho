import streamlit as st
import requests
import pandas as pd 
import time
import plotly.express as px
import requests


def formata_numero(valor, prefixo = ''):
    for unidade in ['', 'mil']:
        if valor <1000:
            return f'{prefixo} {valor:.2f} {unidade}'
        valor /= 1000
    return f'{prefixo} {valor:.2f} milhões'

# Incialiazaçao do ambiente: venv\Scripts\activate , streamlit run main.py

st.set_page_config(layout='wide')

st.markdown("<p style='text-align: center; color:purple; font-size:54px'> Exportação de Vinhedos 🍷 </p>",  unsafe_allow_html=True)

url_exp = 'https://raw.githubusercontent.com/FIAP-Tech-Challenge/exportacao-vinho/main/app/data/exportacao.csv'
response_exp = requests.get(url_exp)     
if response_exp.status_code == 200:
    # Assuming it's a text file
    content = response_exp.text

    # Now, you can work with the content as needed
    with open('file_exp.csv', 'w', encoding="utf-8") as local_file_exp:
        local_file_exp.write(content)
else:
    print(f"Failed to download file. Status code: {response_exp.status_code}")   

with open(local_file_exp.name, encoding="utf-8") as file:
    df = pd.read_csv(file, sep=';', skiprows = 1)

@st.cache_data
def converte_csv(df):
    return df.to_csv(index = False).encode('utf-8')

def mensagem_sucesso():
    sucesso = st.success('Arquivo baixado com sucesso!', icon = "✅")
    time.sleep(5)
    sucesso.empty()

anos = list(range(1970,2007)) # Criando uma lista entre 1970 e 2006
anos = list(map(str,anos)) # Convertendo todos os valores da lista para string
anos_aux = [ano + '.1' for ano in anos] # copiando a lista porém adicionando o pós fixo '.1'
anos_final = anos + anos_aux # concatenando as duas listas

df = df.drop(anos_final, axis=1) # removendo colunas não necessárias

columns_to_melt = list(df.columns) # criando a lista de colunas
columns_to_melt.pop(0) # deletando a coluna Id
columns_to_melt.pop(0) # deletando a coluna país

dados_vinho = df.melt(
    id_vars = ['Id','País'],
    value_vars = columns_to_melt,
    var_name = 'ano',
    value_name = 'valor'
) # Derretando o Dataframe deixando apenas as colunas Id e país fixas

dados_vinho['Medida'] = dados_vinho['ano'].apply(lambda valor: 'Valor' if valor.endswith('.1') else 'Quantidade') # Aplicando regra para nomeação de medida
dados_vinho['ano'] = dados_vinho['ano'].str.replace('.1','') # Removendo .1 do ano
dados_vinho['ano'] = dados_vinho['ano'].replace({'21':'2011', '22':'2012', '23':'2013', '24':'2014','25':'2015','26':'2016','27':'2017','28':'2018','29':'2019'})
dados_vinho.iloc[768:1024] = dados_vinho.iloc[768:1024].replace({'20':'2010'})
dados_vinho.iloc[3584:3840] = dados_vinho.iloc[3584:3840].replace({'20':'2021'})
dados_vinho['País de origem'] = 'Brasil'
dados_vinho.rename({'País':'País de destino'}, axis=1, inplace = True)
df = dados_vinho
df_vinho_valor = dados_vinho[dados_vinho['Medida'] == 'Valor']
df_vinho_quantidade = dados_vinho[dados_vinho['Medida'] == 'Quantidade']
df_agrupado_ano = df_vinho_valor.groupby('ano')['valor'].sum().reset_index()
df_vinho_valor = df_vinho_valor.sort_values(by="valor", ascending=False)
df_agrupado_quantidade = df_vinho_quantidade.groupby('ano')['valor'].sum().reset_index()
df_maiores_gastos = df_vinho_valor.sort_values(by="valor", ascending=False)
df_maiores_gastos = df_maiores_gastos.drop(['Id', 'ano', 'Medida', 'País de origem'], axis=1)
df_maiores_gastos = df_maiores_gastos.loc[1769:3797]
df_maiores_gastos = df_maiores_gastos.groupby("País de destino").sum()
df_maiores_gastos = df_maiores_gastos.sort_values(by="valor", ascending=False)
df_maiores_gastos = df_maiores_gastos.reset_index()
df_maiores_quantidades = df_vinho_quantidade.sort_values(by="valor", ascending=False)
df_maiores_quantidades = df_maiores_quantidades.drop(['Id', 'ano', 'Medida','País de origem'], axis=1)
df_maiores_quantidades = df_maiores_quantidades.loc[617:3609]
df_maiores_quantidades = df_maiores_quantidades.groupby("País de destino").sum()
df_maiores_quantidades = df_maiores_quantidades.sort_values(by="valor", ascending=False)
df_maiores_quantidades = df_maiores_quantidades.reset_index()
df_quantidade = df_agrupado_quantidade[['ano', 'valor']].rename(columns={'valor': 'quantidade'})
df_ano = df_agrupado_ano[['ano', 'valor']].rename(columns={'valor': 'receita'})
df_comparacao_medidas = pd.merge(df_quantidade, df_ano, on='ano')
df_paises_quantidades = df_maiores_quantidades[['País de destino', 'valor']].rename(columns={'valor': 'Quantidade'})
df_paises_valor = df_maiores_gastos[['País de destino', 'valor']].rename(columns={'valor': 'Receita'})
df_paises_expressivos = pd.merge(df_paises_quantidades, df_paises_valor, on='País de destino')
df_paises_expressivos['País de origem'] = 'Brasil'
paises_selecionados = ['Rússia', 'Paraguai',	'Estados Unidos',	'China',	'Espanha',	'Haiti',	'Japão',	'Países Baixos',	'Reino Unido','Alemanha, República Democrática']
df_filtrado = df_vinho_quantidade[df_vinho_quantidade['País de destino'].isin(paises_selecionados)]
df_filtrado = df_filtrado.sort_values(by="valor", ascending=False)
paises_sem_russia = ['Paraguai',	'Estados Unidos',	'China',	'Espanha',	'Haiti',	'Japão',	'Países Baixos',	'Reino Unido','Alemanha, República Democrática']
df_filtrado_sem_russia  = df_vinho_quantidade[df_vinho_quantidade['País de destino'].isin(paises_sem_russia)]
df_filtrado_sem_russia = df_filtrado_sem_russia.sort_values(by="valor", ascending=False)

st.markdown("<p style='text-align: center; color:gray; font-size:24px'>Exportar é atingir novos mercados, é abrir fronteiras para o mundo", unsafe_allow_html=True)

st.markdown("<p style='text-align: justify; color:gray; font-size:18px'>Abaixo temos em ordem os países que mais exportamos em valor (U$) e litros (L) entre o período de 2007 à 2022:", unsafe_allow_html=True)

st.dataframe(df_paises_expressivos, width=1920)

##Gráficos 

fig_valor_anual = px.line(df_agrupado_ano,
                             x ='ano',
                             y ='valor',
                             markers = True,
                             range_y = (0,df_agrupado_ano.max()),
                             title ='Valor anual da exportação de vinhos de mesa')

fig_valor_anual.update_layout(yaxis_title = 'Receita')

fig_quantidade_anual = px.line(df_agrupado_quantidade,
                             x ='ano',
                             y ='valor',
                             markers = True,
                             range_y = (0,df_agrupado_quantidade.max()),
                             title ='Litros anuais de vinho exportados')

fig_quantidade_anual.update_layout(yaxis_title = 'Litros')


fig_valor_paises = px.bar(df_maiores_gastos.head(10),
                             x = 'País de destino',
                             y = 'valor',
                             text_auto = True,
                             title = 'Paises com maior receita exportada')

fig_valor_paises.update_layout(yaxis_title = 'Receita')

fig_quantidade_paises = px.bar(df_maiores_quantidades.head(10), 
                             x = 'País de destino',
                             y = 'valor',
                             text_auto = True,
                             title = 'Paises com maior quantidade em litros de vinho exportado')

fig_quantidade_paises.update_layout(yaxis_title = 'Litros')

fig_comparacao_medidas = px.line(df_comparacao_medidas, x='ano', y=['receita', 'quantidade'],
              markers=True, labels={'value': 'Valor'}, 
              title='A relação entre as medidas de valores recebidos e quantidades exportadas nos últimos 15 anos',
              color_discrete_map={'receita': 'orange', 'quantidade': 'blue'})

fig_comparacao_medidas.update_layout(yaxis_title = 'Medidas')

fig_outlier_com_russia = px.bar(df_filtrado,
                             x ='ano',
                             y ='valor',
                             barmode='group',
                             range_y = (0,df_filtrado.max()),
                             color = 'País de destino',
                             title ='Evolutivo anual de exportação de vinhos em litros com Rússia')

fig_outlier_com_russia .update_layout(yaxis_title = 'Litros')

fig_outlier_sem_russia = px.bar(df_filtrado_sem_russia,
                             x ='ano',
                             y ='valor',
                             barmode='group',
                             range_y = (0,df_filtrado_sem_russia.max()),
                             color = 'País de destino',
                             title ='Evolutivo anual de exportação de vinhos em litros sem Rússia')

fig_outlier_sem_russia.update_layout(yaxis_title = 'Litros')

##Visualização no Streamlit

aba1, aba2, aba3, aba4, aba5, aba6, aba7 = st.tabs(['Receita','Quantidade em litros de vinho exportado anualmente','Receita em dólares obtida pelos principais países', 'Quantidade em litros exportada pelos principais países', 'Russia, nosso outlier', 'Visualização sem outlier', 'Comparação das medidas'])

with aba1:

    coluna1,coluna2 = st.columns(2)
    with coluna1:
        st.metric ('Receita', formata_numero(df_agrupado_ano['valor'].sum(), 'US$'))
        st.plotly_chart(fig_valor_anual, use_container_width = True)
    with coluna2:
        st.write("<p style='text-align: justify; color:gray; font-size:18px'> 💡É notado que as receitas dos anos de 2009 e 2013 foram os anos mais expressivos até 2020. Ano de 2013 foi o ano com o maior valor de receita em todo o período. Deve-se levar em consideração que no ano de 2010 obteve-se a maior queda em todo o período assim como o ano de 2015. a partir do ano de 2016 a exportação de vinhos apresentou melhoras ano após ano, com o ano de 2022 tomando o lugar de 2009 como o segundo ano mais lucrativo do período.",  unsafe_allow_html=True)


with aba2:
    coluna1,coluna2 = st.columns(2)
    with coluna1:
        st.metric ('Litros exportados', formata_numero(df_vinho_quantidade['valor'].sum()))
        st.plotly_chart(fig_quantidade_anual, use_container_width = True)
    with coluna2:
        st.write("<p style='text-align: justify; color:gray; font-size:18px'> 💡 A exportação dos anos de 2009 e 2013 foram os mais expressivos em todo o período. No entanto o ano de 2009 foi o ano em que se teve a maior quantidade de vinhos de mesa exportado e ano de 2013 menor comparado ao ano de 2009.",  unsafe_allow_html=True)
    
with aba3:
    coluna1,coluna2 = st.columns(2)
    with coluna1:
            st.plotly_chart(fig_valor_paises, use_container_width = True)
    with coluna2:
            st.write("<p style='text-align: justify; color:gray; font-size:18px'> 💡É perceptível que os países que tiveram maior contribuição na receita de exportação foram Paraguai e Rússia, os demais países tiveram uma participacão menor comparado aos mesmos no período.",  unsafe_allow_html=True)
           
with aba4:
    coluna1,coluna2 = st.columns(2)
    with coluna1:
            st.plotly_chart(fig_quantidade_paises, use_container_width = True)
    with coluna2:
            st.write("<p style='text-align: justify; color:gray; font-size:18px'> 💡A Rússia foi o país que exportou a maior quantidade em litros de vinho no período de 2007 à 2022 mas mesmo assim não foi o país com a maior receita, tal razão para isso pode ser melhor detalhado nas próximas abas",  unsafe_allow_html=True)       

with aba5:
    coluna1,coluna2 = st.columns(2)
    with coluna1:
            st.plotly_chart(fig_outlier_com_russia )    
    with  coluna2:
            st.write("<p style='text-align: justify; color:gray; font-size:18px'> 💡A Rússia embora tenha contribuído significativamente no perído dos últimos 15 anos com a exportação do vinho no Brasil, pode ser considerada como um outlier(dados que se diferenciam drasticamente de todos os outros) pois ao analisar seus dados é possível verificar que os valores mais expressivos concentram-se apenas nos anos de 2008,2009,2012 e 2013. A partir do ano de 2014 até o momento seus valores foram reduzidos drasticamente. Vale ressaltar que a Rússia detém 43,05 por cento das exportações de vinho de todo o período.",  unsafe_allow_html=True)   

with aba6:
    coluna1,coluna2 = st.columns(2)
    with coluna1:
            st.plotly_chart(fig_outlier_sem_russia )
    with coluna2:
            st.write("<p style='text-align: justify; color:gray; font-size:18px'> '💡O Paraguai destaca-se pelos valores mais significativos ao analisarmos a evolução anual. A partir de 2017, registra um crescimento exponencial, caracterizado por variações positivas em todos os anos, com exceção de 2019. Neste ano, o país enfrentou uma crise política que resultou em uma redução nos valores de exportação. Tal fato deve ser creditado pelo fato do país pertencer ao bloco econômico MERCOSUL (Mercado Comum do Sul) composto por Argentina, Brasil, Paraguai e Uruguai que têm por objetivo promover o comércio, com políticas e acordos que facilitem as trocas entre os participantes.",  unsafe_allow_html=True)

with aba7:
      coluna1,coluna2 = st.columns(2)
      with coluna1:
            st.plotly_chart(fig_comparacao_medidas )
      with coluna2:
            st.write("<p style='text-align: justify; color:gray; font-size:18px'> '💡A partir de 2010, observamos que a tendência da linha de valor supera consistentemente a linha de quantidade, e essa dinâmica persiste até a data mais recente. Essa situação pode ser atribuída ao aumento contínuo do valor do dólar a partir de 2010, exercendo um impacto direto em todas as transações comerciais, bem como o aumento das taxas de exportação contribuindo nesse cenário.",  unsafe_allow_html=True)

#BOTAO DOWNLOAD
                      
st.markdown('Escreva um nome para o arquivo')
coluna1, coluna2 = st.columns(2)
with coluna1:
    nome_arquivo = st.text_input('', label_visibility = 'collapsed', value = 'dados')
    nome_arquivo += '.csv'
with coluna2:
    st.download_button('Fazer o download da tabela em csv', data = converte_csv(df), file_name = nome_arquivo, mime = 'text/csv', on_click = mensagem_sucesso)