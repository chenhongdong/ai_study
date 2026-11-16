# 调用对话API
import os
from openai import OpenAI

client = OpenAI(
    api_key=os.environ.get('DEEPSEEK_API_KEY'),
    base_url="https://api.deepseek.com")

response = client.chat.completions.create(
    model="deepseek-chat",
    messages=[
        {"role": "system", "content": "你是一名可爱的AI助理，你叫小甜甜"},
        {"role": "user", "content": "12个苹果，3个人，怎么均分？"}
    ],
    stream=False
)

print(response.choices[0].content.message)