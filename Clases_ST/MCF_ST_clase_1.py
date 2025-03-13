import streamlit as st
import pandas as pd
import yfinance as yf
import matplotlib.pyplot as plt
from scipy.stats import kurtosis, skew

st.title("Visualización de Rendimientos de Acciones")
st.header("Streamlit clase 1 ")

@st.cache_data
def obtener_datos(stocks):
    df = yf.download(stocks, period="1y")['Close']
    return df

@st.cache_data
def calcular_rendimientos(df):
    return df.pct_change().dropna()

# Lista de acciones de ejemplo
stocks_lista = ['AAPL', 'MSFT', 'GOOGL', 'TSLA', 'AMZN']

with st.spinner("Descargando datos..."):
    df_precios = obtener_datos(stocks_lista)
    df_rendimientos = calcular_rendimientos(df_precios)

# Selector de acción
stock_seleccionado = st.selectbox("Selecciona una acción", stocks_lista)

if stock_seleccionado:
    st.subheader(f"Métricas de Rendimiento: {stock_seleccionado}")
    
    rendimiento_medio = df_rendimientos[stock_seleccionado].mean()
    Kurtosis = kurtosis(df_rendimientos[stock_seleccionado])
    skew = skew(df_rendimientos[stock_seleccionado])
    
    col1, col2, col3= st.columns(3)
    col1.metric("Rendimiento Medio Diario", f"{rendimiento_medio:.4%}")
    col2.metric("Kurtosis", f"{Kurtosis:.4}")
    col3.metric("Skew", f"{skew:.2}")

    # Gráfico de rendimientos diarios
    st.subheader(f"Gráfico de Rendimientos: {stock_seleccionado}")
    fig, ax = plt.subplots(figsize=(13, 5))
    ax.plot(df_rendimientos.index, df_rendimientos[stock_seleccionado], label=stock_seleccionado)
    ax.axhline(y=0, color='r', linestyle='--', alpha=0.7)
    ax.legend()
    ax.set_title(f"Rendimientos de {stock_seleccionado}")
    ax.set_xlabel("Fecha")
    ax.set_ylabel("Rendimiento Diario")
    st.pyplot(fig)
    
    # Histograma de rendimientos
    st.subheader("Distribución de Rendimientos")
    fig, ax = plt.subplots(figsize=(10, 5))
    ax.hist(df_rendimientos[stock_seleccionado], bins=30, alpha=0.7, color='blue', edgecolor='black')
    ax.axvline(rendimiento_medio, color='red', linestyle='dashed', linewidth=2, label=f"Promedio: {rendimiento_medio:.4%}")
    ax.legend()
    ax.set_title("Histograma de Rendimientos")
    ax.set_xlabel("Rendimiento Diario")
    ax.set_ylabel("Frecuencia")
    st.pyplot(fig)

# import streamlit as st
# import pandas as pd
# import matplotlib.pyplot as plt
# import Funciones_MCF as MCF
# from scipy.stats import kurtosis, skew

# st.title("Streamlit Clase 1")
# st.header("Visualizacion de Activos")

# lista_de_stocks = ['AAPL','NVDA','GOOGL','TSLA','AMZN','MSFT']

# with st.spinner("Descargando datos..."):
#     df_precios = MCF.obtener_datos(lista_de_stocks)
#     df_rendimientos = MCF.calcular_rendimientos(df_precios)

# stock_seleccionado = st.selectbox("Selecciona una acción" , lista_de_stocks)

# if stock_seleccionado:
#     st.subheader(f"Métricas de Rendimiento: {stock_seleccionado}")
#     rendimiento_promedio = (df_rendimientos[stock_seleccionado]).mean()
#     deviacion_estandar = df_rendimientos[stock_seleccionado].std()

#     col1, col2 = st.columns(2)
#     col1.metric("Remdimiento Medio Diario", f"{rendimiento_promedio:.4%}")
#     col2.metric("Desviacion Estandar",f"{volatilidad:.4%}")






