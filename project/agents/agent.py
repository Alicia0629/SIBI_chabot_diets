import cohere
from config import KEY_AGENTS, MODEL_COHERE


class Agent:
    def __init__(self, context:str="You are a nutrition assistant", key:str=KEY_AGENTS)->None:
        self.co = cohere.ClientV2(key)
        self.model = MODEL_COHERE
        self.messages = [{'role':'system', 'content':context}]
        self.context = context

    def receive_message(self, message:str, history:bool=True)->str:
        if history:
            self.messages.append({'role':'user', 'content':message})
            print(self.messages)
            messages = self.messages
        else:
            messages = [{'role':'system', 'content':self.context}, {'role':'user', 'content':message}]
                
        response = self.co.chat(model=self.model, messages=messages)
        
        if history:
            self.messages.append({'role':'assistant', 'content':response.message.content})

        return response.message.content[0].text

