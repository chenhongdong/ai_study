from fastapi import APIRouter
from app.models.schemas import ChatRequest
from app.agents.personal_cook import search_recipes, get_message, clear_messages
from fastapi.responses import StreamingResponse

router = APIRouter()

@router.post('/chat/stream')
async def chat_endpoint(request: ChatRequest):
  '''流式对话'''
  return StreamingResponse(
    search_recipes(request.message, request.image_url, request.thread_id),
    media_type='text/event-stream'
  )

@router.get('/chat/messages')
async def get_chat_messages(thread_id: str):
  '''获取历史消息'''
  message = get_message(thread_id)
  return {'messages': message}


@router.delete('/chat/messages')
async def clear_chat_messages(thread_id: str):
  '''清空历史消息'''
  clear_messages(thread_id)
  return {'success': True}