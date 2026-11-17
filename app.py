"""Aplicação interativa para análise de dados de veículos usados"""

import streamlit as st
import pandas as pd
import plotly.express as px

# 1. Carregar o conjunto de dados
car_data = pd.read_csv('vehicles_us.csv')

# 2. Criar o título do aplicativo
st.title("Dashboard de Análise de Veículos")

# 3. Apresentação do projeto
st.write("Bem-vindo ao nosso projeto de análise de dados!")

# 4. Criar botão para gerar o histograma
hist_button = st.button("Criar histograma")

# 5. Verificar se o botão foi clicado
if hist_button:

    st.write("Distribuição da quilometragem dos veículos")

    # 6. Criar o histograma
    fig = px.histogram(
        car_data,
        x="odometer",
        title="Distribuição da quilometragem dos veículos"
    )

    # 7. Mostrar o gráfico no aplicativo
    st.plotly_chart(fig, use_container_width=True)


    # Criar botão para gerar gráfico de dispersão
scatter_button = st.button("Criar gráfico de dispersão")

# Verificar se o botão foi clicado
if scatter_button:
    st.write("Relação entre quilometragem e preço dos veículos")

    fig = px.scatter(
        car_data,
        x="odometer",
        y="price",
        title="Quilometragem x Preço dos veículos"
    )

    st.plotly_chart(fig, use_container_width=True)
