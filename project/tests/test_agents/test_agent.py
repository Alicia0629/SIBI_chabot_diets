import pytest
from agents.agent import Agent

def test_history():
    agent = Agent()
    agent.receive_message(message="Hola, me llamo Alicia", history=True)
    message = agent.receive_message(message="Hola, ¿cómo me llamo?", history=True)
    assert "Alicia" in message