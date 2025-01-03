import pytest
from agents.verify_data_agent import VerifyDataAgent  
from utils.userProfile import UserProfile

def test_verify_data_of_user_true():
    agent = VerifyDataAgent()
    user = UserProfile(
        allergies={"HasDairy": True},
        sex="Masculino", age=30, height=175, weight=70, 
        sportLevel="Ejercicio moderado (3-5 días a la semana)", objective="Adelgazar"
    )
    message = agent.verify_data_of_user(user)
    assert len(message) > 1


def test_verify_data_of_user_false():
    agent = VerifyDataAgent()
    user = UserProfile(
        allergies={"HasDairy": True},
        sex="Masculino", age=30, height=75, weight=70, 
        sportLevel="Ejercicio moderado (3-5 días a la semana)", objective="Adelgazar"
    )
    message = agent.verify_data_of_user(user)
    assert len(message) > 1