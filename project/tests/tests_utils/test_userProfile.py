import pytest
from utils.userProfile import UserProfile

@pytest.fixture
def user_profile():
    return UserProfile(
        allergies={"HasDairy": True, "HasGluten": False},
        sex="Masculino", age=30, height=175, weight=70, 
        sportLevel="Ejercicio moderado (3-5 días a la semana)", objective="Adelgazar"
    )

def test_set_and_get_sex(user_profile):
    user_profile.setSex("Femenino")
    assert user_profile.getSex() == "Femenino"


def test_set_and_get_sex_bool(user_profile):
    user_profile.setSex("Femenino")
    assert user_profile.getIsMan() == False

def test_set_and_get_age(user_profile):
    user_profile.setAge(25)
    assert user_profile.getAge() == 25

def test_bmi_calculation(user_profile):
    user_profile.updateBMI()
    assert user_profile.getBMI() == pytest.approx(22.86, rel=1e-2)
    assert user_profile.getBMIType() == "Peso ideal"

def test_caloric_intake(user_profile):
    user_profile.updateKcalRecommended()
    min_kcal, max_kcal = user_profile.getKcals()
    assert min_kcal > 0
    assert max_kcal > 0

def test_allergies(user_profile):
    assert user_profile.getAllergies() == {"HasDairy": True}

def test_update_allergies(user_profile):
    user_profile.setAllergies({"HasDairy": False, "HasGluten": True})
    assert user_profile.getAllergies() == {"HasGluten": True}

def test_set_and_get_height(user_profile):
    pastBMI = user_profile.getBMI()
    pastMinkcal = user_profile.getMinKcal()
    pastMaxKcal = user_profile.getMaxKcal()

    user_profile.setHeight(180)
    
    assert user_profile.getHeight() == 180
    
    assert user_profile.getBMI() != pastBMI
    min_kcal, max_kcal = user_profile.getKcals()
    assert min_kcal != pastMinkcal
    assert max_kcal != pastMaxKcal

def test_set_and_get_weight(user_profile):
    pastBMI = user_profile.getBMI()
    pastMinkcal = user_profile.getMinKcal()
    pastMaxKcal = user_profile.getMaxKcal()
    
    user_profile.setWeight(80)
    
    assert user_profile.getWeight() == 80
    
    assert user_profile.getBMI() != pastBMI
    min_kcal, max_kcal = user_profile.getKcals()
    assert min_kcal != pastMinkcal
    assert max_kcal != pastMaxKcal

def test_set_and_get_sport_level(user_profile):
    pastMinkcal = user_profile.getMinKcal()
    pastMaxKcal = user_profile.getMaxKcal()
    
    user_profile.setSportLevel("Poco o ningún ejercicio (Sentado)")
    
    assert user_profile.getSportLevel() == 1
    assert user_profile.getSportLevelString() == "Poco o ningún ejercicio (Sentado)"
    
    min_kcal, max_kcal = user_profile.getKcals()
    assert min_kcal != pastMinkcal
    assert max_kcal != pastMaxKcal

def test_set_and_get_objetive_1(user_profile):
    pastMinkcal = user_profile.getMinKcal()
    pastMaxKcal = user_profile.getMaxKcal()
    
    user_profile.setObjective("Ganar músculo")
    
    assert user_profile.getObjective() == 1
    assert user_profile.getObjectiveString() == "Ganar músculo"
    
    min_kcal, max_kcal = user_profile.getKcals()
    assert min_kcal != pastMinkcal
    assert max_kcal != pastMaxKcal

def test_set_and_get_objetive_2(user_profile):
    pastMinkcal = user_profile.getMinKcal()
    pastMaxKcal = user_profile.getMaxKcal()
    
    user_profile.setObjective("Mantenerme sano")
    
    assert user_profile.getObjective() == 0
    assert user_profile.getObjectiveString() == "Mantenerme sano"
    
    min_kcal, max_kcal = user_profile.getKcals()
    assert min_kcal != pastMinkcal
    assert max_kcal != pastMaxKcal

def test_toString(user_profile):
    assert user_profile.toString() == """Allergies: {'HasDairy': True}
Sex: Masculino
Age: 30
Height: 175 cm
Weight: 70 kg
Sport Level: Ejercicio moderado (3-5 días a la semana)
Objective: Adelgazar
BMI: 22.857142857142858 (Peso ideal)
Recommended Caloric Intake: 1916.671875 - 2300.00625 kcal"""