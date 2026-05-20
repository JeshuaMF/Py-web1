import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

st.set_page_config(page_title="Examen Estadístico", layout="wide")

try:
    df = pd.read_csv("datos_examen.csv")
except FileNotFoundError:
    st.error(
        "No se encontró el archivo 'datos_examen.csv'. Asegúrate de subirlo o crearlo."
    )
    st.stop()

st.title("Análisis Estadístico del Examen")
st.markdown("---")

st.header("1. Medidas de Tendencia Central")
col_analisis = "peso"

media = df[col_analisis].mean()
mediana = df[col_analisis].median()
moda = df[col_analisis].mode()[0]

c1, c2, c3 = st.columns(3)
c1.metric("Media", f"{media:.2f}")
c2.metric("Mediana", f"{mediana:.2f}")
c3.metric("Moda", f"{moda:.2f}")

st.markdown("---")

st.header("2. Visualización de Frecuencias")

col_izq, col_der = st.columns(2)

with col_izq:
    st.subheader("Frecuencia Absoluta (Color)")
    fig_bar, ax_bar = plt.subplots()
    df["color"].value_counts().plot(kind="bar", ax=ax_bar, color="skyblue")
    ax_bar.set_ylabel("Cantidad")
    st.pyplot(fig_bar)

with col_der:
    st.subheader("Frecuencia Relativa (Color)")
    fig_pie, ax_pie = plt.subplots()
    df["color"].value_counts().plot(
        kind="pie", autopct="%1.1f%%", ax=ax_pie, startangle=90
    )
    ax_pie.set_ylabel("")
    st.pyplot(fig_pie)

st.subheader("Polígono de Frecuencias Acumuladas")
counts, bin_edges = np.histogram(df[col_analisis], bins=10)

acumulada = np.cumsum(counts)
bin_centers = (bin_edges[:-1] + bin_edges[1:]) / 2

fig_pol, ax_pol = plt.subplots(figsize=(10, 4))
ax_pol.plot(
    bin_centers,
    acumulada,
    marker="s",
    color="orange",
    linestyle="-",
    label="Frec. Acumulada",
)
ax_pol.fill_between(bin_centers, acumulada, alpha=0.1, color="orange")
ax_pol.set_xlabel(col_analisis.capitalize())
ax_pol.set_ylabel("Frecuencia Acumulada")
ax_pol.grid(True, linestyle="--", alpha=0.6)
st.pyplot(fig_pol)

st.markdown("---")

if st.checkbox("Mostrar tabla de datos crudos"):
    st.dataframe(df)
