from utils.userProfile import UserProfile

from agents.verify_data_agent import VerifyDataAgent

def changeData(userProfile:UserProfile, AIMessage:str):
    newProfile = userProfile.clone()
    
    pairs = AIMessage.split(";")
    updates = {}
    for pair in pairs:
        if pair.strip():
            key, value = pair.split("]")
            key = key.strip("[").strip()
            value = value.strip()
            updates[key] = value

    if "allergies" in updates:
        oldAllergies = newProfile.getAllergies()
        updateAllergies = eval(updates["allergies"])
        newAllergies = {}
        for key, value in oldAllergies.items():
            newAllergies[key] = value
        for key, value in updateAllergies.items():
            newAllergies[key] = value
        newProfile.setAllergies(newAllergies)

    if "sex" in updates:
        newProfile.setSex(updates["sex"], True)

    if "age" in updates:
        newProfile.setAge(int(updates["age"]), True)

    if "height" in updates:
        newProfile.setHeight(float(updates["height"]), True, True)

    if "weight" in updates:
        newProfile.setWeight(float(updates["weight"]), True, True)

    if "sportLevel" in updates:
        newProfile.setSportLevelInt(int(updates["sportLevel"]), True)

    if "objective" in updates:
        newProfile.setObjectiveInt(int(updates["objective"]), True)

    verify_agent = VerifyDataAgent()
    coherent = verify_agent.verify_data_of_user(newProfile)

    if True:
        userProfile.updateFromUserProfile(newProfile)

    return coherent