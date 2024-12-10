import streamlit as st
from utils.userProfile import UserProfile
from agents.verify_data_agent import VerifyDataAgent
from agents.def_user_agent import DefUserAgent

verify_agent = VerifyDataAgent()
def_user_agent = DefUserAgent()

st.title("Recomendador de comidas")

if 'user' not in st.session_state:
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
            user_profile = UserProfile(allergies=allergies, sex=sexo, age=edad, height=altura, weight=peso, sportLevel=deporte, objective=objetivo)
            coherentData = verify_agent.verify_data_of_user(user_profile)
            if ("True" in coherentData):
                st.session_state.user = user_profile
                st.rerun()
            else:
                st.warning(coherentData)

if 'user' in st.session_state:
    st.subheader("Haz tus preguntas sobre dietética a la IA")
    col1, col2 = st.columns([1,3])  

    with col2:
        user_input = st.text_input("Escribe tu mensaje...")

        if user_input:
            st.write(f"Usuario: {user_input}")
            ai_response = "Proximamente :)"
            st.write(f"AI: {ai_response}")
    
    with col1:
        st.subheader("Tú perfil")
        st.write(def_user_agent.define_user(st.session_state.user))

