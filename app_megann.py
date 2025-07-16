import streamlit as st

st.set_page_config(page_title="Conversor de Megann 💜", page_icon="🌡️", layout="centered", initial_sidebar_state="collapsed")

st.markdown("<h1 style='text-align: center; color: #8833ff;'>SISTEMA DE CONVERSIONES 5.0</h1>", unsafe_allow_html=True)
st.markdown("<h4 style='text-align: center;'>Diseñado con amor para Megann Quispe 💕</h4>", unsafe_allow_html=True)
st.markdown("---")

opciones = ["Selecciona una opción", "Temperatura (°C a °F)", "Longitud (km a millas)", "Masa (kg a libras)"]
opcion = st.selectbox("¿Qué quieres convertir hoy, Megann?", opciones)

valor = st.text_input("Ingresa el valor a convertir:")

if st.button("Convertir"):
    try:
        numero = float(valor)

        if opcion == opciones[1]:
            if numero < -273 or numero > 100:
                st.error("La temperatura debe estar entre -273 y 100 °C.")
            else:
                resultado = round((9 * numero + 160) / 5, 2)
                st.success(f"{numero} °C = {resultado} °F")

        elif opcion == opciones[2]:
            if numero <= 0:
                st.error("La longitud debe ser mayor a 0.")
            else:
                resultado = round(numero / 1.60934, 2)
                st.success(f"{numero} km = {resultado} millas")

        elif opcion == opciones[3]:
            if numero <= 0:
                st.error("La masa debe ser mayor a 0.")
            else:
                resultado = round(numero / 0.453592, 2)
                st.success(f"{numero} kg = {resultado} libras")

        else:
            st.warning("Por favor, selecciona una opción de conversión.")
    
    except ValueError:
        st.error("Por favor, ingresa un número válido.")
