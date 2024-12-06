from .agent import Agent

class VerifyDataAgent(Agent):

    def __init__(self, context="you have to check that the data you get from a user makes sense or is not coherent, for example a 180cm tall man weighing 30kg is not coherent data, but a woman of 160cm and 50kg is coherent. You must return ONLY one output word, ‘True’ if they are consistent and ‘False’ if they are not consistent. Only say False in very rare situations, there are a lot of different bodies."):
        super().__init__(context)

    def receive_message(self, message, history=False):
        response = super().receive_message(message,history)

        while "True" not in response and "False" not in response:
            response = super().receive_message("Respond only 'True' if the data is consistent and 'False' if it is not"+message,history)

        return ("True" in response)

    def verify_data(self, age, height, weight):
        message = "AGE: "+str(age)+" HEIGHT: "+str(height)+" WEIGHT: "+str(weight)
        response = self.receive_message(message, False)
        return response

