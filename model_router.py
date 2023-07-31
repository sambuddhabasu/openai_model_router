import openai as oai

class OpenAI:
    @property
    def api_key(self):
        return oai.api_key

    @api_key.setter
    def api_key(self, value):
        oai.api_key = value

    class ChatCompletion:
        @staticmethod
        def create(messages, **kwargs):
            model = 'gpt-3.5-turbo'
            if 'functions' in kwargs:
                model = 'gpt-3.5-turbo-0613'

            return oai.ChatCompletion.create(model=model, messages=messages, **kwargs)

openai = OpenAI()
