from .agent import Agent
from utils.userProfile import UserProfile
from config import KEY_DETECTCHANGE

CONTEXT_PREDETERM = """
Tienes que valorar si el usuario ha cambiado algún detalle sobre su perfil.
Los datos del perfil del usuario son:
            [allergies] las cuales se guardan en un diccionario con las clave "HasDairy","HasGluten", "HasEgg", "HasFish", "HasShellfish","HasTreenut","HasPeanut","HasSoy","HasSesame","HasMustard"
            [sex] "M" para hombre, "F" para mujer
            [age] edad en años
            [height] altura en centimetros
            [weight] peso en kilogramos
            [sportLevel] Devuelveme un número según la actividad deportiva que puede ser: 1,2,3,4 o 5. Esos valores significan:
                    -"Poco o ningún ejercicio (Sentado)": 1
                    -"Ejercicio ligero (1-3 días a la semana)": 2
                    -"Ejercicio moderado (3-5 días a la semana)": 3
                    -"Ejercicio fuerte (6-7 días a la semana)": 4
                    -"Ejercicio muy fuerte (dos veces al día, entrenamientos muy duros)": 5
            [objective] Devuelveme un número según la  objetivo del usuario que puede ser: -1, 0 o 1. Esos valores significan:
                    -"Mantenerme sano":0
                    -"Ganar músculo":1
                    -"Adelgazar":-1
Te pasaré el perfil del usuario, el mensaje que ha mandado y debes decirme si hay algún cambio en su perfil.
Si no hay cambio devuelveme 'False', pero si hay cambios devuelveme una lista separada de ; de las variables que han cambiado, cada variable se representará su nombre rodeada por corchetes y a continuación su valor nuevo
"""

class DetectChangeDataAgent(Agent):

    def __init__(self, context:str=CONTEXT_PREDETERM)->None:
        super().__init__(context=context, key=KEY_DETECTCHANGE)

    def receive_message(self, message:str, history:bool=False)->str:
        response = super().receive_message(message,history)

        return response

    def analyse_message(self, message:str, user_profile:UserProfile)->str:
        newMessage = "mensaje: '"+message+"' perfil usuario actualmente: "+user_profile.toString()
        response = self.receive_message(message=newMessage)
        
        return response

