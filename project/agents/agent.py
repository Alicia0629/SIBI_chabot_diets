import cohere

co = cohere.ClientV2("CjRinfo0Wsy3g0DbVPIS6VKDn9Ts9yl7KO4cWkXr")

class Agent:
    def __init__(self, context="Eres un assitente sobre nutrición"):
        self.context = context
        self.model = "command-r-plus-08-2024"

    def receive_message_withoutHistory(self, message):
        messages=[{'role':'system', 'content':self.context},
                {'role':'user', 'content':message}]

        response = co.chat(model=self.model, messages=messages)

        return response.message.content[0].text

