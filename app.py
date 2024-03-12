import pandas as pd
import plotly.express as px
import streamlit as st

car_data = pd.read_csv('vehicles_us.csv')  # leer los datos

st.header('Car Sale')

hist_button = st.button('Construir histograma')  # crear un botón

if hist_button:  # al hacer clic en el botón
    # escribir un mensaje
    st.write('Creación de un histograma para el conjunto de datos de anuncios de venta de coches')

    # crear un histograma
    fig = px.histogram(car_data, x="odometer")

    # mostrar un gráfico Plotly interactivo
    st.plotly_chart(fig, use_container_width=True)

st.header('Compare Yourself')

# Creación de scatter cpn checkbox
build_scatter = st.checkbox('Construir un diagráma de dispersión para observar relación: precio, odómetro y transmisión')

if build_scatter:  # si la casilla de verificación está seleccionada
    #st.write('Construir un diagráma de dispersión para observar relación: precio, odómetro y transmisión')
    # crear un scatter
    scatter_fig = px.scatter(data_frame=car_data,
                             x="odometer",
                             y="price",
                             color="transmission",
                             width=1000,
                             height=400,
                             title="Relation price / odometer / transmission")
    st.plotly_chart(scatter_fig, use_container_width=True)

