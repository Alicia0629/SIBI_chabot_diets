import pytest
import ast
from utils.userProfile import UserProfile
from agents.verify_data_agent import VerifyDataAgent
from utils.change_profile import changeData

# Test basic data update with a valid AI message
def test_changeData_basic():
    user = UserProfile(allergies={"HasDairy": True, "HasGluten": False}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Ejercicio moderado (3-5 días a la semana)", objective="Adelgazar")
    ai_message = "[age]30;[sex]Female;[allergies]{'HasFish': True}"
    result = changeData(user, ai_message)
    # Check if the function returns True (indicating coherence)
    assert result == 'True'
    # Verify the profile was updated correctly
    assert user.getSex() == "Femenino"
    assert user.getAge() == 30
    assert user.getAllergies()["HasFish"] is True

# Test for handling wrong allergy text
def test_changeData_invalid_allergies():
    user = UserProfile(allergies={"HasDairy": True, "HasGluten": False}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Ejercicio moderado (3-5 días a la semana)", objective="Adelgazar")
    ai_message = "[allergies][HasFish]"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getAllergies()["HasFish"] is True

# Test to handle errors from ast.literal_eval
def test_changeData_ast_error():
    user = UserProfile(allergies={"HasDairy": True, "HasGluten": False}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Ejercicio moderado (3-5 días a la semana)", objective="Adelgazar")
    ai_message = "[allergies]{invalid: True}"
    result = changeData(user, ai_message)
    # Ensure the function handles the error gracefully and no changes are made
    assert result == 'True'
    assert user.getAllergies() == user.getAllergies()  # No changes

# Test to verify the coherence 
def test_changeData_coherence():
    user = UserProfile(allergies={"HasDairy": True, "HasGluten": False}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Ejercicio moderado (3-5 días a la semana)", objective="Adelgazar")
    ai_message = "[height] 185 cm"
    result = changeData(user, ai_message)
    
    # Verify the function returns True and the height is updated
    assert result == 'True'
    assert user.getHeight() == 185.0

# Test to ensure text_similarity is correctly used for unknown allergies
def test_changeData_text_similarity_allergies():
    user = UserProfile(allergies={"HasDairy": True, "HasGluten": False}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Ejercicio moderado (3-5 días a la semana)", objective="Adelgazar")
    ai_message = "[allergies]{'HasFishy': True}"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getAllergies()["HasFish"] is True

# Test to ensure boolean value is handled correctly when it is a string
def test_changeData_boolean_as_string():
    user = UserProfile(allergies={"HasDairy": True, "HasGluten": False}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Ejercicio moderado (3-5 días a la semana)", objective="Adelgazar")
    ai_message = "[allergies]{'HasFish': 'True'}"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getAllergies()["HasFish"] is True

# Test for handling sport level input as number
def test_changeData_sportLevel_number():
    user = UserProfile(allergies={}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Poco o ningún ejercicio (Sentado)", objective="Mantenerme sano")
    ai_message = "[sportLevel]3"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getSportLevel() == 3


# Test for handling objective input as number
def test_changeData_objective_number():
    user = UserProfile(allergies={}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Poco o ningún ejercicio (Sentado)", objective="Mantenerme sano")
    ai_message = "[objective]1"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getObjectiveString() == "Ganar músculo"

# Test for objective input requiring text_similarity
def test_changeData_objective_text_similarity():
    user = UserProfile(allergies={}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Poco o ningún ejercicio (Sentado)", objective="Mantenerme sano")
    ai_message = "[objective]adelgazar"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getObjectiveString() == "Adelgazar"

# Test for weight update using a numeric value in AI message
def test_changeData_weight_update():
    user = UserProfile(allergies={}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Poco o ningún ejercicio (Sentado)", objective="Mantenerme sano")
    ai_message = "[weight]80"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getWeight() == 80.0

# Test for sportLevel update when value "1" is in the message
def test_changeData_sportLevel_1():
    user = UserProfile(allergies={}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Poco o ningún ejercicio (Sentado)", objective="Mantenerme sano")
    ai_message = "[sportLevel]1"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getSportLevel() == 1

# Test for sportLevel update when value "2" is in the message
def test_changeData_sportLevel_2():
    user = UserProfile(allergies={}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Poco o ningún ejercicio (Sentado)", objective="Mantenerme sano")
    ai_message = "[sportLevel]2"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getSportLevel() == 2

# Test for sportLevel update when value "4" is in the message
def test_changeData_sportLevel_4():
    user = UserProfile(allergies={}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Poco o ningún ejercicio (Sentado)", objective="Mantenerme sano")
    ai_message = "[sportLevel]4"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getSportLevel() == 4

# Test for sportLevel update when value "5" is in the message
def test_changeData_sportLevel_5():
    user = UserProfile(allergies={}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Poco o ningún ejercicio (Sentado)", objective="Mantenerme sano")
    ai_message = "[sportLevel]5"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getSportLevel() == 5

# Test for objective update when value "-1" is in the message
def test_changeData_objective_minus_1():
    user = UserProfile(allergies={}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Poco o ningún ejercicio (Sentado)", objective="Mantenerme sano")
    ai_message = "[objective]-1"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getObjective() == -1

# Test for objective update when value "0" is in the message
def test_changeData_objective_0():
    user = UserProfile(allergies={}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Poco o ningún ejercicio (Sentado)", objective="Mantenerme sano")
    ai_message = "[objective]0"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getObjective() == 0

# Test for sportLevel update when sportLevel value is a number
def test_changeData_sportLevel_numeric():
    user = UserProfile(allergies={}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Poco o ningún ejercicio (Sentado)", objective="Mantenerme sano")
    ai_message = "[sportLevel]3"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getSportLevel() == 3

# Test for sportLevel update when sportLevel is a non-numeric string (text similarity)
def test_changeData_sportLevel_text_similarity():
    user = UserProfile(allergies={}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Poco o ningún ejercicio (Sentado)", objective="Mantenerme sano")
    ai_message = "[sportLevel]Ejercicio fuerte"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getSportLevelString() == "Ejercicio fuerte (6-7 días a la semana)"

# Test for boolean value conversion with text similarity
def test_changeData_boolean_text_similarity():
    user = UserProfile(allergies={}, sex="Male", age=30, height=180.0, weight=75.0, sportLevel="Poco o ningún ejercicio (Sentado)", objective="Mantenerme sano")
    ai_message = "[allergies]{'HasDairy':'true'}"
    result = changeData(user, ai_message)
    assert result == 'True'
    assert user.getAllergies()["HasDairy"] is True
