import streamlit as st
import pandas as pd
import plotly.express as px

# Encabezado
st.header('Análisis de anuncios de venta de vehículos en EE. UU.')

# Cargar los datos
car_data = pd.read_csv('vehicles_us.csv')

# --- OPCIÓN CON BOTONES ---
st.subheader("Usa los botones para mostrar gráficos:")

# Botón para histograma
if st.button('Construir histograma'):
    st.write('Histograma del odómetro (kilometraje)')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

# Botón para diagrama de dispersión
if st.button('Construir gráfico de dispersión'):
    st.write('Diagrama de dispersión: Precio vs Kilometraje')
    fig = px.scatter(car_data, x='odometer', y='price',
                     title='Precio vs Odómetro')
    st.plotly_chart(fig, use_container_width=True)

# --- OPCIÓN CON CHECKBOXES ---
st.subheader("O usa las casillas para mostrar los gráficos:")

if st.checkbox('Mostrar histograma de odómetro'):
    st.write('Histograma del odómetro (kilometraje)')
    fig = px.histogram(car_data, x='odometer')
    st.plotly_chart(fig, use_container_width=True)

if st.checkbox('Mostrar diagrama de dispersión Precio vs Odómetro'):
    st.write('Diagrama de dispersión: Precio vs Kilometraje')
    fig = px.scatter(car_data, x='odometer', y='price',
                     title='Precio vs Odómetro')
    st.plotly_chart(fig, use_container_width=True)
