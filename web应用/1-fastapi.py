from fastapi import FastAPI
from book import book
from user import user

from tortoise.contrib.fastapi import register_tortoise
from settings import TORTOISE_ORM


app = FastAPI()
# 路由分发到/book和/user，方便对不同的模块及接口进行管理，不至于都写在根路由下
app.include_router(book, prefix='/book')
app.include_router(user, prefix='/user')


@app.get('/')
def root():
  return {'code': 0, 'msg': 'ok', 'data': [{'role':'user','content':'开始'}]}

@app.get('/class')
def get_class():
  return [
    {'id': 1, 'name': 'Python'},
    {'id': 2, 'name': 'FastAPI'}
  ]

# 启动服务 ————> uvicorn: Python中的轻量级web服务器
if __name__ == '__main__':
  import uvicorn
  uvicorn.run(app, host='127.0.0.1', port=8000)