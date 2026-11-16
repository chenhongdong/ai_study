# 字典：使用键值对存储，每个键对应一个值，通过key找到value

dict = {"王林": 670, "李木碗": 608, "许力国": 580, "韩立": 688, "a": {"aa": 100}}

print(dict)
print(type(dict))

# 查询
print(dict['韩立'])

keys = dict.keys()
print(keys)

values = dict.values()
print(values)

items = dict.items()
print(items)

# 删除
# score = dict.pop('韩立')
# print(score)
# del dict['王林']
# print('删除后的字典：',dict)


# 遍历
for k,v in dict.items():
    print(f"{k}的成绩是{v}")


# list.copy()为什么仍可能共享嵌套对象?
# 因为list.copy()只复制了一层，而嵌套对象的引用没有被复制，所以会共享嵌套对象。
# 解决方法：使用copy.deepcopy()方法，它可以复制嵌套对象。
import copy

# 深拷贝
# d2 = dict.copy()
d2 = copy.deepcopy(dict)
d2['a']['aa'] = 888
print(d2)
print(dict)




# def echo_title(title: str) -> str:
#   return title

# print(echo_title(42))

# 用自己写的函数处理标题与文件类型：去空白、类型大小写规范化、空标题与非法类型拒绝、错误输入类型明确报错。
def echo_title(title: str) -> str:
  if not title:
    return ValueError("标题不能为空")
  if not isinstance(title, str):  
    return ValueError("标题必须为字符串类型")
  title = title.strip()
  # title = title.title()  # 以标题为主的格式，首字母大写，其余小写
  title = title.lower() # 全部小写
  return title


# print(echo_title("  chdAAAjxkslaA  "))
print(echo_title(44))


# 做一个小型控制流练习：把混合大小写的文件类型列表筛成允许类型，不修改原列表，解释循环与推导式两种写法
