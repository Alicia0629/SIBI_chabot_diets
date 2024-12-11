from .agent import Agent
from utils.userProfile import UserProfile


CONTEXT_PREDETERM = """Eres un expero un nutrición
Devuelve un texto de no más de 10 líneas.
El texto debe describa nutricionalmente al usuario y tips principales sobre alimentación, ten encuenta en esta sus alergias y si estas le pueden afectar en algo. Comenta cosas como kcal diarias recomendadas y su indice de masa corporal.
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

