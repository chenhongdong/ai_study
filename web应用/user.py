from fastapi import APIRouter, Request

user =APIRouter()

@user.get('/')
def get_users(request: Request):
  if request.query_params.get('name') == '乔峰':
    return {'id': 1, 'name': '乔峰'}
  elif request.query_params.get('name') == '慕容复':
    return {'id': 2, 'name': '慕容复'}
  return [
    {'id': 1, 'name': '乔峰'},
    {'id': 2, 'name': '慕容复'},
    {'id': 3, 'name': '段誉'},
    {'id': 4, 'name': '虚竹'}
  ]