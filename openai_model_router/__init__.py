import openai as oai
import tiktoken


encoding = tiktoken.get_encoding("cl100k_base")

# Implementation based off https://community.openai.com/t/how-to-calculate-the-tokens-when-using-function-call/266573/11
def num_tokens_from_functions(functions):
        """Return the number of tokens used by a list of functions."""
        num_tokens = 0
        for function in functions:
            function_tokens = len(encoding.encode(function['name']))
            function_tokens += len(encoding.encode(function['description']))

            if 'parameters' in function:
                parameters = function['parameters']
                if 'properties' in parameters:
                    for propertiesKey in parameters['properties']:
                        function_tokens += len(encoding.encode(propertiesKey))
                        v = parameters['properties'][propertiesKey]
                        for field in v:
                            if field == 'type':
                                function_tokens += 2
                                function_tokens += len(encoding.encode(v['type']))
                            elif field == 'description':
                                function_tokens += 2
                                function_tokens += len(encoding.encode(v['description']))
                            elif field == 'enum':
                                function_tokens -= 3
                                for o in v['enum']:
                                    function_tokens += 3
                                    function_tokens += len(encoding.encode(o))
                            else:
                                print(f"Warning: not supported field {field}")
                    function_tokens += 11

            num_tokens += function_tokens

        num_tokens += 12
        return num_tokens

# Implementation based off https://github.com/openai/openai-cookbook/blob/main/examples/How_to_count_tokens_with_tiktoken.ipynb
def num_tokens_from_messages(messages):
    """Return the number of tokens used by a list of messages."""
    tokens_per_message = 3
    tokens_per_name = 1
    num_tokens = 0
    for message in messages:
        num_tokens += tokens_per_message
        for key, value in message.items():
            num_tokens += len(encoding.encode(value))
            if key == "name":
                num_tokens += tokens_per_name
    num_tokens += 3  # every reply is primed with <|start|>assistant<|message|>
    return num_tokens

def add_longer_context_suffix(input_tokens):
    return '-16k' if input_tokens > 4096 else ''

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
            input_tokens = num_tokens_from_messages(messages)
            if 'functions' in kwargs:
                # Function calls
                input_tokens += num_tokens_from_functions(kwargs['functions'])
                model += add_longer_context_suffix(input_tokens) + '-0613'
            else:
                # Simple calls
                model += add_longer_context_suffix(input_tokens)

            return oai.ChatCompletion.create(model=model, messages=messages, **kwargs)

openai = OpenAI()
