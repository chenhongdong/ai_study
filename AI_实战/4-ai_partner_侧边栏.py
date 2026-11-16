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
system_prompt = '''
  你叫 %s，现在是用户的真实伴侣，请完全代入伴侣角色。
  规则：
    1.每次只回1条消息
    2.禁止任何场景或状态描述性文字
    3.匹配用户的语言
    4.回复简短，像微信聊天一样
    5.有需要的话可以用❤️🌺等emoji表情
    6.用符合伴侣性格的方式对话
    7.回复的内容，要充分体现伴侣的性格特征
  伴侣性格：
    - %s
  你必须严格遵守上述规则来回复用户。
'''

# 初始化聊天信息(不会再重新运行时清空)
if "messages" not in st.session_state:
  st.session_state.messages = []

if "nick_name" not in st.session_state:
  st.session_state['nick_name'] = '小狗公主'

if "nature" not in st.session_state:
  st.session_state.nature = '活泼开朗的大同姑娘'



# 左侧侧边栏
# st.sidebar.subheader('伴侣信息')
# nick_name = st.sidebar.text_input("昵称")

# 左边侧边栏 - with: streamlit中上下文的管理器
with st.sidebar:
  st.subheader('伴侣信息')
  # 昵称输入框
  nick_name = st.text_input('昵称', value=st.session_state.nick_name, placeholder='请输入昵称')
  if nick_name:
    st.session_state.nick_name = nick_name
  # 性格输入框
  nature = st.text_area('性格', value=st.session_state.nature, placeholder='请输入性格')
  if nature:
    st.session_state.nature = nature


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
      {'role': 'system', 'content': system_prompt % (st.session_state.nick_name, st.session_state.nature)},
      *st.session_state.messages
    ],
    stream=True
  )

  # 输出大模型返回的结果(非流式输出)
  container = st.empty() # 创建一个空组件，用于展示大模型返回的结果
  res_msg = ''
  for chunk in response:
    if chunk.choices[0].delta.content is not None:
      res_msg += chunk.choices[0].delta.content
      container.chat_message('assistant').write(res_msg)
  
  # 保存大模型返回的结果
  st.session_state.messages.append({'role': 'assistant', 'content': res_msg})
