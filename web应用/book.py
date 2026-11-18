from fastapi import APIRouter

book = APIRouter()

@book.get('/')
def get_books():
  return {'code': 0, 'msg': 'ok', 'data': [
    {'id': 1, 'name': '《西游记》'},
    {'id': 2, 'name': '《水浒传》'},
    {'id': 3, 'name': '《三国演义》'}
  ]}