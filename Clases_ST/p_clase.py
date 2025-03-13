import pandas as pd
import numpy as np 
import Funciones_MCF as MCF
import streamlit as st


'''
Streamlit de la clase 

'''

st.title('Clase 1')
st.header('Visualizacion de Activos')


M7 = ['AAPL','MSFT','NVDA','TSLA','GOOGL','NFLX','AMZN']
with st.spinner('Descargando data...'):
    df_precios = MCF.obtener_datos(M7)
    df_rendimientos = MCF.calcular_rendimientos(df_precios)

stock_seleccionado = st.selectbox('Selecciona una Accion',M7)

if stock_seleccionado:

    st.subheader(f'Metricas :{stock_seleccionado}')

    promedio_rendi_diario = df_rendimientos['AAPL'].mean()
    kurtosis = kurtosis(df_rendimientos['AAPL'])
    skew = skew(df_rendimientos['AAPL'])


