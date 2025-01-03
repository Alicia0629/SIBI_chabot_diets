import pytest
from agents.detect_change_data_agent import DetectChangeDataAgent  
from utils.userProfile import UserProfile

def test_analyse_message():
    agent = DetectChangeDataAgent()
    user = UserProfile(
        allergies={"HasDairy": True},
        sex="Masculino", age=30, height=175, weight=70, 
        sportLevel="Ejercicio moderado (3-5 días a la semana)", objective="Adelgazar"
    )
    message = agent.analyse_message(message="Soy celiaca", user_profile=user)
    assert len(message) > 1