import streamlit as st

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


# 消息输入框
prompt = st.chat_input('请输入您的问题')
if prompt:
  st.write(f"用户：{prompt}")