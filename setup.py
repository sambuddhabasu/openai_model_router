from setuptools import setup, find_packages

setup(
    name='openai-model-router',
    version='0.1',
    packages=find_packages(),
    install_requires=[
        'openai==0.27.8',
        'tiktoken==0.4.0',
    ],
    author='Sambuddha Basu',
    description='Automatically route your prompts to the best OpenAI model',
    long_description=open('README.md').read(),
    long_description_content_type='text/markdown',
    url='https://github.com/sambuddhabasu/openai_model_router',
)
