import pytest
from agents.recommendation_agent import RecommendationAgent  

def test_chat_and_recommend_empty():
    agent = RecommendationAgent(file="data/datasets/TestRecipes2.csv", using_rag=True)
    allergies = {"HasDairy":True,"HasGluten":True, "HasEgg":True, "HasFish":True, "HasShellfish":True,"HasTreenut":True,"HasPeanut":True,"HasSoy":True,"HasSesame":True,"HasMustard":True}
    message = agent.chat_and_recommend(user_input="Dame ideas para desayunar", dietary_restrictions=allergies)
    assert len(message) > 1


def test_chat_and_recommend_with_rag():
    agent = RecommendationAgent(using_rag=True)
    message = agent.chat_and_recommend(user_input="Dame ideas para desayunar", dietary_restrictions={"HasDairy":True})
    assert len(message) > 1

def test_chat_and_recommend_without_RAG():
    agent = RecommendationAgent(using_rag=False)
    message = agent.chat_and_recommend(user_input="Dame ideas para desayunar", dietary_restrictions={})
    assert len(message) > 1