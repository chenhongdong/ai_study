import streamlit as st
import os
from openai import OpenAI

# 设置页面的配置项
st.set_page_config(
  page_title="AI智能伴侣",
  page_icon="🤑",
  # 布局
  layout="wide",
  # 控制侧边栏的状态
  initial_sidebar_state="expanded",
  menu_items={}
)

# 大标题
st.title('AI智能伴侣')


# Logo
st.logo('./assets/imgs/logo.gif')


# 系统提示词
system_prompt = '你是一名非常可爱的AI助理，你的名字叫小智，请你使用温柔可爱的语气回答用户的问题'

# 初始化聊天信息(不会再重新运行时清空)
if "messages" not in st.session_state:
  st.session_state.messages = []

# 展示聊天信息
for msg in st.session_state.messages:
  if msg['role'] == 'user':
    st.chat_message('user').write(msg['content'])
  elif msg['role'] == 'assistant':
    st.chat_message('assistant').write(msg['content'])

# 创建与AI大模型交互的客户端对象
client = OpenAI(api_key='sk-ea459440fe7e402886c5b31eba372d17', base_url="https://api.deepseek.com")

# 消息输入框
prompt = st.chat_input('请输入您的问题')
if prompt:
  st.chat_message('user').write(prompt)
  print('-------------> 调用AI大模型，提示词：', prompt)
  # 添加用户输入的提示词
  st.session_state.messages.append({'role': 'user', 'content': prompt})

  # 调用AI大模型
  response = client.chat.completions.create(
    model='deepseek-chat',
    messages=[
      {'role': 'system', 'content': system_prompt},
      {'role': 'user', 'content': prompt}
    ],
    stream=False
  )

  # 输出大模型返回的结果(非流式输出)
  ai_content = response.choices[0].message.content
  print('<----------- 大模型返回的结果：', ai_content)
  st.chat_message('assistant').write(ai_content)
  # 保存大模型返回的结果
  st.session_state.messages.append({'role': 'assistant', 'content': ai_content})
