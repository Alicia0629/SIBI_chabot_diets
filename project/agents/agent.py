import cohere
from config import KEY_COHERE, MODEL_COHERE

co = cohere.ClientV2(KEY_COHERE)

class Agent:
    def __init__(self, context="You are a nutrition assistant"):
        self.model = MODEL_COHERE
        self.messages = [{'role':'system', 'content':context}]
        self.context = context

    def receive_message(self, message, history=True):
        if history:
            messages = self.messages.append({'role':'user', 'content':message})
        else:
            messages = [{'role':'system', 'content':self.context}, {'role':'user', 'content':message}]
        
        response = co.chat(model=self.model, messages=messages)
        
        if history:
            self.messages.append({'role':'assistant', 'content':response.message.content})

        return response.message.content[0].text

