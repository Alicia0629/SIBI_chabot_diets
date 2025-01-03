import streamlit as st
from utils.userProfile import UserProfile
from utils.change_profile import changeData
from agents import VerifyDataAgent, DefUserAgent, DetectChangeDataAgent, RecommendationAgent, VerifyDataAgent

if 'verify_agent' not in st.session_state:
    st.session_state['verify_agent'] = VerifyDataAgent()
if 'def_user_agent' not in st.session_state:
    st.session_state['def_user_agent'] = DefUserAgent()
if 'detect_change_data_agent' not in st.session_state:
    st.session_state['detect_change_data_agent'] = DetectChangeDataAgent()
if 'recomend_agent' not in st.session_state:
    st.session_state['recomend_agent'] = RecommendationAgent()

verify_agent = st.session_state['verify_agent']
def_user_agent = st.session_state['def_user_agent']
detect_change_data_agent = st.session_state['detect_change_data_agent']
recomend_agent = st.session_state['recomend_agent']


st.title("Recomendador de comidas")

if 'user' not in st.session_state:
    st.subheader("Porfavor inserta tus datos personales, para que podamos recomendarte mejor tus dietas.")
    col1, col2, col3, col4 = st.columns([6,2,6,10])  
    with col3:
        sexo = st.radio("Sexo", ["Masculino", "Femenino"])
        edad = st.slider("Edad", min_value=18, max_value=120, value=18)
        altura = st.slider("Altura (cm)", min_value=50, max_value=250, value=167)
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
                recomend_agent.update_filters(st.session_state.user.getAllergies())
                st.rerun()
            else:
                st.warning(coherentData)

if 'user' in st.session_state:
    col1, col2 = st.columns([1, 1]) 
    user = st.session_state.user

    if user.getDefinition() is None or st.session_state.get("profile_updated", False):
        user.setDefinition(def_user_agent.define_user(user))
        st.session_state["profile_updated"] = False 

    with col2:
        st.subheader("Haz tus preguntas sobre dietética a la IA")
        user_input = st.text_input("Escribe tu mensaje...")
        if user_input:
            ai_response = ""
            st.write(f"Usuario: {user_input}")

            #Analyse the message to see if there have been any changes
            analyse_change_data=detect_change_data_agent.analyse_message(message=user_input, user_profile=st.session_state.user)

            if 'false' not in analyse_change_data.lower():
                coherent = changeData(userProfile=st.session_state.user, AIMessage=analyse_change_data)
                if 'true' not in coherent.lower():
                    ai_response = "Error cambiando datos: '"+coherent+"'"
                else:
                    st.session_state["profile_updated"] = True
                    recomend_agent.update_filters(st.session_state.user.getAllergies())
                    st.success("Datos del usuario actualizados.")
                    ai_response = " "

            #Create response
            if len(ai_response) < 1:
                process = recomend_agent.chat_and_recommend(user_input, st.session_state.user.getAllergies())
                ai_response = process

            if len(ai_response) != 1:
                st.write(f"AI: {ai_response}")
    
    with col1:
        user = st.session_state.user

        if user.getDefinition() is None or st.session_state.get("profile_updated", False):
            user.setDefinition(def_user_agent.define_user(user))
            st.session_state["profile_updated"] = False 

        st.write(user.getDefinition())
       

