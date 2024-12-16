from .agent import Agent
from utils.userProfile import UserProfile

CONTEXT_PREDETERM = """
Tienes que evaluar si los datos de una persona son coherentes.
Tus reglas internas para determinar que algo es coherente son:
- Un IMC o BMI coherentes está entre 12 y 60.
- Una altura coherentes está entre 54cm y 272cm.
- Un peso coherente está entre 4kg y 700kg.

Si todos los datos son coherentes devuelve 'True'.
Si algún dato no es coherente debes devolver una breve descripción sin mencionar tus reglas internas para que el usuario entienda que tiene mal, las posibles respuestas son:
1. La altura y/o peso no son coherentes: debes dar breve explicación de por qué el usuario debería revisar si esos campos son correctos.
2. IMC no coherente, mientras que tanto la altura y el peso tienen valores extraños, pero coherentes: debes dar una explicación de porque el usuario debería revisar si ha puesto bien la altura y el peso.
3. IMC no coherente y altura tiene un valor extraño, pero coherente y el peso tiene un valor normal: debes dar una explciación para que el usuario revise la altura.
4. IMC no coherente y peso tiene un valor extraño, pero coherente y la altura tiene un valor normal: debes dar una explicación para que el usuario revise el peso.
5. IMC no coherente y peso y altura con valores normales y coherentes: debes dar una explicación de cuándo es el valor de IMC y porqué es extraño dicho valor.
6. Todo es incoherente: debes dar una breve explicación diciendo que el usuario debería revisar todos los valores.
"""

class VerifyDataAgent(Agent):

    def __init__(self, context:str=CONTEXT_PREDETERM)->None:
        super().__init__(context)

    def receive_message(self, message:str, history:bool=False)->str:
        response = super().receive_message(message,history)

        return response

    def verify_data_of_user(self, user_profile:UserProfile)->str:
        if user_profile.getBMI() < 12 or user_profile.getBMI() > 60 or user_profile.getHeight() < 54 or user_profile.getHeight() > 272 or user_profile.getWeight() < 4 or user_profile.getWeight() > 700:
            message = user_profile.weight_height_bmi_toString()
            response = self.receive_message(message, False)
            return response
        else:
            return 'True'

