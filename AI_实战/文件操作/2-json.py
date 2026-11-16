# 读写JSON格式文件

import json

# 写入json数据
user = {
    "name": "张三",
    "age": 18,
    "hobbies": ["阅读", "游泳"],
    "skill": ["前端工程师", "创业中", "转行中"]
}

# with open('resources/user.json', 'w', encoding='utf-8') as f:
#     json.dump(user, f, ensure_ascii=False, indent=2)



with open('resources/user.json', 'r', encoding='utf-8') as f:
    obj = json.load(f)
    print(obj)
    print(type(obj))