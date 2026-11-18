import streamlit as st
import os
from openai import OpenAI
from datetime import datetime
import json
import time

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
st.logo('resources/imgs/logo.gif')

# 保存会话方法
def save_session():
  if st.session_state.current_session:
    # 创建会话数据
    session_data = {
      "nick_name": st.session_state.nick_name,
      "nature": st.session_state.nature,
      "current_session": st.session_state.current_session,
      "messages": st.session_state.messages
    }
    # 创建会话存储目录
    # if not os.path.exists('sessions'):
    #   os.mkdir('sessions')
    os.makedirs('sessions', exist_ok=True)
    # 保存会话记录
    with open(f"sessions/{st.session_state.current_session}.json", 'w', encoding='utf-8') as f:
      json.dump(session_data, f, ensure_ascii=False, indent=2)

# 生成会话名称
def genrate_session_name():
  return time.strftime('%Y-%m-%d_%H-%M-%S')

# 加载会话方法
def load_sessions():
  sessions = []
  if os.path.exists('sessions'):
    list = os.listdir('sessions')
    for file in list:
      if file.endswith('.json'):
        sessions.append(file[0:-5:1])
  sessions.sort(reverse=True)
  return sessions

# 删除指定会话
def del_session(session):
  try:
    if os.path.exists(f'sessions/{session}.json'):
      os.remove(f'sessions/{session}.json')
      # 如果删除的是当前会话，就需要清空聊天数据并重新给current_session赋值
      if session == st.session_state.current_session:
        st.session_state.current_session = genrate_session_name()
        st.session_state.messages = []
  except Exception:
    st.error('删除会话有点问题了啊')

# 加载指定会话
def load_session(session_name):
  try:
    if os.path.exists(f'sessions/{session_name}.json'):
      with open(f'sessions/{session_name}.json', 'r', encoding='utf-8') as f:
        session_data = json.load(f)
        st.session_state.messages = session_data['messages']
        st.session_state.nick_name = session_data['nick_name']
        st.session_state.nature = session_data['nature']
        st.session_state.current_session = session_name
  except Exception:
    st.error('加载出问题了')



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
if "current_session" not in st.session_state:
  st.session_state.current_session = genrate_session_name()


# 左侧侧边栏
# st.sidebar.subheader('伴侣信息')
# nick_name = st.sidebar.text_input("昵称")

# 左边侧边栏 - with: streamlit中上下文的管理器
with st.sidebar:
  # 会话信息
  st.subheader('AI控制面板')

  # 新建会话
  if st.button('新建会话', width='stretch', icon='✏️'):
    # 1. 保存当前会话，有聊天信息时才进行保存
    save_session()

    # 2. 保存新建会话
    if st.session_state.messages:
      st.session_state.messages = []
      st.session_state.current_session = genrate_session_name()
      save_session()
      # 重新运行当前页面
      st.rerun()

  # 历史会话
  st.text('历史会话')

  session_list = load_sessions()
  for session in session_list:
    col1, col2 = st.columns([4, 1])
    with col1:
      if st.button(session, width='stretch', icon='📄',type='primary' if session == st.session_state.current_session else 'secondary'):
        load_session(session)
        st.rerun()
    with col2:
      if st.button('', width='stretch', icon='❌️', key=f'delete_{session}'):
        del_session(session)
        st.rerun()

  # 分割线
  st.divider()

  st.subheader('伴侣信息')
  # 昵称输入框
  nick_name = st.text_input('昵称', value=st.session_state.nick_name, placeholder='请输入昵称')
  if nick_name:
    st.session_state.nick_name = nick_name
  # 性格输入框
  nature = st.text_area('性格', value=st.session_state.nature, placeholder='请输入性格')
  if nature:
    st.session_state.nature = nature
    

st.text(f'当前对话：{st.session_state.current_session}')

# 展示聊天信息
for msg in st.session_state.messages:
  st.chat_message(msg['role']).write(msg['content'])

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

  # 大模型返回结果后保存会话
  save_session()


