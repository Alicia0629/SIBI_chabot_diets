import pytest
from agents.def_user_agent import DefUserAgent  
from utils.userProfile import UserProfile

def test_define_user():
    agent = DefUserAgent()
    user = UserProfile(
        allergies={"HasDairy": True},
        sex="Masculino", age=30, height=175, weight=70, 
        sportLevel="Ejercicio moderado (3-5 días a la semana)", objective="Adelgazar"
    )
    message = agent.define_user(user)
    assert len(message) > 1