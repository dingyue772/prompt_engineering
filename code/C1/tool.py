import os
import openai
from dotenv import load_dotenv, find_dotenv

_ = load_dotenv(find_dotenv())

openai.api_key = os.environ['OPENAI_API_KEY']
openai.api_base = 'https://api.zyai.online/v1'

def get_completion(prompt, temperature=0):
    model="gpt-3.5-turbo"
    '''
    prompt: 对应的提示词
    model: 调用的模型，默认为 gpt-3.5-turbo(ChatGPT)
    '''
    messages = [{"role": "user", "content": prompt}]
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # 模型输出的温度系数，控制输出的随机程度
    )
    # 调用 OpenAI 的 ChatCompletion 接口
    return response.choices[0].message["content"]

def get_completion_from_messages(messages, model="gpt-3.5-turbo", temperature=0):
    response = openai.ChatCompletion.create(
        model=model,
        messages=messages,
        temperature=temperature, # 控制模型输出的随机程度
    )
    return response.choices[0].message["content"]

