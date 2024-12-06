import pytest
from utils.health_calculators import calculate_bmi, bmi_type, calculate_kcal_to_mantein_weight

# Test for calculate_bmi
def test_calculate_bmi():
    weight = 70  # kg
    height = 175  # cm
    expected_bmi = weight / ((height / 100) ** 2)  # BMI = 70 / (1.75^2) = 22.86
    assert calculate_bmi(weight, height) == pytest.approx(expected_bmi, rel=1e-2)

def test_calculate_bmi_underweight():
    weight = 50  # kg
    height = 160  # cm
    expected_bmi = weight / ((height / 100) ** 2)  # BMI = 50 / (1.6^2) = 19.53
    assert calculate_bmi(weight, height) == pytest.approx(expected_bmi, rel=1e-2)

def test_calculate_bmi_overweight():
    weight = 85  # kg
    height = 170  # cm
    expected_bmi = weight / ((height / 100) ** 2)  # BMI = 85 / (1.7^2) = 29.41
    assert calculate_bmi(weight, height) == pytest.approx(expected_bmi, rel=1e-2)

# Test for bmi_type
def test_bmi_type_underweight():
    bmi = 16.0
    assert bmi_type(bmi) == "Peso bajo"

def test_bmi_type_ideal():
    bmi = 22.0
    assert bmi_type(bmi) == "Peso ideal"

def test_bmi_type_overweight():
    bmi = 28.0
    assert bmi_type(bmi) == "Sobrepeso"

def test_bmi_type_obesity_1():
    bmi = 32.0
    assert bmi_type(bmi) == "Obesidad leve"

def test_bmi_type_obesity_2():
    bmi = 36.0
    assert bmi_type(bmi) == "Obesidad moderada"

def test_bmi_type_obesity_3():
    bmi = 42.0
    assert bmi_type(bmi) == "Obesidad mórbida"

# Test for calculate_kcal_to_mantein_weight
def test_calculate_kcal_to_mantein_weight_male_1():
    weight = 70  # kg
    height = 175  # cm
    age = 25
    sport_level = 3  # Moderate exercise
    is_man = True
    expected_kcal = (10 * weight) + (6.25 * height) - (5 * age) + 5  # TMB for male
    expected_kcal *= 1.55  # Activity multiplier for moderate exercise
    assert calculate_kcal_to_mantein_weight(is_man, age, sport_level, weight, height) == pytest.approx(expected_kcal, rel=1e-2)

def test_calculate_kcal_to_mantein_weight_male_2():
    weight = 80  # kg
    height = 185  # cm
    age = 27
    sport_level = 4  
    is_man = True
    expected_kcal = (10 * weight) + (6.25 * height) - (5 * age) + 5  # TMB for male
    expected_kcal *= 1.725
    assert calculate_kcal_to_mantein_weight(is_man, age, sport_level, weight, height) == pytest.approx(expected_kcal, rel=1e-2)


def test_calculate_kcal_to_mantein_weight_female_1():
    weight = 60  # kg
    height = 165  # cm
    age = 30
    sport_level = 2  # Light exercise
    is_man = False
    expected_kcal = (10 * weight) + (6.25 * height) - (5 * age) - 161  # TMB for female
    expected_kcal *= 1.375  # Activity multiplier for light exercise
    assert calculate_kcal_to_mantein_weight(is_man, age, sport_level, weight, height) == pytest.approx(expected_kcal, rel=1e-2)


def test_calculate_kcal_to_mantein_weight_female_2():
    weight = 50  # kg
    height = 170  # cm
    age = 23
    sport_level = 5
    is_man = False
    expected_kcal = (10 * weight) + (6.25 * height) - (5 * age) - 161  # TMB for female
    expected_kcal *= 1.9
    assert calculate_kcal_to_mantein_weight(is_man, age, sport_level, weight, height) == pytest.approx(expected_kcal, rel=1e-2)

def test_calculate_kcal_to_mantein_weight_invalid_sport_level():
    # This should raise an AssertionError since sport level is out of the valid range
    with pytest.raises(AssertionError):
        calculate_kcal_to_mantein_weight(True, 25, 6, 70, 175)  # sportLevel 6 is invalid

def test_calculate_kcal_to_mantein_weight_edge_case():
    # Test edge case with very low activity
    weight = 80  # kg
    height = 180  # cm
    age = 40
    sport_level = 1  # No exercise
    is_man = True
    expected_kcal = (10 * weight) + (6.25 * height) - (5 * age) + 5  # TMB for male
    expected_kcal *= 1.2  # Activity multiplier for low/no exercise
    assert calculate_kcal_to_mantein_weight(is_man, age, sport_level, weight, height) == pytest.approx(expected_kcal, rel=1e-2)
