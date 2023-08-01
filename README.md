# OpenAI Model Router

Given the number of OpenAI models, it can get tricky to identify which model to call for a given prompt. So we built the Model Router, to dynamically select the *most appropriate model* for our prompt.

List of supported models: `gpt-3.5-turbo, gpt-3.5-turbo-0613, gpt-3.5-turbo-16k, gpt-3.5-turbo-16k-0613`
Support for more models coming soon ;)

## Usage

Simply use the Model Router instead of using OpenAI directly. And, no need to specify the model anymore!

### Example 1: Simple Message

#### Before
```python
import openai
openai.api_key = "sk-..."

chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo",
    messages=[{"role": "user", "content": "Hello world"}]
)

print(chat_completion.choices[0].message.content)
```

#### After
```python
from model_router import openai # import from model_router instead
openai.api_key = "sk-..."

chat_completion = openai.ChatCompletion.create(
    # skip the model
    messages=[{"role": "user", "content": "Hello world"}]
)

print(chat_completion.choices[0].message.content)
```

### Example 2: Function Calling

#### Before
```python
import openai
openai.api_key = "sk-..."

chat_completion = openai.ChatCompletion.create(
    model="gpt-3.5-turbo-0613",
    messages=[{"role": "user", "content": "What's the weather like in Boston?"}],
    functions=[...],
    function_call="auto",
)

print(chat_completion.choices[0].message.content)
```

#### After
```python
from model_router import openai # import from model_router instead
openai.api_key = "sk-..."

chat_completion = openai.ChatCompletion.create(
    # skip the model
    messages=[{"role": "user", "content": "What's the weather like in Boston?"}],
    functions=[...],
    function_call="auto",
)

print(chat_completion.choices[0].message.content)
```

## Questions/Feedback

For any questions/feedback, please reach out to [@sambuddha_basu](https://twitter.com/sambuddha_basu)
