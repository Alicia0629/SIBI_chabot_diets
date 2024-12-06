import streamlit as st

from agents.verify_data_agent import VerifyDataAgent

verify_agent = VerifyDataAgent()


st.title("Recomendador de comidas")

if 'edad' not in st.session_state or 'altura' not in st.session_state or 'peso' not in st.session_state or 'sexo' not in st.session_state or 'deporte' not in st.session_state or 'objetivo' not in st.session_state:
    st.subheader("Porfavor inserta tus datos personales, para que podamos recomendarte mejor tus dietas.")
    col1, col2, col3, col4 = st.columns([6,2,6,10])  
    with col3:
        sexo = st.radio("Sexo", ["Masculino", "Femenino"])
        edad = st.slider("Edad", min_value=18, max_value=120, value=18)
        altura = st.slider("Altura (cm)", min_value=50, max_value=250, value=50)
        peso = st.number_input("Peso (kg)", min_value=1.0, max_value=300.0, step=1.0, format="%.1f")


    with col4:
        deporte = st.radio(
            "Cantidad de ejercicio", 
            [
                "Poco o ningún ejercicio (Sentado)", 
                "Ejercicio ligero (1-3 días a la semana)", 
                "Ejercicio moderado (3-5 días a la semana)", 
                "Ejercicio fuerte (6-7 días a la semana)", 
                "Ejercicio muy fuerte (dos veces al día, entrenamientos muy duros)"
            ]
        )
        objetivo = st.radio(
        "Mi objetivo alimenticio es...",
        ("Mantenerme sano", "Ganar músculo", "Adelgazar")
    )
    
    with col1:
        st.markdown("Selecciona los alimentos que quieres suprimir de tu dieta")

        allergies = {
            "HasDairy": st.checkbox("Lácteos"),
            "HasGluten": st.checkbox("Gluten"),
            "HasEgg": st.checkbox("Huevos"),
            "HasFish": st.checkbox("Pescado"),
            "HasShellfish": st.checkbox("Mariscos"),
            "HasTreenut": st.checkbox("Frutos secos (árboles)"),
            "HasPeanut": st.checkbox("Maní"),
            "HasSoy": st.checkbox("Soja"),
            "HasSesame": st.checkbox("Sésamo"),
            "HasMustard": st.checkbox("Mostaza")
        }

    col1,col2,col3 = st.columns([1,90,1]) 
    with col2:
        if st.button("Siguiente", use_container_width=True):
            coherentData = verify_agent.verify_data(edad, altura, peso)
            if coherentData:
                st.session_state.edad = edad
                st.session_state.altura = altura
                st.session_state.peso = peso
                st.session_state.sexo = sexo
                st.session_state.deporte = deporte
                st.session_state.objetivo = objetivo
                st.session_state.allergies = allergies
                st.rerun()
            else:
                st.warning("Los campos no tienen coherencia.")

if 'edad' in st.session_state and 'altura' in st.session_state and 'peso' in st.session_state and 'sexo' in st.session_state and 'deporte' in st.session_state and 'objetivo' in st.session_state:
    st.subheader("Chat con AI")
    #st.write(f"Edad: {st.session_state.edad}")
    #st.write(f"Altura: {st.session_state.altura} cm")
    #st.write(f"Peso: {st.session_state.peso} kg")
    #st.write(f"Sexo: {st.session_state.sexo}")
    #st.write(f"Deporte: {st.session_state.deporte}")
    #st.write(f"Objetivo: {st.session_state.objetivo}")
    #st.write("Alergias seleccionadas:")
    #st.write(st.session_state.allergies)

    user_input = st.text_input("Escribe tu mensaje...")

    if user_input:
        st.write(f"Usuario: {user_input}")
        ai_response = "Proximamente :)"
        st.write(f"AI: {ai_response}")

