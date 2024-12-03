import streamlit as st

st.title("Recomendador de comidas")

if 'edad' not in st.session_state or 'altura' not in st.session_state or 'peso' not in st.session_state or 'sexo' not in st.session_state or 'deporte' not in st.session_state:
    edad = st.number_input("Edad", min_value=1, max_value=120)
    altura = st.number_input("Altura (cm)", min_value=50, max_value=250)
    peso = st.number_input("Peso (kg)", min_value=1, max_value=300)
    sexo = st.selectbox("Sexo", ["Masculino", "Femenino"])
    deporte = st.selectbox(
        "Cantidad de ejercicio", 
        [
            "Poco o ningún ejercicio (Sentado)", 
            "Ejercicio ligero (1-3 días a la semana)", 
            "Ejercicio moderado (3-5 días a la semana)", 
            "Ejercicio fuerte (6-7 días a la semana)", 
            "Ejercicio muy fuerte (dos veces al día, entrenamientos muy duros)"
        ]
    )

    if st.button("Siguiente"):
        if edad and altura and peso and sexo and deporte:
            st.session_state.edad = edad
            st.session_state.altura = altura
            st.session_state.peso = peso
            st.session_state.sexo = sexo
            st.session_state.deporte = deporte
            st.rerun()
        else:
            st.warning("Por favor, completa todos los campos.")

if 'edad' in st.session_state and 'altura' in st.session_state and 'peso' in st.session_state and 'sexo' in st.session_state and 'deporte' in st.session_state:
    st.subheader("Chat con AI")
    st.write(f"Edad: {st.session_state.edad}")
    st.write(f"Altura: {st.session_state.altura} cm")
    st.write(f"Peso: {st.session_state.peso} kg")
    st.write(f"Sexo: {st.session_state.sexo}")
    st.write(f"Deporte: {st.session_state.deporte}")

    user_input = st.text_input("Escribe tu mensaje...")

    if user_input:
        st.write(f"Usuario: {user_input}")
        ai_response = "Proximamente :)"
        st.write(f"AI: {ai_response}")

