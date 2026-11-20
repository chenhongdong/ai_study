from langchain.agents import create_agent
from langchain.chat_models import init_chat_model
from langchain.messages import HumanMessage

# 1. 创建模型
model = init_chat_model(
  model='deepseek-flash',
  extra_body={'thinking': {'type': 'disabled'}}  # 默认开启思考模式，不需要就关闭disabled
)

# response = model.invoke('你觉得BTC在2027年2月份跌到4万吗？')

# print(response)

# 2.智能体流式变化
agent = create_agent(
  model,
  tools=[],
  system_prompt='你是王者荣耀里的妲己，现在你是我的智能AI助手，按照你的风格去回答问题'
)

stream = agent.stream_events(
  {'messages': [HumanMessage('你觉得Solana未来的发展怎么样，并且代币sol会不会涨到$1000')]},
  version='v3'
)

for msg in stream.messages:
  for chunk in msg.text:
    print(chunk, end='', flush=True)