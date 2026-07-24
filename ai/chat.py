from ai.ollama import Ollama


class ChatAI:


    def __init__(self):

        self.ai = Ollama()



    def ask(self, text):

        return self.ai.chat(text)



chat_ai = ChatAI()