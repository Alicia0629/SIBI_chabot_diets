
def calculate_bmi(weight:float, height:float) -> float:
    """
    Calculates the Body Mass Index (BMI) given the weight and height.

    Parameters:
        weight (float): The person's weight in kilograms.
        height (float): The person's height in centimiters

    Returns:
        float: The BMI value calculated as weight divided by the square of the height.

    """
    height_meters = height / 100
    bmi = weight / (height_meters**2)
    return bmi

def bmi_type(bmi:float) -> str:
    """
    Determines the BMI classification based on the given BMI value.

    Parameters:
        imc (float): The Body Mass Index (BMI) value.

    Returns:
        str: The BMI classification as a string:
    """
    if bmi < 18.5:
        return "Peso bajo"
    elif bmi < 25:
        return "Peso ideal"
    elif bmi < 30:
        return "Sobrepeso"
    elif bmi < 35:
        return "Obesidad leve"
    elif bmi < 40:
        return "Obesidad moderada"
    return "Obesidad mórbida"


def calculate_kcal_to_mantein_weight(isMan:bool, age:int, sportLevel:int, weight:float, height:float) -> float: 
    """
    Calculates the daily caloric intake required to maintain the current weight
    based on the revised Harris-Benedict equations by Mifflin and St Jeor (1990).

    Parameters:
        isMan (bool): Indicates if the person is male (True) or female (False).
        age (int): The person's age in years.
        sportLevel (int): The person's activity level, where:
            - 1: Little or no exercise (TMB x 1.2)
            - 2: Light exercise (1-3 days per week, TMB x 1.375)
            - 3: Moderate exercise (3-5 days per week, TMB x 1.55)
            - 4: Intense exercise (6-7 days per week, TMB x 1.725)
            - 5: Very intense exercise (twice a day, hard training, TMB x 1.9).
        weight (float): The person's weight in kilograms.
        height (float): The person's height in centimeters.

    Returns:
        float: The total daily caloric intake required (in kcal) based on the
        Basal Metabolic Rate (TMB) and activity level.

    Formula:
        - For men: TMB = (10 x weight) + (6.25 x height) - (5 x age) + 5
        - For women: TMB = (10 x weight) + (6.25 x height) - (5 x age) - 161

    The calculated TMB is then multiplied by a factor based on `sportLevel` to determine
    the recommended daily caloric intake.
    """
    assert sportLevel in [1,2,3,4,5]
    tmb = 10*weight
    tmb += 6.25*height
    tmb -= 5*age
    if isMan:
        tmb += 5
    else:
        tmb -=161

    if sportLevel == 1:
        tmb *= 1.2
    elif sportLevel == 2:
        tmb *= 1.375
    elif sportLevel == 3:
        tmb *= 1.55
    elif sportLevel == 4:
        tmb *= 1.725
    elif sportLevel == 5:
        tmb *=1.9

    return tmb

