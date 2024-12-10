from .agent import Agent
from utils.userProfile import UserProfile

CONTEXT_PREDETERM = """Eres un expero un nutrición
Devuelve un texto con tres párrafos con no más de 2 líneas cada párrafo.
En el primer párrafo describas al usuario y qué quiere conseguir. Dile datos como tu imc.
En el segundo párrafo dile si debería hacer algún cambio con la cantidad de deporte que hace o si está actuando correctamente.
En el tercer párrafo dile consejos sobre qué debería comer. Comenta también las kcal que debería consumir.
"""

CONTEXT_PREDETERM = """Eres un expero un nutrición
Devuelve un texto super esquemático que debde incluir:
- Definición perfil del usuario (sólo lo más importante a nivel dietético)
- Si las necesidades deportivas se están cumpliendo
- ¿Cómo debería comer?
"""

class DefUserAgent(Agent):

    def __init__(self, context=CONTEXT_PREDETERM):
        super().__init__(context)

    def receive_message(self, message, history=False):
        response = super().receive_message(message,history)

        return response

    def define_user(self, user_profile):
        message = user_profile.toString()
        response = self.receive_message(message, False)
        return response

