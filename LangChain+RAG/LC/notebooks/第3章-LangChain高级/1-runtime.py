from dataclasses import dataclass
from dotenv import load_dotenv
from langchain.messages import HumanMessage
from langchain.tools import ToolRuntime, tool
from langchain.agents import create_agent, AgentState
from langchain.chat_models import init_chat_model
from langchain_core.messages.tool import tool_call
from langgraph.checkpoint.memory import InMemorySaver
from langgraph.types import Command

# 加载环境变量
load_dotenv()


# 1. Context（运行上下文）
USER_DATABASE = {
  'school_a': {
    'u001': {'name': '胡歌', 'course': 'LangChain 开发指南'},
    'u002': {'name': '杨幂', 'course': 'Java开发入门'}
  },
  'school_b': {
    'u001': {'name': '霍建华', 'course': 'Python 入门'},
    'u002': {'name': '刘诗诗', 'course': 'Langgraph+RAG实战'}
  }
}

# 1.1 定义ContextSchema
@dataclass
class UserContext():
  user_id: str    # 用户id
  tenant_id: str  # 租户id

# 1.2 在Tool中使用Context
@tool
def get_current_user_profile(runtime: ToolRuntime[UserContext]):
  ''' 获取当前用户信息 '''
  ctx = runtime.context
  print('当前上下文：', ctx)
  profile = USER_DATABASE.get(ctx.tenant_id, {}).get(ctx.user_id)
  return f'当前用户信息是{profile['name']}和{profile['course']}'

# 1.3 在Agent中添加Context
model = init_chat_model(
  model='deepseek-flash',
  extra_body={'thinking': {'type': 'disabled'}}
)

# agent = create_agent(
#   model=model,
#   tools=[get_current_user_profile],
#   system_prompt='你是一名AI助手，负责帮我查看资料',
#   context_schema=UserContext
# )

# context = UserContext(tenant_id='school_b', user_id='u001')

# config = {'configurable': {'thread_id': '1'}}

# response = agent.invoke(
#   {'messages': [HumanMessage('检查我的课程')]},
#   config=config,
#   context=context
# )

# for msg in response['messages']:
#   msg.pretty_print()





# 2. State-短期记忆
# 2.1 自定义State
class CustomState(AgentState):
  model_call_count: int

# 2.2 在Tool中访问state
@tool
def get_model_call_count(runtime: ToolRuntime):
  ''' 调用模型次数工具 '''
  count = runtime.state.get('model_call_count', 0)
  update = {
    'messages': {
      contetn: '成功更新工具调用次数',
      tool_call: runtime.tool_call_id
    },
    'model_call_count': count + 1
  }

  return Command(update=update)

# 2.3 创建agent指定state
checkpointer = InMemorySaver()
agent = create_agent(
  model,
  state_schema=CustomState,
  tools=[get_model_call_count],
  checkpointer=checkpointer,
  system_prompt='你是ai助手，你需要在每次回答用户前调用工具记录模型调用次数'
)