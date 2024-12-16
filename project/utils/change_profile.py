import ast

from utils.userProfile import UserProfile
from utils.text_process import text_similarity, extract_numbers
from agents.verify_data_agent import VerifyDataAgent

sport_list=["Poco o ningún ejercicio (Sentado)",
            "Ejercicio ligero (1-3 días a la semana)",
            "Ejercicio moderado (3-5 días a la semana)",
            "Ejercicio fuerte (6-7 días a la semana)",
            "Ejercicio muy fuerte (dos veces al día, entrenamientos muy duros)"]

goal_list =["Mantenerme sano",
            "Ganar músculo",
            "Adelgazar"]

allergies_list = ["HasDairy","HasGluten", "HasEgg", "HasFish", "HasShellfish","HasTreenut","HasPeanut","HasSoy","HasSesame","HasMustard"]

boolean_list = ["True", "False"]

def changeData(userProfile:UserProfile, AIMessage:str):
    newProfile = userProfile.clone()
    
    pairs = AIMessage.split(";")
    updates = {}
    for pair in pairs:
        if pair.strip():
            print(pair)
            key = pair.split("]")[0][1:].strip()
            value = pair.split("]")[1].strip()
            value = value.replace("[","")
            updates[key] = value
    print(updates)

    if "allergies" in updates:
        oldAllergies = newProfile.getAllergies()
        updateAllergies = ast.literal_eval(updates["allergies"])
        newAllergies = {}
        for key, value in oldAllergies.items():
            newAllergies[key] = value
        for key, value in updateAllergies.items():
            if key not in allergies_list:
                key = text_similarity(phrase=key, texts=allergies_list)
            if not isinstance(value, bool) and value not in boolean_list:
                value = text_similarity(phrase=key, texts=boolean_list)
            if not isinstance(value, bool):
                value = str(value) == "True"
            newAllergies[key] = value
        newProfile.setAllergies(newAllergies)

    if "sex" in updates:
        newProfile.setSex(updates["sex"], True)

    if "age" in updates:
        newProfile.setAge(int(extract_numbers(updates["age"])), True)

    if "height" in updates:
        newProfile.setHeight(float(extract_numbers(updates["height"])), True, True)

    if "weight" in updates:
        newProfile.setWeight(float(extract_numbers(updates["weight"])), True, True)

    if "sportLevel" in updates:
        try:
            newProfile.setSportLevelInt(int(extract_numbers(updates["sportLevel"])), True)
        except:
            frase = text_similarity(phrase=updates["sportLevel"], texts=sport_list)
            newProfile.setSportLevel(frase, True)

    if "objective" in updates:
        try:
            newProfile.setObjectiveInt(int(extract_numbers(updates["objective"])), True)
        except:
            frase = text_similarity(phrase=updates["objective"], texts=goal_list)
            newProfile.setObjective(frase, True)

    verify_agent = VerifyDataAgent()
    coherent = verify_agent.verify_data_of_user(newProfile)

    if True:
        userProfile.updateFromUserProfile(newProfile)

    return coherent