from utils.health_calculators import calculate_bmi, bmi_type, calculate_kcal_to_mantein_weight

class UserProfile:
    """
    Class to manage a user's profile including health information and goals.
    Calculates BMI and recommends daily caloric intake based on user inputs.
    """

    def __init__(self, allergies: dict, sex: str, age: int, height: float, weight: float, sportLevel: str, objective: str):
        """
        Initializes the user's profile with health data.

        Parameters:
            allergies (dict): Dictionary of allergies and their statuses (True or False).
            sex (str): Gender of the user (starts with "M" for male, starts with "F" for female).
            age (int): Age of the user (years).
            height (float): Height of the user (in centimeters).
            weight (float): Weight of the user (in kilograms).
            sportLevel (str): User's activity level.
            objective (str): User's goal (e.g., "Mantenerme sano", "Ganar músculo", "Adelgazar").
        """
        self.setAllergies(allergies)
        self.setSex(sex, False)
        self.setAge(age, False)
        self.setSportLevel(sportLevel, False)
        self.setObjective(objective, False)
        self.setHeight(height, False, False)
        self.setWeight(weight, False, False)
        self._definition = None

        self.updateBMI()
        self.updateKcalRecommended()

    def clone(self):
        """
        Creates and returns a copy of the current object.
        """
        return UserProfile(
            allergies=self.getAllergies(),
            sex=self.getSex(),
            age=self.getAge(),
            height=self.getHeight(),
            weight=self.getWeight(),
            sportLevel=self.getSportLevelString(),
            objective=self.getObjectiveString()
        )
    
    def updateFromUserProfile(self, other_user: "UserProfile"):
        """
        Updates all attributes of the current user profile with the attributes of another user profile.

        Parameters:
            other_user (UserProfile): Another UserProfile instance from which to copy data.
        """
        self.setAllergies(other_user.getAllergies())
        self.setSex(other_user.getSex(), updateKcal=False)
        self.setAge(other_user.getAge(), updateKcal=False)
        self.setHeight(other_user.getHeight(), updateKcal=False, updateBMI=False)
        self.setWeight(other_user.getWeight(), updateKcal=False, updateBMI=False)
        self.setSportLevel(other_user.getSportLevelString(), updateKcal=False)
        self.setObjective(other_user.getObjectiveString(), updateKcal=False)
        self._definition = None

        self.updateBMI()
        self.updateKcalRecommended()


    def setAllergies(self, allergies: dict):
        """
        Sets the user's allergies dictionary. Only keeps allergies with True values.

        Parameters:
            allergies (dict): Dictionary of allergies.
        """
        self._allergies = {}

        for key, value in allergies.items():
            if value == True:
                self._allergies[key] = value

    def getAllergies(self) -> dict:
        """
        Returns the dictionary of allergies.

        Returns:
            dict: The user's allergies.
        """
        return self._allergies

    def setSex(self, sex: str, updateKcal: bool = True):
        """
        Sets the user's sex and optionally updates the recommended caloric intake and BMI.

        Parameters:
            sex (str): Gender of the user (starts with "M" for male, starts with "F" for female).
            updateKcal (bool): Whether to update the recommended caloric intake (default True).
        """
        self._isMan = (sex[0] == "M")
        if updateKcal:
            self.updateKcalRecommended()

    def getSex(self) -> str:
        """
        Returns the user's gender.

        Returns:
            str: "Masculino" if male, "Femenino" if female.
        """
        return "Masculino" if self._isMan else "Femenino"

    def getIsMan(self) -> bool:
        """
        Returns whether the user is male.

        Returns:
            bool: True if male, False if female.
        """
        return self._isMan

    def setAge(self, age: int, updateKcal: bool = True):
        """
        Sets the user's age and optionally updates the recommended caloric intake and BMI.

        Parameters:
            age (int): Age of the user (years).
            updateKcal (bool): Whether to update the recommended caloric intake (default True).
        """
        assert 0 < age < 130, "Age must be between 1 and 129"
        self._age = age
        if updateKcal:
            self.updateKcalRecommended()

    def getAge(self) -> int:
        """
        Returns the user's age.

        Returns:
            int: The user's age.
        """
        return self._age

    def setHeight(self, height: float, updateKcal: bool = True, updateBMI: bool = True):
        """
        Sets the user's height and optionally updates the recommended caloric intake and BMI.

        Parameters:
            height (float): Height of the user (in centimeters).
            updateKcal (bool): Whether to update the recommended caloric intake (default True).
            updateBMI (bool): Whether to update the BMI (default True).
        """
        self._height = height
        if updateKcal:
            self.updateKcalRecommended()
        if updateBMI:
            self.updateBMI()

    def getHeight(self) -> float:
        """
        Returns the user's height.

        Returns:
            float: The user's height in centimeters.
        """
        return self._height

    def setWeight(self, weight: float, updateKcal: bool = True, updateBMI: bool = True):
        """
        Sets the user's weight and optionally updates the recommended caloric intake and BMI.

        Parameters:
            weight (float): Weight of the user (in kilograms).
            updateKcal (bool): Whether to update the recommended caloric intake (default True).
            updateBMI (bool): Whether to update the BMI (default True).
        """
        self._weight = weight
        if updateKcal:
            self.updateKcalRecommended()
        if updateBMI:
            self.updateBMI()

    def getWeight(self) -> float:
        """
        Returns the user's weight.

        Returns:
            float: The user's weight in kilograms.
        """
        return self._weight

    def setSportLevel(self, sportLevel: str, updateKcal: bool = True):
        """
        Sets the user's activity level based on the provided string.

        Parameters:
            sportLevel (str): The user's activity level (e.g., "Ejercicio ligero").
            updateKcal (bool): Whether to update the recommended caloric intake (default True).
        """
        sport_map = {
            "Poco o ningún ejercicio (Sentado)": 1,
            "Ejercicio ligero (1-3 días a la semana)": 2,
            "Ejercicio moderado (3-5 días a la semana)": 3,
            "Ejercicio fuerte (6-7 días a la semana)": 4,
            "Ejercicio muy fuerte (dos veces al día, entrenamientos muy duros)": 5
        }
        self._sportLevel = sport_map.get(sportLevel)

        if updateKcal:
            self.updateKcalRecommended()

    def setSportLevelInt(self, sportLevel: int, updateKcal: bool = True):
        """
        Sets the user's activity level.

        Parameters:
            sportLevel (int): The user's activity level (1,2,3,4,5).
            updateKcal (bool): Whether to update the recommended caloric intake (default True).
        """
        assert 1 <= sportLevel <= 5
        self._sportLevel = sportLevel
        if updateKcal:
            self.updateKcalRecommended()

    def getSportLevel(self) -> int:
        """
        Returns the user's activity level.

        Returns:
            int: The user's activity level (1-5).
        """
        return self._sportLevel
    
    def getSportLevelString(self) -> str:
        """
        Returns the activity level as a string.

        Returns:
            str: Activity level description.
        """
        sport_map = {
            1: "Poco o ningún ejercicio (Sentado)",
            2: "Ejercicio ligero (1-3 días a la semana)",
            3: "Ejercicio moderado (3-5 días a la semana)",
            4: "Ejercicio fuerte (6-7 días a la semana)",
            5: "Ejercicio muy fuerte (dos veces al día, entrenamientos muy duros)"
        }
        return sport_map.get(self._sportLevel)

    def setObjective(self, objective: str, updateKcal: bool = True):
        """
        Sets the user's goal (e.g., "Mantenerme sano", "Ganar músculo", "Adelgazar").

        Parameters:
            objective (str): The user's goal.
            updateKcal (bool): Whether to update the recommended caloric intake (default True).
        """
        goal_map = {
            "Mantenerme sano": 0,
            "Ganar músculo": 1,
            "Adelgazar": -1
        }
        self._objetive = goal_map.get(objective)

        if updateKcal:
            self.updateKcalRecommended()

    def setObjectiveInt(self, objective: int, updateKcal: bool = True):
        """
        Sets the user's goal.

        Parameters:
            objective (int): The user's goal. (-1,0,1)
            updateKcal (bool): Whether to update the recommended caloric intake (default True).
        """
        
        self._objetive = objective

        if updateKcal:
            self.updateKcalRecommended()

    def getObjective(self) -> int:
        """
        Returns the user's goal.

        Returns:
            int: The user's goal (0 for maintaining weight, 1 for gaining muscle, -1 for losing weight).
        """
        return self._objetive
    
    def getObjectiveString(self) -> str:
        """
        Returns the user's goal as a string.

        Returns:
            str: The user's goal description.
        """
        goal_map = {
            0: "Mantenerme sano",
            1: "Ganar músculo",
            -1: "Adelgazar"
        }
        return goal_map.get(self._objetive)

    def updateBMI(self):
        """
        Updates the user's BMI based on the current weight and height.
        """
        self._bmi = calculate_bmi(self._weight, self._height)

    def getBMI(self) -> float:
        """
        Returns the user's BMI.

        Returns:
            float: The user's BMI value.
        """
        return self._bmi

    def getBMIType(self) -> str:
        """
        Returns the user's BMI classification based on the BMI value.

        Returns:
            str: The classification (e.g., "Peso bajo", "Peso ideal").
        """
        return bmi_type(self._bmi)

    def updateKcalRecommended(self):
        """
        Updates the recommended daily caloric intake based on the user's goal and activity level.
        """
        kcal_to_mantein = calculate_kcal_to_mantein_weight(self._isMan, self._age, self._sportLevel, self._weight, self._height)
        
        if self._objetive == -1:  # Lose weight
            self._minKcal = kcal_to_mantein * (1 - 0.25)
            self._maxKcal = kcal_to_mantein * (1 - 0.10)
        elif self._objetive == 0:  # Maintain weight
            self._minKcal = kcal_to_mantein
            self._maxKcal = kcal_to_mantein
        elif self._objetive == 1:  # Gain muscle
            self._minKcal = kcal_to_mantein * (1 + 0.10)
            self._maxKcal = kcal_to_mantein * (1 + 0.20)

    def getKcals(self):
        """
        Returns the user's recommended daily caloric intake range.

        Returns:
            list: A list containing the minimum and maximum daily caloric intake.
        """
        return [self._minKcal, self._maxKcal]

    def getMinKcal(self):
        """
        Returns the user's minimum recommended daily caloric intake.

        Returns:
            float: The minimum daily caloric intake.
        """
        return self._minKcal

    def getMaxKcal(self):
        """
        Returns the user's maximum recommended daily caloric intake.

        Returns:
            float: The maximum daily caloric intake.
        """
        return self._maxKcal
    
    def setDefinition(self, definition):
        """
        Set's a definition for the profile of the user.
        """
        self._definition = definition
    
    def getDefinition(self):
        """
        Return the user's definition of profile.

        Returns:
            str: A string containing the definition of the user.
        """
        return self._definition
    

    
    def weight_height_bmi_toString(self) -> str:
        """
        Returns a string representation of the user's profile weight, height and bmi.
        
        Returns:
            str: A string containing the user profile details of weight, height and bmi.
        """
        return (f"Height: {self.getHeight()} cm\n"
                f"Weight: {self.getWeight()} kg\n"
                f"BMI: {self.getBMI()} ({self.getBMIType()})\n")
    
    def toString(self) -> str:
        """
        Returns a string representation of the user's profile.
        
        Returns:
            str: A string containing all the user profile details.
        """
        return (f"Allergies: {self.getAllergies()}\n"
                f"Sex: {self.getSex()}\n"
                f"Age: {self.getAge()}\n"
                f"Height: {self.getHeight()} cm\n"
                f"Weight: {self.getWeight()} kg\n"
                f"Sport Level: {self.getSportLevelString()}\n"
                f"Objective: {self.getObjectiveString()}\n"
                f"BMI: {self.getBMI()} ({self.getBMIType()})\n"
                f"Recommended Caloric Intake: {self.getMinKcal()} - {self.getMaxKcal()} kcal")
